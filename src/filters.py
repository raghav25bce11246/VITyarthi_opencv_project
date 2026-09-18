import cv2


def _validate_kernel_size(kernel_size):
    if not isinstance(kernel_size, int):
        raise TypeError("Kernel size must be an integer.")

    if kernel_size <= 0 or kernel_size % 2 == 0:
        raise ValueError("Kernel size must be a positive odd number.")


def average_blur(image, kernel_size=5):
    """Apply a simple average blur."""
    _validate_kernel_size(kernel_size)
    return cv2.blur(image, (kernel_size, kernel_size))


def gaussian_blur(image, kernel_size=5):
    """Apply Gaussian blur."""
    _validate_kernel_size(kernel_size)
    return cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)
