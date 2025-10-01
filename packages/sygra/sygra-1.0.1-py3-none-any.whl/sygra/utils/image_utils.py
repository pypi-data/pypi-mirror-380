import base64
import io
import os
import re
from typing import Any, Optional

import requests  # type: ignore[import-untyped]
from PIL import Image

from sygra.logger.logger_config import logger

# Curated list of common user-facing image file extensions
COMMON_IMAGE_EXTENSIONS = (
    ".jpg",
    ".jpeg",
    ".png",
    ".gif",
    ".bmp",
    ".tiff",
    ".tif",
    ".webp",
    ".ico",
    ".apng",
)


def load_image(data: Any) -> Optional[Image.Image]:
    """
    Attempt to load an image from various types of inputs.

    Args:
        data (Any): The input data which can be an Image object, bytes, a file path, or a URL.

    Returns:
        Optional[Image.Image]: The loaded PIL Image object or None if loading fails.
    """
    try:
        if isinstance(data, Image.Image):
            return data
        if isinstance(data, dict) and isinstance(data.get("bytes"), bytes):
            return Image.open(io.BytesIO(data["bytes"]))
        if isinstance(data, bytes):
            return Image.open(io.BytesIO(data))
        if isinstance(data, str):
            if data.startswith("http"):
                response = requests.get(data, timeout=5)
                response.raise_for_status()
                return Image.open(io.BytesIO(response.content))
            if os.path.exists(data):
                return Image.open(data)
        logger.warning(f"Unsupported image data format: {type(data)}")
        return None
    except Exception as e:
        logger.warning(f"Failed to load image: {e}")
        return None


def get_image_fields(record: dict[str, Any]) -> list[str]:
    """
    Identify keys in a record that likely contain image data.

    Args:
        record (dict[str, Any]): The record to inspect.

    Returns:
        list[str]: A list of keys that contain image-like data.
    """
    image_fields = set()

    for key, value in record.items():
        if is_data_url(value) or is_image_like(value):
            image_fields.add(key)
        elif isinstance(value, list):
            # Only check the first item in the list for image-like data
            if value and (is_image_like(value[0]) or is_data_url(value[0])):
                image_fields.add(key)

    if not image_fields:
        logger.warning("No image fields found in the record.")
    return list(image_fields)


def is_data_url(val: Any) -> bool:
    """
    Check if value is already a base64 data URL.

    Args:
        val (Any): The value to check.

    Returns:
        bool: True if the value is a data URL, False otherwise.
    """
    return isinstance(val, str) and val.startswith("data:image/")


def is_valid_image_bytes(data: bytes) -> bool:
    """
    Safely verify whether bytes represent a valid image.

    Args:
        data (bytes): The byte data to check.

    Returns:
        bool: True if the bytes represent a valid image, False otherwise.
    """
    try:
        Image.open(io.BytesIO(data)).verify()
        return True
    except Exception:
        return False


def is_image_like(val: Any) -> bool:
    """
    Check if a value looks like valid image content.

    Args:
        val (Any): The value to check.

    Returns:
        bool: True if the value is an image or looks like an image, False otherwise.
    """
    if isinstance(val, Image.Image):
        return True
    elif isinstance(val, dict) and isinstance(val.get("bytes"), bytes):
        return is_valid_image_bytes(val["bytes"])
    elif isinstance(val, bytes):
        return is_valid_image_bytes(val)
    elif isinstance(val, str):
        return (
            val.startswith("http") and val.lower().endswith(COMMON_IMAGE_EXTENSIONS)
        ) or val.lower().endswith(  # URL check
            COMMON_IMAGE_EXTENSIONS
        )  # Local file check
    return False


def get_image_url(image: Image.Image) -> str:
    """
    Convert a PIL Image to a base64-encoded data URL string.

    Args:
        image (Image.Image): The PIL Image to convert.

    Returns:
        str: The base64-encoded data URL string representing the image.
    """
    try:
        image_bytes_io = io.BytesIO()
        format = image.format or "PNG"
        image.save(image_bytes_io, format=format)
        encoded = base64.b64encode(image_bytes_io.getvalue()).decode("utf-8")
        mime_type = f"image/{format.lower()}"
        return f"data:{mime_type};base64,{encoded}"
    except Exception as e:
        logger.warning(f"Failed to encode image to data URL: {e}")
        return ""


def expand_image_item(item: dict[str, Any], state: dict[str, Any]) -> list[dict[str, Any]]:
    """
    Expand an image item with a variable URL into multiple items if necessary.

    Args:
        item (dict[str, Any]): The image item to expand.
        state (dict[str, Any]): The current state containing variable values.

    Returns:
        list[dict[str, Any]]: A list of expanded image items.
    """
    key_match = re.findall(r"{(.*?)}", item["image_url"])
    expanded = []
    if key_match:
        assert len(key_match) == 1, "Only one variable is expected in image_url"
        var_name = key_match[0]
        val = state.get(var_name)
        if isinstance(val, list):
            for img_url in val:
                expanded.append({"type": "image_url", "image_url": img_url})
        else:
            expanded.append({"type": "image_url", "image_url": val})
    else:
        expanded.append(item)
    return expanded
