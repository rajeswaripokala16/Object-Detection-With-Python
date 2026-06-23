# Object Detection with Python

## Overview

Object Detection is a computer vision application used to identify and locate objects in images and videos. This project uses OpenCV and a pretrained SSD MobileNet model to perform real-time object detection.

---

## Problem Statement

Manual monitoring of visual data is time-consuming and error-prone. This project automates object detection and recognition using deep learning techniques.

---

## Tools Used

- Python
- OpenCV
- TensorFlow
- NumPy
- SSD MobileNet V3

---

## Dataset

COCO (Common Objects in Context)

Source:
https://cocodataset.org/

Number of Images:
330,000+

Classes:
80

---

## Modules

### Input Module

Captures video from webcam.

### Preprocessing Module

Resizes and prepares image for the model.

### Object Detection Module

Uses SSD MobileNet to classify objects.

### Output Module

Draws bounding boxes and labels.

---

## Working

1. Capture frame.
2. Convert image for model.
3. Detect objects.
4. Calculate confidence scores.
5. Draw bounding boxes.
6. Display output.

---

## Algorithm

1. Import libraries.
2. Load pretrained model.
3. Capture video frame.
4. Detect objects.
5. Draw rectangles and labels.
6. Display output.
7. Repeat until user exits.

---

## Expected Output

The system detects objects in real time and displays their names and confidence scores.

Applications include:

- Surveillance Systems
- Smart Security
- Autonomous Vehicles
- Robotics
- Traffic Monitoring

---

## Future Enhancements

- YOLOv8 integration
- Object Tracking
- Face Recognition
- Mobile Deployment
