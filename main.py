
import cv2
import mediapipe as mp
import time
from pathlib import Path

model = Path(__file__).with_name("gesture_recognizer.task")

if not model.exists():
    raise FileNotFoundError(
        "Download gesture_recognizer.task and put it beside main.py"
    )

vision = mp.tasks.vision

options = vision.GestureRecognizerOptions(
    base_options=mp.tasks.BaseOptions(
        model_asset_path=str(model)
    ),
    running_mode=vision.RunningMode.VIDEO,
    num_hands=1
)

labels = {
    "Open_Palm": "Open Hand",
    "Closed_Fist": "Fist",
    "Thumb_Up": "Thumbs Up",
    "Victory": "Victory / Peace"
}

camera = cv2.VideoCapture(0)
start = time.monotonic()

if not camera.isOpened():
    raise RuntimeError("Cannot open webcam. Close other camera apps.")

try:
    with vision.GestureRecognizer.create_from_options(options) as detector:
        while True:
            ok, frame = camera.read()
            if not ok:
                break

            frame = cv2.flip(frame, 1)
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            image = mp.Image(
                image_format=mp.ImageFormat.SRGB,
                data=rgb
            )

            timestamp = int((time.monotonic() - start) * 1000)
            result = detector.recognize_for_video(image, timestamp)

            gesture = "No Hand Detected"

            if result.gestures and result.gestures[0]:
                name = result.gestures[0][0].category_name
                gesture = labels.get(name, name)

            cv2.putText(
                frame, "Gesture: " + gesture, (20, 45),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2
            )

            cv2.imshow("AI Hand Gesture Recognition", frame)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
finally:
    camera.release()
    cv2.destroyAllWindows()
