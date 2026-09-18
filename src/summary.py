from pathlib import Path


def image_info(image, source_name):
    """Return a compact dictionary describing the input image."""
    height, width = image.shape[:2]
    channels = 1 if len(image.shape) == 2 else image.shape[2]

    return {
        "source": str(source_name),
        "width": width,
        "height": height,
        "channels": channels,
        "dtype": str(image.dtype),
    }


def write_summary(info, generated_files, output_path):
    """Write a plain-text processing summary."""
    output_path = Path(output_path)

    lines = [
        "IMAGE PROCESSING SUMMARY",
        "========================",
        f"Source: {info['source']}",
        f"Dimensions: {info['width']} x {info['height']}",
        f"Channels: {info['channels']}",
        f"Data type: {info['dtype']}",
        "",
        "Generated files:",
    ]

    for file_name in generated_files:
        lines.append(f"- {file_name}")

    output_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return output_path
