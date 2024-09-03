import cv2
import numpy as np
from tesseract_reader.bbox.bbox import BBox


class ImageProcessor:
    def draw_bboxes(self, image: np.ndarray, bboxes: BBox):
        for bbox in bboxes:
            top_left = (bbox.x_top_left, bbox.y_top_left)
            bottom_right = (bbox.x_top_left + bbox.width, bbox.y_top_left + bbox.height)
            cv2.rectangle(image, top_left, bottom_right, (0, 255, 0), 2)
        return image
