import cv2
from src.webcam_utils import *

def main():
    cap = cv2.VideoCapture(0)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        center_rect = calculate_center_rectangle(frame)
        draw_rectangle(frame, *center_rect)

        faces = detect_faces(frame, face_cascade)
        for (x, y, w, h) in faces:
            face_rect = ((x, y), (x + w, y + h))
            draw_rectangle(frame, *face_rect, color=(255, 0, 0))
            draw_direction_arrow(frame, center_rect, face_rect)

        cv2.imshow('Webcam', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
