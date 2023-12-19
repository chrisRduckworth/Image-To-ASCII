import cv2 as cv
import numpy as np

def load_image(img_name, edge_detection, max_val, min_val, threshold):
    """loads the image, runs edge detection"""
    img = cv.imread(img_name, cv.IMREAD_GRAYSCALE)
    if edge_detection:
        img = cv.Canny(img, max_val, min_val)
    img = cv.threshold(img, threshold, 255, cv.THRESH_BINARY)[1]
    img = np.array(img, np.bool_)
    return img

def trim_whitespace(img):
    """removes empty rows/columns"""
    non_zero_indices = np.nonzero(img)
    min_y = min(non_zero_indices[0])
    max_y = max(non_zero_indices[0])
    min_x = min(non_zero_indices[1])
    max_x = max(non_zero_indices[1])

    img = img[min_y: max_y + 1, min_x: max_x + 1]
    return img

def pad_height(img, char_height):
    if img.shape[0] % char_height == 0:
        return img
    height_to_add = char_height - (img.shape[0] % char_height)
    img = np.concatenate((img, np.zeros((height_to_add, img.shape[1]), np.bool_)))
    return img
