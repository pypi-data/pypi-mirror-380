"""
IA Parc Inference data handler
"""
import os
#import io
import logging
import logging.config
from typing import Any
import iap_messenger.decoders as decoders

Error = ValueError | None

LEVEL = os.environ.get('LOG_LEVEL', 'INFO').upper()
logging.basicConfig(
    level=LEVEL,
    force=True,
    format="%(name)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
LOGGER = logging.getLogger("Inference")
LOGGER.propagate = True


def decode(raw: bytes, content_type: str="", conf=None) -> tuple[Any, Error]:
    if conf is None:
        conf = {}
    if content_type == "":
        content_type = conf.get("type", "json")
    if content_type == "multimodal" or content_type == "multipart":
        # Handle boundary detection if not in content_type
        if "boundary" not in content_type:
            boundary = decoders._get_boundary(raw)
            LOGGER.info(f"Detected boundary: '{boundary}'")
            if boundary:
                content_type = f"multipart/form-data; boundary={boundary}"
            else:
                LOGGER.error("Could not detect boundary in multipart data")
                return None, ValueError("Could not detect boundary in multipart data")
        
        raw_items, error = decoders.decode_multipart(
            raw, conf, content_type, use_lz4=False)
        
        if error:
            LOGGER.error(f"Error in multipart decoding: {error}")
            return None, error
        
        if len(conf.get("items", [])) == 0:
            return decoders.decode(raw_items[conf["name"]], conf["type"])
        else:
            result = {}
            for item in conf["items"]:
                item_data = raw_items.get(item["name"])
                if item_data:
                    result[item["name"]], error = decoders.decode(
                        item_data, item["type"])
                    LOGGER.info(f"Decoded item '{item['name']}': {result[item['name']]}")
                    if error:
                        LOGGER.error(f"Error decoding {item['name']}: {error}")
                        return None, error
                else:
                    LOGGER.warning(f"No data found for field {item['name']}")
            return result, None
    else:
        return decoders.decode(raw, content_type)
