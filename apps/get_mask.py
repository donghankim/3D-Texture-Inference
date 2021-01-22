import numpy as np
import cv2
import pdb

def main(img_path):
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    img[np.where(img > 5)] = 255
    
    cv2.imwrite("../sample_images/mask.png", img)





if __name__ == '__main__':
    img_path = '../sample_images/mask_test.png'
    main(img_path)