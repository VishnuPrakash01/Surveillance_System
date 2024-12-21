# DETECT, SEPARATE AND MATCH INDIVIDUAL FROM A SURVEILLANCE CAMERA USING FACE RECOGNITION MECHANISM

## Overview
This project leverages advanced face recognition mechanisms to detect, separate, and match individuals from surveillance camera footage. The core functionality is built using Python libraries such as `dlib`, `face_recognition`, and `OpenCV`, enabling real-time or batch processing of video feeds to identify and track individuals accurately.

## Features
- **Detection**: Identifies faces in surveillance footage.
- **Separation**: Isolates individual faces from frames for further analysis.
- **Matching**: Matches detected faces with a pre-existing database of known individuals.

## Prerequisites
Ensure you have Python installed on your system. The project is compatible with Python 3.x.

## Setup Instructions

### Step 1: Install Required Libraries
1. **Install the `dlib` library**
   ```bash
   pip install dlib
   ```
   The `dlib` library provides machine learning tools and algorithms essential for face recognition.

2. **Install the `face_recognition` library**
   ```bash
   pip install face_recognition
   ```

3. **Install the OpenCV library**
   ```bash
   pip install opencv-python
   ```

4. **Other Relevant Libraries**
   Import the following libraries in your Python scripts:
   ```python
   import cv2
   import numpy as np
   import face_recognition as faceRegLib
   ```

## How It Works
1. **Detection**: The `face_recognition` library, backed by `dlib`, identifies faces in video frames.
2. **Separation**: Each detected face is cropped or isolated using OpenCV.
3. **Matching**: Detected faces are compared with a pre-existing database using face encoding.

## Usage
- Configure the input video source (live camera feed or video file).
- Load the database of known individuals (if required for matching).
- Run the Python script to process the video and analyze results.

## Example Script
Here is an example to demonstrate basic face detection:

```python
import cv2
import face_recognition as faceRegLib

# Load a video file
video_capture = cv2.VideoCapture('input_video.mp4')

while video_capture.isOpened():
    ret, frame = video_capture.read()
    if not ret:
        break

    # Convert the frame to RGB (OpenCV uses BGR by default)
    rgb_frame = frame[:, :, ::-1]

    # Find all face locations in the frame
    face_locations = faceRegLib.face_locations(rgb_frame)

    # Draw rectangles around detected faces
    for top, right, bottom, left in face_locations:
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

    # Display the frame
    cv2.imshow('Video', frame)

    # Break loop with 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
```

## Notes
- Ensure your system has a capable GPU or sufficient CPU power for real-time face recognition.
- Always handle sensitive data securely when working with surveillance footage.

## Contributing
Contributions to improve functionality or add new features are welcome. Please create a pull request with detailed information about the changes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contact

For queries or support, please contact: [vishnu] vishnuprakashl0112@gmail.com

## Acknowledgments
- [dlib](http://dlib.net/)
- [face_recognition](https://github.com/ageitgey/face_recognition)
- [OpenCV](https://opencv.org/)
