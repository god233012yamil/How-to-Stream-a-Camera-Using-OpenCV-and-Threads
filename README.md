# RTSP Camera Streaming with OpenCV and Threading

This project demonstrates how to stream an IP camera feed using the **RTSP** protocol with OpenCV and threading in Python. The solution handles real-time video streaming by using a separate thread to fetch video frames, ensuring smooth video processing continuously.

## Table of Contents
- [Introduction](#introduction)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Code Explanation](#code-explanation)
  - [RTSPCameraStream Class](#rtspcamerastream-class)
  - [Starting the Stream](#starting-the-stream)
  - [Reading Frames](#reading-frames)
  - [Main Function](#main-function)
- [License](#license)

## Introduction

Streaming a camera feed using OpenCV is an effective way to capture and process real-time video data. This project focuses on capturing an RTSP feed from an IP camera and displaying it using OpenCV. We use threading to keep the stream running in the background, allowing for further video processing without blocking the main thread.

## Requirements

- Python 3.x
- OpenCV (`opencv-python` package)
- An IP camera with RTSP support
- Basic knowledge of Python and threading

## Installation

1. Clone the repository:

    git clone https://github.com/yourusername/rtsp-camera-streaming-opencv.git

2. Install the required dependencies:

    pip install opencv-python

3. Ensure your IP camera supports RTSP and that you have the credentials to access it.

## Usage

1. Replace the default camera credentials and stream path in the `main()` function in the script:

    user = "your_user"
    password = "your_password"
    ip = "camera_ip"
    port = 554  # Default RTSP port
    stream_path = "camera video stream path"

2. Run the script:

    python stream_camera.py

3. Press **'q'** to stop the stream and close the window.

## Code Explanation

### RTSPCameraStream Class

This class is responsible for handling the RTSP connection and continuously fetching frames from the IP camera in a separate thread.

![image](https://github.com/user-attachments/assets/9d64fd18-cf4b-4b47-8c7c-6487feb42ed8)

### Starting the Stream

The start method initializes the streaming process in a separate thread, ensuring the camera stream does not block the main thread.

![image](https://github.com/user-attachments/assets/122268cf-342a-4680-bed9-ebfcf2db53f6)

The stream is started by calling the start method, which begins fetching frames in the background.

### Reading Frames

The read method allows you to retrieve the latest frame captured by the camera. This method can be used in your main loop to display the video stream or further process the frames.

![image](https://github.com/user-attachments/assets/4248070b-f5bc-4b3a-942d-d46377b9d551)

### Main Function

The main function demonstrates how to use the RTSPCameraStream class to stream the camera feed and display it in a window.

![image](https://github.com/user-attachments/assets/3e13e27b-78e8-4759-af42-8f82b6316837)

The video stream will be displayed in a window, and pressing the 'q' key will stop the stream and close the window.

### License

This project is licensed under the GNU GENERAL PUBLIC LICENSE License - see the LICENSE file for details.

You can just modify the content to suit your GitHub repository's structure, such as adjusting the installation section based on your package manager or dependencies.


