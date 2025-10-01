import os
import requests
import gzip
import logging
from botocore.exceptions import ClientError
from .config import (
    OUTPUT_METHOD,
    HTTP_ENDPOINT,
    TLS_CERT_PATH,
    TLS_KEY_PATH,
    AUTH_METHOD,
    AUTH_TOKEN,
    API_KEY,
    OUTPUT_DIR,
    COMPRESS_OUTPUT_FILE,
)

def download_file(s3_client, bucket_name, object_key):
    try:
        response = s3_client.get_object(Bucket=bucket_name, Key=object_key)
        return response['Body'].read()
    except ClientError as e:
        logging.error(f"Failed to download file: s3://{bucket_name}/{object_key}, error: {e}")
        raise

def process_log_file(s3_client, bucket_name, object_key):
    raw_content = download_file(s3_client, bucket_name, object_key)
    try:
        text_content = gzip.decompress(raw_content).decode('utf-8')
    except Exception:
        text_content = raw_content.decode('utf-8')
    logs = text_content.split('\n')

    if OUTPUT_METHOD == 'console':
        _emit_console_logs(object_key, logs)
        return

    if OUTPUT_METHOD == 'files':
        local_path = os.path.join(OUTPUT_DIR, object_key)

        # Determine output path and opener based on compression setting
        if COMPRESS_OUTPUT_FILE:
            out_path = local_path if local_path.lower().endswith('.gz') else local_path + '.gz'
            logging.info(f"Output path: {out_path}")
            opener = lambda path: gzip.open(path, 'at')
        else:
            out_path = local_path[:-3] if local_path.lower().endswith('.gz') else local_path
            logging.info(f"Output path: {out_path}")
            opener = lambda path: open(path, 'a')

        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        with opener(out_path) as file:
            for log in logs:
                if log.strip():
                    write_log_to_file(log, file)
    else:
        for log in logs:
            if log.strip():
                send_log_to_http(log)


def _emit_console_logs(object_key, logs):
    print(f"------------ object: {object_key} ------------")
    for log_line in logs:
        line = log_line.rstrip('\r\n')
        if line:
            print(line)

def send_log_to_http(log):
    try:
        headers = {'Content-Type': 'application/json'}
        cert = None

        if TLS_CERT_PATH and TLS_KEY_PATH:
            cert = (TLS_CERT_PATH, TLS_KEY_PATH)

        if AUTH_METHOD == 'token' and AUTH_TOKEN:
            headers['Authorization'] = f'Bearer {AUTH_TOKEN}'
        elif AUTH_METHOD == 'api_key' and API_KEY:
            headers['X-API-Key'] = API_KEY

        response = requests.post(HTTP_ENDPOINT, data=log, headers=headers, cert=cert)
        response.raise_for_status()
        logging.debug(f"Log {log} forwarded successfully to HTTP endpoint {HTTP_ENDPOINT}")
    except Exception as e:
        logging.error(f"Failed to forward log {log} to HTTP endpoint {HTTP_ENDPOINT}, error: {e}")

def write_log_to_file(log, file):
    try:
        file.write(log + '\n')
        logging.debug(f"Log {log} written successfully to file {file.name}")
    except Exception as e:
        logging.error(f"Failed to write log {log} to file {file.name}, error: {e}")
