import numpy as np
import cv2
import matplotlib.pyplot as plt
from PIL import Image, ImageFilter
import pdb


def main():
    image = cv2.imread('demo.png')
    blur = cv2.GaussianBlur(image, (5,5), 0)
    blur_hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)

    # create NumPy arrays from the boundaries
    lower = np.array([0,0,0], dtype = "uint8")
    upper = np.array([180,255,40], dtype = "uint8")

    # find the colors within the specified boundaries and apply
    mask = cv2.inRange(blur_hsv, lower, upper)  
    mask = 255 - mask
    output = cv2.bitwise_and(image, image, mask = mask)
    median = cv2.medianBlur(mask, 5)

    cv2.imwrite('demo_mask.png', median)


if __name__ == '__main__':
    main()