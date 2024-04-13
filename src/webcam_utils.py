import cv2


def calculate_laser_pov(frame):
    h, w, _ = frame.shape
    center_x, center_y = w // 2, h // 2
    size = min(h, w) // 4
    top_left = (center_x - size // 2, center_y - size // 2)
    bottom_right = (center_x + size // 2, center_y + size // 2)

    return top_left, bottom_right


def calculate_rectangle_center(top_left, bottom_right):
    center_x = top_left[0] + (bottom_right[0] - top_left[0]) // 2
    center_y = top_left[1] + (bottom_right[1] - top_left[1]) // 2

    return (center_x, center_y)


def calculate_arrow_direction(center_rect, face_rect, length=50):
    # Calculate centers of rectangles
    center_of_center_rect = calculate_rectangle_center(*center_rect)
    center_of_face_rect = calculate_rectangle_center(*face_rect)

    # Calculate vector components and magnitude
    dx = center_of_face_rect[0] - center_of_center_rect[0]
    dy = center_of_face_rect[1] - center_of_center_rect[1]
    magnitude = (dx ** 2 + dy ** 2) ** 0.5

    # Normalize and scale the vector
    if magnitude == 0:  # To handle the case where centers are the same
        unit_dx, unit_dy = 0, 0
    else:
        unit_dx = dx / magnitude
        unit_dy = dy / magnitude

    # Calculate the end point of the arrow
    end_x = int(center_of_center_rect[0] + unit_dx * length)
    end_y = int(center_of_center_rect[1] + unit_dy * length)

    return center_of_center_rect, (end_x, end_y)


def detect_faces(frame, face_cascade):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
    return faces


def draw_rectangle(frame, top_left, bottom_right, color=(0, 255, 0), thickness=2):
    cv2.rectangle(frame, top_left, bottom_right, color, thickness)


def draw_arrow(frame, start_point, end_point, color=(255, 0, 0), thickness=2):
    arrow = calculate_arrow_direction(start_point, end_point)
    cv2.arrowedLine(frame, *arrow, color, thickness)
