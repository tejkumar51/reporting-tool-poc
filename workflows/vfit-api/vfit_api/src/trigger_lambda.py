import json
from src.common import log

import uuid

logger = log.setup_logging()


def handler(event=None, context=None):
    logger.info("trigger lambda_handler event: %s ", event)
    try:
        req_id = str(uuid.uuid4())
        logger.info("UUID generated: %s", req_id)
    except Exception as e:
        logger.exception("An error occurred while processing ")
        return json.dumps({"error": {"code": "INVALID_REQUEST", "fields": e}})

    return {
        "body": json.dumps({"statusCode": 200, "uuid": req_id}),
        "isBase64Encoded": False,
    }
