import cv2


def to_grayscale(image):
    """Convert a BGR image to grayscale."""
    if image is None:
        raise ValueError("Image cannot be None.")

    if len(image.shape) == 2:
        return image.copy()

    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
