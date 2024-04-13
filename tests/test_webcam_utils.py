from src.webcam_utils import calculate_laser_pov, calculate_arrow_direction, calculate_rectangle_center
import numpy as np

def test_calculate_laser_pov():
    frame = np.zeros((480, 640, 3), dtype=np.uint8)
    top_left, bottom_right = calculate_laser_pov(frame)
    assert top_left == (260, 180) and bottom_right == (380, 300)

def test_calculate_rectangle_center():
    top_left = (100, 100)
    bottom_right = (300, 300)
    expected_center = (200, 200)

    assert calculate_rectangle_center(top_left, bottom_right) == expected_center

def test_calculate_arrow_direction():
    center_rect = ((200, 200), (300, 300))  # Laser POV rectangle
    face_rect = ((400, 400), (500, 500))  # Face rectangle
    start_point, end_point = calculate_arrow_direction(center_rect, face_rect, length=50)

    expected_start = (250, 250)
    expected_end = (285, 285)

    assert start_point == expected_start
    assert end_point == expected_end
