# Image Processing Basics with OpenCV

A small hands-on image processing project built around the concepts covered in the VITyarthi OpenCV session.

The project takes an input image and demonstrates the basic operations we covered in class:

- reading an image with OpenCV
- displaying/saving processed images
- converting BGR images to grayscale
- splitting the blue, green and red channels
- applying blur filters
- generating a simple result summary

I kept the project intentionally simple so that the code is easy to follow and each operation can be traced back to one OpenCV concept.

## Project structure

```text
vityarthi_opencv_project/
|
|-- assets/
|   `-- sample_image.jpg
|
|-- docs/
|   |-- architecture.png
|   |-- component_diagram.png
|   |-- sequence_diagram.png
|   |-- use_case_diagram.png
|   `-- workflow.png
|
|-- notebooks/
|   `-- image_processing_demo.ipynb
|
|-- outputs/
|   `-- .gitkeep
|
|-- report/
|   `-- VITyarthi_Project_Report.pdf
|
|-- src/
|   |-- __init__.py
|   |-- basic_ops.py
|   |-- channels.py
|   |-- cli.py
|   |-- filters.py
|   |-- io_utils.py
|   |-- pipeline.py
|   `-- summary.py
|
|-- tests/
|   `-- test_processing.py
|
|-- .gitignore
|-- LICENSE
|-- README.md
|-- requirements.txt
|-- run.py
`-- statement.md
```

## Main features

### 1. Image input/output
Loads an image from disk, checks whether it was read correctly, and saves all generated results into an output folder.

### 2. Grayscale conversion
Converts the original BGR image into a single-channel grayscale image.

### 3. BGR channel separation
Splits the image into Blue, Green and Red channels. It also creates visual channel images where only one colour channel is kept at a time.

### 4. Image blurring
Applies:
- average blur
- Gaussian blur

The blur kernel size can be changed from the command line.

### 5. Result summary
Creates a small text file containing image dimensions, channel count, file name and names of the generated output files.

## Technologies used

- Python 3
- OpenCV
- NumPy
- Matplotlib
- Jupyter Notebook
- Pytest

## Installation

Clone the repository and move inside the project folder.

```bash
git clone <your-repository-url>
cd vityarthi_opencv_project
```

Create a virtual environment (recommended):

```bash
python -m venv .venv
```

On Windows:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the project

The repository already contains a sample image.

```bash
python run.py --image assets/sample_image.jpg
```

To use your own image:

```bash
python run.py --image path/to/your/image.jpg
```

To change the blur kernel:

```bash
python run.py --image assets/sample_image.jpg --kernel 9
```

The kernel must be a positive odd number such as 3, 5, 7, 9, etc.

Generated files are written inside `outputs/`.

## Run the notebook

Start Jupyter:

```bash
jupyter notebook
```

Open:

```text
notebooks/image_processing_demo.ipynb
```

Run the cells from top to bottom.

## Testing

Run:

```bash
pytest -q
```

The tests check:

- grayscale output shape
- BGR channel separation
- blur output dimensions
- invalid blur kernel handling
- full processing pipeline output

## Example outputs

After running the project, the output folder contains files similar to:

```text
original.jpg
grayscale.jpg
blue_channel.jpg
green_channel.jpg
red_channel.jpg
average_blur.jpg
gaussian_blur.jpg
summary.txt
```

## Project workflow

```text
Input image
    |
    v
Read and validate
    |
    +--> Save original
    |
    +--> Convert to grayscale
    |
    +--> Split BGR channels
    |
    +--> Apply blur filters
    |
    v
Save outputs + write summary
```

The detailed diagrams are available in the `docs/` folder.

## Notes

OpenCV reads colour images in **BGR** order, not RGB. When an OpenCV image is shown with Matplotlib, it should normally be converted from BGR to RGB first.

For this project I used `matplotlib` inside the notebook because `cv2.imshow()` can be awkward in some Jupyter environments. The core processing is still done completely with OpenCV.

## Future improvements

A few extensions that can be added later:

- edge detection
- thresholding
- image resizing and rotation
- histogram plotting
- brightness/contrast controls
- a simple Streamlit or Tkinter interface

## License

This project is released under the MIT License.
