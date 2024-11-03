# Face Recognition Based Attendance System

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [File Structure](#file-structure)

## Project Overview

The Face Recognition Attendance System is an application that utilizes computer vision and machine learning techniques to automate attendance tracking in educational or organizational settings. The system captures faces using a webcam, trains a model on the captured images, recognizes faces, and records attendance automatically.

## Features

- **Camera Check**: Verify the camera's functionality before capturing images.
- **Face Capture**: Capture and save images of individuals for training the model.
- **Model Training**: Train a facial recognition model using the captured images.
- **Attendance Recognition**: Recognize faces in real-time and mark attendance accordingly.
- **Email Notification**: Automatically send attendance records via email.

## Requirements

- Python 3.x
- OpenCV
- NumPy
- Pandas
- Scikit-learn
- Other dependencies (listed in requirements.txt)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/mhdshabeer/Facial_Recognition_Based_Attendance_System.git

2. Install the required packages:
   ```bash
   pip install -r requirements.txt

3. Run the main.py file

## File Structure:
```bash
Face-Recognition-Attendance-System/
│
├── Take_Photos.py          # Module for capturing images
├── Model_Train.py          # Module for training the model
├── Mark_Attendance.py       # Module for recognizing faces and marking attendance
├── Cam_Checker.py          # Module for checking camera functionality
├── SendToMail.py           # Module for sending email notifications
├── haarcascade_frontalface_default.xml  # Haar cascade classifier for face detection
├── StudentDetails/         # Directory for storing student details and images
│   └── StudentDetails.csv  # CSV file for storing student ID and names
├── TrainingImage/          # Directory for storing captured training images
└── requirements.txt        # List of required Python packages


