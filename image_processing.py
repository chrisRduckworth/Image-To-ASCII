import cv2 as cv
import numpy as np

def load_image(img_name, edge_detection, max_val, min_val):
    """loads the image, runs edge detection"""
    img = cv.imread(img_name, cv.IMREAD_GRAYSCALE)
    if edge_detection:
        img = cv.Canny(img, max_val, min_val)
    # we use INV because black being a 1 makes more sense to me
    img = cv.threshold(img, 127, 255, cv.THRESH_BINARY_INV)[1]
    img = np.array(img, np.bool_)
    return img
