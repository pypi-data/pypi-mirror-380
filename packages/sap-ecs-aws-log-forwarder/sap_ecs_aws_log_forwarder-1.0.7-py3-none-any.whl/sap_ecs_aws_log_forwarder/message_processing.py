import json
import logging
from typing import Any, Callable, Dict, List

from botocore.exceptions import ClientError


def format_metadata(metadata: Dict[str, Any]) -> str:
    formatted = {}
    for key, value in metadata.items():
        formatted[key] = value.isoformat() if hasattr(value, "isoformat") else value
    payload = json.dumps(formatted, sort_keys=True, indent=2, default=str)
    return "  " + payload.replace("\n", "\n  ")


def log_message_metadata(message: Dict[str, Any], prefix: str = "") -> None:
    metadata = {
        "id": message.get("MessageId"),
        "receipt_handle": message.get("ReceiptHandle"),
        "receive_count": message.get("Attributes", {}).get("ApproximateReceiveCount"),
    }
    prefix_text = f"{prefix} - " if prefix else ""
    logging.debug("%sMessage metadata:\n%s", prefix_text, format_metadata(metadata))


class QueueMessageProcessor:
    def __init__(
        self,
        *,
        sqs_client,
        s3_client,
        queue_url: str,
        process_log_file: Callable[[Any, str, str], None],
        relevance_checker: Callable[[str, str], bool],
        max_retries: int,
    ) -> None:
        self.sqs_client = sqs_client
        self.s3_client = s3_client
        self.queue_url = queue_url
        self.process_log_file = process_log_file
        self.relevance_checker = relevance_checker
        self.max_retries = max_retries

    def process(self, message: Dict[str, Any]) -> None:
        message_id = message.get("MessageId")
        receipt_handle = message.get("ReceiptHandle")
        log_message_metadata(message, prefix="Received")

        body_text = message.get("Body", "")
        try:
            payload = json.loads(body_text)
        except json.JSONDecodeError as exc:
            logging.error("Failed to decode message %s: %s", message_id, exc)
            self._delete_message(message_id, receipt_handle, reason="decode-error")
            return

        records: List[Dict[str, Any]] = payload.get("Records", [])
        if not records:
            logging.debug("Message %s contains no Records payload. Deleting.", message_id)
            self._delete_message(message_id, receipt_handle, reason="empty-records")
            return

        # Process each record. We stop after the first outcome that deletes or requeues the message.
        for index, record in enumerate(records):
            if self._process_record(message, payload, record, index):
                break

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------
    def _process_record(
        self,
        message: Dict[str, Any],
        message_body: Dict[str, Any],
        record: Dict[str, Any],
        record_index: int,
    ) -> bool:
        message_id = message.get("MessageId")
        receipt_handle = message.get("ReceiptHandle")

        event_type = record.get("eventName", "")
        s3_info = record.get("s3", {})
        bucket_name = s3_info.get("bucket", {}).get("name", "")
        object_key = s3_info.get("object", {}).get("key", "")

        if event_type != "ObjectCreated:Put" or not self.relevance_checker(bucket_name, object_key):
            logging.debug(
                "Irrelevant message: event_type=%s, object_path=s3://%s/%s. Skipping message.",
                event_type,
                bucket_name,
                object_key,
            )
            self._delete_message(message_id, receipt_handle, reason="irrelevant")
            return True

        retry_count = int(record.get("retry_count", 0))
        if retry_count >= self.max_retries:
            logging.error("Max retries reached for message: %s. Deleting message.", message_id)
            self._delete_message(message_id, receipt_handle, reason="max-retries")
            return True

        if not bucket_name or not object_key:
            logging.error("No bucket name or object key found in message: %s - %s", message_id, record)
            self._delete_message(message_id, receipt_handle, reason="missing-object")
            return True

        try:
            logging.info("Processing message: %s - s3://%s/%s", message_id, bucket_name, object_key)
            self.process_log_file(self.s3_client, bucket_name, object_key)
            self._delete_message(message_id, receipt_handle, reason="processed", log_success=True)
            return True
        except Exception as exc:  # pragma: no cover - exercised via tests
            return self._handle_processing_failure(
                message,
                message_body,
                record,
                record_index,
                exc,
            )

    def _handle_processing_failure(
        self,
        message: Dict[str, Any],
        message_body: Dict[str, Any],
        record: Dict[str, Any],
        record_index: int,
        error: Exception,
    ) -> bool:
        message_id = message.get("MessageId")
        receipt_handle = message.get("ReceiptHandle")
        retry_count = int(record.get("retry_count", 0))

        metadata = {
            "receive_count": message.get("Attributes", {}).get("ApproximateReceiveCount"),
            "retry_count": retry_count,
        }
        logging.error(
            "Error processing message %s: %s | metadata:\n%s",
            message_id,
            error,
            format_metadata(metadata),
        )

        retry_count += 1
        if retry_count >= self.max_retries:
            logging.error("Max retries reached during failure handling for message: %s. Deleting.", message_id)
            self._delete_message(message_id, receipt_handle, reason="max-retries")
            return True

        record["retry_count"] = retry_count
        message_body.setdefault("Records", [])[record_index] = record
        updated_body = json.dumps(message_body)

        try:
            self.sqs_client.send_message(QueueUrl=self.queue_url, MessageBody=updated_body)
            logging.debug("Message %s requeued with retry_count=%s.", message_id, retry_count)
        except ClientError as send_err:  # pragma: no cover - defensive
            logging.error("Failed to requeue message %s: %s", message_id, send_err)
            # If we cannot requeue, we fall back to deleting to avoid tight loops.
            self._delete_message(message_id, receipt_handle, reason="requeue-failed")
            return True

        self._delete_message(message_id, receipt_handle, reason="requeued")
        return True

    def _delete_message(self, message_id: str, receipt_handle: str, *, reason: str, log_success: bool = False) -> None:
        try:
            self.sqs_client.delete_message(QueueUrl=self.queue_url, ReceiptHandle=receipt_handle)
            logging.debug("Message %s deleted (%s).", message_id, reason)
            if log_success:
                logging.info("Message processed and deleted: %s", message_id)
        except ClientError as err:
            error_code = err.response.get("Error", {}).get("Code")
            if error_code in {"ReceiptHandleIsInvalid", "AWS.SimpleQueueService.NonExistentQueue"}:
                logging.debug("Message %s already removed by SQS (%s).", message_id, reason)
            else:
                raise
