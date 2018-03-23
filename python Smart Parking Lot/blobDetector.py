import numpy as np
import cv2

def countPixels(img):
    thresh = cv2.threshold(img, 25, 255, cv2.THRESH_BINARY)[1]
    count_white =cv2.countNonZero(thresh);
    print(count_white)
    if count_white >= 500:
        return True
    else:
        return False
