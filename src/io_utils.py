from pathlib import Path
import cv2


def load_image(image_path):
    """Read an image and raise a useful error if it cannot be loaded."""
    path = Path(image_path)

    if not path.exists():
        raise FileNotFoundError(f"Image not found: {path}")

    image = cv2.imread(str(path))
    if image is None:
        raise ValueError(f"OpenCV could not read this file as an image: {path}")

    return image


def ensure_output_dir(output_dir):
    """Create the output directory when it does not already exist."""
    path = Path(output_dir)
    path.mkdir(parents=True, exist_ok=True)
    return path


def save_image(image, output_path):
    """Save an image and check that OpenCV completed the write."""
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    ok = cv2.imwrite(str(output_path), image)
    if not ok:
        raise IOError(f"Could not save image to: {output_path}")

    return output_path
