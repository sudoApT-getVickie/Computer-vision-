# Computer Vision Project

Python script that loads, manipulates, and displays image data using the OpenCV library.

Project Description
This project demonstrates fundamental image processing techniques through two primary tasks:

1. **Image I/O and GUI Window Management:** Reading the standard MountKenya file (`image.jpg`) from local storage into the program's memory. The script utilizes OpenCV's high-level GUI functions to render the image array in a display window. It also includes memory management commands to pause execution until user interaction occurs, followed by safely destroying the window to free up system resources.

2. **Color Space Transformation:**
   Implementing a basic color space conversion algorithm. The script takes the multi-channel BGR (Blue, Green, Red) image matrix and applies OpenCV's `cvtColor` function to mathematically flatten it into a single-channel grayscale matrix.
   

## Prerequisites
Before running this script, ensure you have Python installed along with the OpenCV library.

Install OpenCV via pip:
```bash
pip install opencv-python
