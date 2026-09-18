from pathlib import Path

from .basic_ops import to_grayscale
from .channels import channel_visuals
from .filters import average_blur, gaussian_blur
from .io_utils import ensure_output_dir, load_image, save_image
from .summary import image_info, write_summary


def process_image(image_path, output_dir="outputs", kernel_size=5):
    """Run all project operations on one image."""
    output_dir = ensure_output_dir(output_dir)
    image = load_image(image_path)

    generated = []

    outputs = {
        "original": image,
        "grayscale": to_grayscale(image),
        "average_blur": average_blur(image, kernel_size),
        "gaussian_blur": gaussian_blur(image, kernel_size),
    }

    for name, channel_image in channel_visuals(image).items():
        outputs[f"{name}_channel"] = channel_image

    saved_paths = {}
    for name, result in outputs.items():
        file_path = output_dir / f"{name}.jpg"
        save_image(result, file_path)
        saved_paths[name] = file_path
        generated.append(file_path.name)

    info = image_info(image, Path(image_path).name)
    summary_path = write_summary(
        info,
        generated,
        output_dir / "summary.txt",
    )

    return {
        "image_info": info,
        "files": saved_paths,
        "summary": summary_path,
    }
