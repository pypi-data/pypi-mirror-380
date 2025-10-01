from pathlib import Path
from typing import Final

from ..types import ImageFormat


# Maps file extensions to canonical format names
_EXT_TO_FORMAT: Final[dict[str, ImageFormat]] = {
    "jpg": "JPEG",
    "jpeg": "JPEG",
    "png": "PNG",
    "webp": "WEBP",
    "tif": "TIFF",
    "tiff": "TIFF",
    "bmp": "BMP",
    "gif": "GIF",
    "ico": "ICO",
    "heic": "HEIC",
    "svg": "SVG",
    "pdf": "PDF",
}


def guess_image_format(
    file_path: str,
    default: ImageFormat | None = None
) -> ImageFormat | None:
    """
    Guess image format from the file path extension.

    Examples:
        guess_image_format("/path/to/image.jpg")  -> "JPEG"
        guess_image_format("/path/to/photo.png")  -> "PNG"
        guess_image_format("/path/to/img.webp")   -> "WEBP"
        guess_image_format("/path/to/file.unknown", default="PNG") -> "PNG"

    Args:
        file_path: The file path string.
        default:   Optional fallback format to return when the extension is unknown
                   or missing. If None and the extension is unknown, returns the
                   uppercase extension (e.g., 'DDS' for '.dds'). If no extension
                   is present and default is None, raises ValueError.

    Returns:
        ImageFormat: Canonical format string, e.g. "JPEG", "PNG", "WEBP".

    Raises:
        ValueError: If the path has no extension and no default is provided.
    """
    ext = Path(file_path).suffix.lower().lstrip(".")

    if not ext:
        if default is not None:
            return default
        raise ValueError(f"Cannot determine image format from path without extension: {file_path!r}")

    fmt = _EXT_TO_FORMAT.get(ext)
    if fmt:
        return fmt

    # Fallback: use the uppercase extension or the provided default
    return default
