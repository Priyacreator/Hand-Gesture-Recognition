# AI Hand Gesture Recognition System 🖐️

## 📌 Project Overview

This project is a real-time AI-based hand gesture recognition system developed using Python, OpenCV, and MediaPipe. It uses a webcam to detect hand gestures and displays the recognized gesture on the video feed.

The system uses MediaPipe's pre-trained Gesture Recognizer model to identify common hand gestures.

## ✨ Features

- Real-time hand gesture recognition using a webcam.
- Detection of one hand at a time.
- Recognition of Open Hand, Fist, Thumbs Up, and Victory/Peace gestures.
- Live display of the recognized gesture.
- Mirrored webcam feed for a more natural user experience.
- Simple and lightweight Python implementation.

## 🛠️ Technologies Used

- **Python** – Core programming language.
- **OpenCV** – Webcam capture, image processing, and display.
- **MediaPipe** – Hand gesture recognition using a pre-trained model.
- **Pathlib** – Locating the model file.
- **Time** – Generating timestamps for video processing.

## 📂 Project Structure

```text
Hand-Gesture-Recognition/
├── main.py
├── gesture_recognizer.task
├── requirements.txt
├── README.md
├── .gitignore
└── screenshots/
```

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/Hand-Gesture-Recognition.git
```

### 2. Navigate to the Project Directory

```bash
cd Hand-Gesture-Recognition
```

### 3. Create a Virtual Environment (Recommended)

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### 5. Download the Gesture Recognition Model

Download the MediaPipe Gesture Recognizer model and save it as `gesture_recognizer.task` in the same directory as `main.py`.

Model download: https://storage.googleapis.com/mediapipe-models/gesture_recognizer/gesture_recognizer/float16/1/gesture_recognizer.task

### 6. Run the Application

```bash
python main.py
```

## 🖐️ Supported Gestures

| Gesture | Display Label |
|---|---|
| Open Palm | Open Hand |
| Closed Fist | Fist |
| Thumbs Up | Thumbs Up |
| Victory | Victory / Peace |

## 🎮 How to Use

1. Connect a webcam or use your computer's built-in camera.
2. Run `main.py`.
3. Show one hand in front of the webcam.
4. Perform one of the supported gestures.
5. View the recognized gesture on the screen.
6. Press **Q** to exit the application.

## 🔍 How It Works

1. OpenCV captures video frames from the webcam.
2. Each frame is flipped and converted from BGR to RGB.
3. MediaPipe processes the frame using its Gesture Recognizer model.
4. The predicted gesture category is mapped to a readable label.
5. OpenCV displays the video feed with the recognized gesture.

## 🚀 Future Improvements

- Add mouse cursor movement and click controls.
- Integrate scrolling and volume control.
- Recognize additional hand gestures.
- Improve usability under different lighting conditions.
- Add customizable gesture-to-action mappings.

## 👩‍💻 Author

**Priya Yadav**

## 📄 License

For educational and learning purposes. If you plan to distribute the project, consider adding an appropriate open-source license.

