import cv2
import numpy as np

y, y1, x, x1 = 10, 80, 10, 80
img = cv2.imread('pos1.bmp',cv2.IMREAD_COLOR)
roi = img[y:y1, x:x1]
cv2.imwrite("roi.png", roi)
