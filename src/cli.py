import argparse

from .pipeline import process_image


def build_parser():
    parser = argparse.ArgumentParser(
        description="Run basic OpenCV image processing operations."
    )
    parser.add_argument(
        "--image",
        required=True,
        help="Path to the input image.",
    )
    parser.add_argument(
        "--output",
        default="outputs",
        help="Directory where processed images will be saved.",
    )
    parser.add_argument(
        "--kernel",
        type=int,
        default=5,
        help="Positive odd blur kernel size (default: 5).",
    )
    return parser


def main():
    args = build_parser().parse_args()

    try:
        result = process_image(
            image_path=args.image,
            output_dir=args.output,
            kernel_size=args.kernel,
        )
    except (FileNotFoundError, ValueError, TypeError, IOError) as exc:
        print(f"Error: {exc}")
        return 1

    info = result["image_info"]
    print("Processing complete.")
    print(f"Image: {info['source']}")
    print(f"Size: {info['width']} x {info['height']}")
    print(f"Saved results to: {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
