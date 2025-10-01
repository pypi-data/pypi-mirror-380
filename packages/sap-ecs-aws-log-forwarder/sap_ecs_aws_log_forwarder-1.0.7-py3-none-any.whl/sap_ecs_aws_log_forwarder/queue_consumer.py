import time
import logging
import os
import boto3
from .config import (
    AWS_ACCESS_KEY_ID,
    AWS_SECRET_ACCESS_KEY,
    AWS_REGION,
    SQS_QUEUE_URL,
    TIMEOUT_DURATION,
    LOGSERV_LOG_INCLUDE_FILTERS,
    LOGSERV_LOG_EXCLUDE_FILTERS,
    LOG_LEVEL,
    OUTPUT_METHOD,
)
from .log_processor import process_log_file
from .message_processing import QueueMessageProcessor

# Global Variables
# Initialize SQS and S3 clients
RELEVANT_ENV_VARS = [
    "AWS_ACCESS_KEY_ID",
    "AWS_REGION",
    "SQS_QUEUE_URL",
    "OUTPUT_METHOD",
    "TIMEOUT_DURATION",
    "LOGSERV_LOG_INCLUDE_FILTERS",
    "LOGSERV_LOG_EXCLUDE_FILTERS",
    "HTTP_ENDPOINT",
    "TLS_CERT_PATH",
    "TLS_KEY_PATH",
    "AUTH_METHOD",
    "AUTH_TOKEN",
    "API_KEY",
    "OUTPUT_DIR",
    "COMPRESS_OUTPUT_FILE",
    "LOG_LEVEL",
]

MAX_RETRIES = 5  # Maximum number of retries for a message
CONSOLE_MODE = OUTPUT_METHOD == "console"

def set_log_level():
    """Set the log level based on the LOG_LEVEL config."""
    numeric_level = getattr(logging, LOG_LEVEL, logging.INFO)
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(message)s",
        level=numeric_level,
    )
    logging.info("Log level set to %s", logging.getLevelName(numeric_level))


def log_env_vars():
    """Log relevant environment variables at DEBUG level."""
    logging.info("Relevant environment variables:")
    for key in RELEVANT_ENV_VARS:
        logging.info("%s=%s", key, os.getenv(key))

def has_timed_out(start_time, timeout_duration):
    if timeout_duration is None:
        return False
    return (time.time() - start_time) > timeout_duration

def is_relevant_event(bucket_name, object_key):
    """Filter relevant events based on include/exclude filters."""
    bucket = (bucket_name or "").lower()
    key = (object_key or "").lower()
    subject = f"{bucket}/{key}" if bucket else key

    if "logserv" not in subject:
        return False
    if LOGSERV_LOG_EXCLUDE_FILTERS and any(ex in subject for ex in LOGSERV_LOG_EXCLUDE_FILTERS):
        return False
    if LOGSERV_LOG_INCLUDE_FILTERS:
        if not any(filt in subject for filt in LOGSERV_LOG_INCLUDE_FILTERS):
            return False
    return True

def consume_queue():
    # Set log level
    set_log_level()
    log_env_vars()

    logging.info("Starting queue consumer...")
    sqs_client = boto3.client(
        "sqs",
        region_name=AWS_REGION,
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    )
    s3_client = boto3.client(
        "s3",
        region_name=AWS_REGION,
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    )

    processor = QueueMessageProcessor(
        sqs_client=sqs_client,
        s3_client=s3_client,
        queue_url=SQS_QUEUE_URL,
        process_log_file=process_log_file,
        relevance_checker=is_relevant_event,
        max_retries=MAX_RETRIES,
    )

    start_time = time.time()
    try:
        while True:
            if has_timed_out(start_time, TIMEOUT_DURATION):
                logging.info("Timeout reached. Exiting.")
                break

            response = sqs_client.receive_message(
                QueueUrl=SQS_QUEUE_URL,
                MaxNumberOfMessages=10,
                WaitTimeSeconds=20,
                VisibilityTimeout=10,
                AttributeNames=["ApproximateReceiveCount"],
            )
            messages = response.get("Messages", [])
            if not messages:
                logging.info("No messages in the queue. Waiting...")
                time.sleep(20)
                continue

            for message in messages:
                processor.process(message)

    except KeyboardInterrupt:
        logging.info("Forwarder stopped by user.")
    except Exception as e:
        logging.error("An error occurred: %s", e)


if __name__ == "__main__":
    consume_queue()
