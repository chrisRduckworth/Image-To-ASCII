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

def trim_whitespace(img):
    """removes empty rows/columns"""
    while not any(img[0]):
        img = img[1:]
    while not any(img[-1]):
        img = img[:-1]
    while not any(r[0] for r in img):
        img = [r[1:] for r in img]
    while not any(r[-1] for r in img):
        img = [r[:-1] for r in img]
    return img

def pad_height(img, char_height):
    if img.shape[0] % char_height == 0:
        return img
    height_to_add = char_height - (img.shape[0] % char_height)
    img = np.concatenate((img, np.zeros((height_to_add, img.shape[1]), np.bool_)))
    return img
