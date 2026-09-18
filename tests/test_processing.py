import cv2
import numpy as np
import pytest

from src.basic_ops import to_grayscale
from src.channels import split_bgr
from src.filters import average_blur, gaussian_blur
from src.pipeline import process_image


@pytest.fixture
def sample_array():
    image = np.zeros((30, 40, 3), dtype=np.uint8)
    image[:, :, 0] = 30
    image[:, :, 1] = 120
    image[:, :, 2] = 220
    return image


def test_grayscale_is_single_channel(sample_array):
    gray = to_grayscale(sample_array)
    assert gray.shape == (30, 40)


def test_split_bgr_returns_three_channels(sample_array):
    blue, green, red = split_bgr(sample_array)
    assert blue.shape == green.shape == red.shape == (30, 40)
    assert int(blue[0, 0]) == 30
    assert int(green[0, 0]) == 120
    assert int(red[0, 0]) == 220


def test_blur_keeps_same_shape(sample_array):
    assert average_blur(sample_array, 5).shape == sample_array.shape
    assert gaussian_blur(sample_array, 5).shape == sample_array.shape


def test_even_kernel_is_rejected(sample_array):
    with pytest.raises(ValueError):
        gaussian_blur(sample_array, 4)


def test_full_pipeline(tmp_path, sample_array):
    input_path = tmp_path / "input.jpg"
    assert cv2.imwrite(str(input_path), sample_array)

    result = process_image(input_path, tmp_path / "out", kernel_size=5)

    expected = {
        "original",
        "grayscale",
        "average_blur",
        "gaussian_blur",
        "blue_channel",
        "green_channel",
        "red_channel",
    }

    assert expected.issubset(result["files"].keys())

    for file_path in result["files"].values():
        assert file_path.exists()

    assert result["summary"].exists()
