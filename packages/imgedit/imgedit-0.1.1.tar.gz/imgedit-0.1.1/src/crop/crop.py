from PIL import Image


def crop_transparent_edges_file(
    p_in:  str,
    p_out: str | None = None,

    threshold: int | None = None
) -> bool:
    """
    Crops transparent edges from an image file.

    Args:
        p_in: Path to input image file
        p_out: Path to output image file (default: overwrite input)
        threshold: Threshold value for cropping (default: None)

    Returns:
        bool: True if successful, False otherwise
    """

    try:
        img_in = Image.open(p_in)
    except (IOError, OSError) as e:
        print(f"Error opening image file {p_in}: {e}")
        return False

    try:
        cropped = crop_transparent_edges_img(img_in, threshold)
    except ValueError as e:
        print(f"Error cropping image: {e}")
        return False

    try:
        cropped.save(p_out or p_in)
    except (IOError, OSError) as e:
        print(f"Error saving image file {p_out or p_in}: {e}")
        return False

    return True


def crop_transparent_edges_img(
    img_in: Image.Image,

    threshold: int | None = None
) -> Image.Image:
    """
    Crops transparent edges from an image file.

    Args:
        img_in: Input image
        threshold: Threshold value for cropping (default: None)

    Returns:
        Image.Image: Cropped image
    """
    # Implementation
    # Make cropping more aggressive by ignoring near-transparent pixels
    img = img_in

    # Convert paletted images to RGBA if needed
    if img.mode == 'P':
        try:
            img = img.convert('RGBA')
        except Exception:
            pass

    # Only crop when an alpha channel exists
    if img.mode not in ('RGBA', 'LA'):
        return img_in

    # Obtain alpha channel
    try:
        alpha = img.getchannel('A')
    except Exception:
        alpha = img.split()[-1]

    # Threshold alpha to remove near-transparent padding (adjustable)

    if threshold is None:
        threshold = int((img.width + img.height) / 2 * 0.01)

    mask = alpha.point(lambda a: 255 if a > threshold else 0)

    bbox = mask.getbbox()
    if bbox is None:
        raise ValueError('Image has no opaque content to crop.')

    return img.crop(bbox)
