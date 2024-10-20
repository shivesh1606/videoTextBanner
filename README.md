# Video Text Banner using OpenCV

This project adds text banners to a video using OpenCV. The text can be long, with different lines separated by a `;`. Each line will appear sequentially on different frames of the video, centered on the screen. The font size and color are customizable (currently set to black with a larger font size).

## Features
- Add text banners to videos, where different lines are separated by `;`.
- Text appears in the center of the video.
- Customize the font size and color.
- Each line of text changes after a certain number of frames.

## Prerequisites

1. Install [Python 3.x](https://www.python.org/downloads/).
2. Create a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

### `requirements.txt`

```txt
opencv-python==4.8.0.74
numpy<2
