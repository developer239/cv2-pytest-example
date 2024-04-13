import cv2
import numpy as np

def calculate_center_rectangle(frame):
    h, w, _ = frame.shape
    center_x, center_y = w // 2, h // 2
    size = min(h, w) // 4
    top_left = (center_x - size // 2, center_y - size // 2)
    bottom_right = (center_x + size // 2, center_y + size // 2)
    return top_left, bottom_right

def draw_rectangle(frame, top_left, bottom_right, color=(0, 255, 0), thickness=2):
    cv2.rectangle(frame, top_left, bottom_right, color, thickness)

def detect_faces(frame, face_cascade):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
    return faces

def draw_direction_arrow(frame, center_rect, face_rect):
    center_of_center_rect = (center_rect[0][0] + (center_rect[1][0] - center_rect[0][0]) // 2,
                             center_rect[0][1] + (center_rect[1][1] - center_rect[0][1]) // 2)
    center_of_face_rect = (face_rect[0][0] + (face_rect[1][0] - face_rect[0][0]) // 2,
                           face_rect[0][1] + (face_rect[1][1] - face_rect[0][1]) // 2)
    cv2.arrowedLine(frame, center_of_center_rect, center_of_face_rect, (255, 0, 0), 2)
