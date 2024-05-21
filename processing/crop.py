import cv2
import skimage as ski
from matplotlib import  pyplot as plt
import os

def image_crop(image, x_start, x_end, y_start, y_end):
    crop_image = image[y_start:y_end, x_start:x_end]
    return crop_image