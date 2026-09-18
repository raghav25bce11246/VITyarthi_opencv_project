import cv2
import numpy as np


def split_bgr(image):
    """Return the blue, green and red single-channel arrays."""
    if image is None:
        raise ValueError("Image cannot be None.")

    if len(image.shape) != 3 or image.shape[2] != 3:
        raise ValueError("BGR channel splitting needs a 3-channel image.")

    return cv2.split(image)


def channel_visuals(image):
    """Create three colour images showing only B, G or R information."""
    blue, green, red = split_bgr(image)
    zeros = np.zeros_like(blue)

    blue_img = cv2.merge([blue, zeros, zeros])
    green_img = cv2.merge([zeros, green, zeros])
    red_img = cv2.merge([zeros, zeros, red])

    return {
        "blue": blue_img,
        "green": green_img,
        "red": red_img,
    }
