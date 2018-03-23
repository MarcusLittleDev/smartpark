import numpy as np
import cv2
from parkingMap import parkingMap


map = parkingMap("map.txt")

cap = cv2.VideoCapture(0)
waitTime = 50

#Reading the first frame
(grabbed, frame) = cap.read()

while(cap.isOpened()):

    (grabbed, frame) = cap.read()

    cv2.namedWindow('Parking Lot')
# while True:
#     count = 0
#     img = cam.getImage()
#     while count < len(map.lotMap):
#         spot = map.lotMap[count]
#         spotImg = spot.cropImage(lotImg)
#         currImg = spot.cropImage(img)
#         status = bSub(spotImg, currImg)
#         if status != spot.spotStatus:
#             spot.changeStatus()
#         count += 1
#
    cv2.imshow('Parking Lot',frame)

    key = cv2.waitKey(waitTime)

    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
