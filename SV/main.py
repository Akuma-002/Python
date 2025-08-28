import cv2
from camera_handler import CameraHandler
from gesture_recognition import GestureRecognition
from speech_output import SpeechOutput

def main():
    cam = CameraHandler()
    gesture_model = GestureRecognition()
    speaker = SpeechOutput()

    print("[INFO] Starting Silent Voice system... Press 'q' to quit.")

    while True:
        ok, frame = cam.read()
        if not ok:
            print("[ERROR] Frame not captured")
            break

        # TODO: extract real landmarks (e.g., Mediapipe hand tracking)
        landmarks = [0.1, 0.5, 0.9]  # dummy features
        gesture = gesture_model.classify(landmarks)

        cv2.putText(frame, f"Gesture: {gesture}", (50, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        cv2.imshow("Silent Voice", frame)

        if gesture:
            speaker.speak(gesture)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cam.release()
    print("[INFO] System stopped.")

if __name__ == "__main__":
    main()
