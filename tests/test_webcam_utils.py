from src.webcam_utils import calculate_center_rectangle, detect_faces
import numpy as np

def test_calculate_center_rectangle():
    frame = np.zeros((480, 640, 3), dtype=np.uint8)
    top_left, bottom_right = calculate_center_rectangle(frame)
    assert top_left == (240, 160) and bottom_right == (400, 320)

# Additional tests can be written for `draw_direction_arrow` and `detect_faces`.
