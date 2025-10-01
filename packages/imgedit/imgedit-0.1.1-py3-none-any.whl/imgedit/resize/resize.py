from typing import Literal

from PIL import Image, ImageFilter

from ..common import PILColor


type ImgBgImg = Literal['bg', 'bg_blur']
type ImgBg = PILColor | ImgBgImg


def resize_img_file(
    p_in:     str,

    size:       tuple[int, int],
    object_fit: Literal['fill', 'contain', 'cover'],

    bg:    ImgBg | None = None,
    p_out: str | None = None
) -> bool:
    """
    Resizes an image file to the specified size.

    Args:
        p_in: Path to input image file
        size: Target size as (width, height)
        object_fit: CSS like resizing value
        bg: Background color or image to use for fill ('bg' or 'bg_blur')
        p_out: Path to output image file (default: overwrite input)

    Returns:
        bool: True if successful, False otherwise
    """

    try:
        img_in = Image.open(p_in)
    except (IOError, OSError) as e:
        print(f"Error opening image file {p_in}: {e}")
        return False

    try:
        resized = resize_img_img(img_in, size, object_fit, bg)
    except ValueError as e:
        print(f"Error resizing image: {e}")
        return False

    try:
        resized.save(p_out or p_in)
    except (IOError, OSError) as e:
        print(f"Error saving image file {p_out or p_in}: {e}")
        return False

    return True


def resize_img_img(
    img_in:     Image.Image,

    size:       tuple[int, int],
    object_fit: Literal['fill', 'contain', 'cover'],

    bg: ImgBg | None = None
) -> Image.Image:
    """
    Resizes an image to the specified size.

    Args:
        img_in: Input image
        size: Target size as (width, height)
        object_fit: CSS like resizing value
        bg: Background color or image to use for fill ('bg' or 'bg_blur')

    Returns:
        Image.Image: Resized image
    """

    target_w, target_h = size
    if not isinstance(target_w, int) or not isinstance(target_h, int):
        raise ValueError('size must be a tuple of two integers (width, height)')
    if target_w <= 0 or target_h <= 0:
        raise ValueError('size must be positive')

    # Choose best available resampling method across Pillow versions
    try:
        resample = Image.Resampling.LANCZOS  # Pillow >= 9.1
    except AttributeError:
        resample = Image.LANCZOS if hasattr(Image, 'LANCZOS') else Image.ANTIALIAS # type: ignore

    in_w, in_h = img_in.size

    if object_fit == 'fill':
        # Stretch to target size (aspect ratio not preserved)
        return img_in.resize((target_w, target_h), resample=resample)

    # For contain/cover we preserve aspect ratio
    # Compute the uniform scale factor first
    scale = min(target_w / in_w, target_h / in_h) if object_fit == 'contain' else max(target_w / in_w, target_h / in_h)

    new_w = max(1, int(round(in_w * scale)))
    new_h = max(1, int(round(in_h * scale)))
    resized = img_in.resize((new_w, new_h), resample=resample)

    if object_fit == 'contain':
        # Letterbox/pillarbox into target size canvas, centered
        # Use a neutral background based on the image mode (0 works for L/RGB/RGBA/P etc.)
        background = Image.new(img_in.mode, (target_w, target_h), 0)

        if bg is not None:
            if bg in ['bg', 'bg_blur']:
                bg_overlay = resize_img_img(
                    img_in,
                    size=(target_w, target_h),
                    object_fit='cover'
                )

                if bg == 'bg_blur':
                    blur_radius = (target_w + target_h) / 2 / 25

                    bg_overlay = bg_overlay.filter(ImageFilter.GaussianBlur(blur_radius))

                background.paste(bg_overlay, (0, 0))
            else:
                background = Image.new(img_in.mode, (target_w, target_h), bg)

        offset_x = (target_w - new_w) // 2
        offset_y = (target_h - new_h) // 2

        # Preserve transparency when pasting if image has alpha
        mask = None
        if resized.mode in ('RGBA', 'LA'):
            try:
                mask = resized.getchannel('A')  # Prefer this over split()[3]
            except Exception:
                mask = resized.split()[3]  # Fallback

        if mask is not None:
            background.paste(resized, (offset_x, offset_y), mask=mask)
        else:
            background.paste(resized, (offset_x, offset_y))

        return background

    if object_fit == 'cover':
        # Center-crop to target size
        left = max(0, (new_w - target_w) // 2)
        top = max(0, (new_h - target_h) // 2)
        right = left + target_w
        bottom = top + target_h
        return resized.crop((left, top, right, bottom))

    raise ValueError(f"Unsupported object_fit: {object_fit}")
