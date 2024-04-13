import os
import cv2

from src.webcam_utils import (
    calculate_laser_pov,
    draw_rectangle,
    detect_faces,
    draw_arrow
)


def main():
    cap = cv2.VideoCapture(0)

    base_dir = os.path.dirname(os.path.abspath(__file__))
    cascade_path = os.path.join(base_dir, '..', 'assets', 'cascades', 'haarcascade_frontalface_default.xml')
    face_cascade = cv2.CascadeClassifier(cascade_path)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        center_rect = calculate_laser_pov(frame)
        draw_rectangle(frame, *center_rect)

        faces = detect_faces(frame, face_cascade)
        first_face = faces[0] if len(faces) > 0 else None

        if (first_face is not None):
            face_rect = ((first_face[0], first_face[1]), (first_face[0] + first_face[2], first_face[1] + first_face[3]))
            draw_rectangle(frame, *face_rect, color=(255, 0, 0))
            draw_arrow(frame, center_rect, face_rect)

        cv2.imshow('Webcam', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
