import threading
import time
import numpy as np
import cv2

exitFlag = 0

class camThread (threading.Thread):
   def __init__(self, waitTime, windowName, map, cam):
      threading.Thread.__init__(self)
      self.waitTime = waitTime
      self.windowName = windowName
      self.map = map
      self.currFrame = None
      self.cam = cam

   def run(self):
      print("Starting ")
      cap = cv2.VideoCapture(1)
      cap.set(3, 1920)
      cap.set(4, 1080)
      fgbg = cv2.createBackgroundSubtractorMOG2()

      #Reading the first frame
      (grabbed, frame) = cap.read()
      self.currFrame = frame
      while(cap.isOpened()):
          (grabbed, frame) = cap.read()
          fgmask = fgbg.apply(frame)
          fgmask = cv2.GaussianBlur(fgmask, (21, 21), 0)
          thresh = cv2.threshold(fgmask, 25, 255, cv2.THRESH_BINARY)[1]
          self.currFrame = thresh
          cv2.imwrite("frame.jpg", thresh)
          img = frame
          img = createGrid(img, self.map)
          cv2.namedWindow(self.windowName)
          cv2.moveWindow(self.windowName,0,0)
          cv2.imshow(self.windowName,img)
          key = cv2.waitKey(self.waitTime)

          if key == 27:
              break

      cap.release()
      cv2.destroyAllWindows()
      print("Exiting ")

def createGrid(img, map):

    i = 0
    while(i < len(map.lotMap)):
        spot = map.lotMap[i]
        if(spot.spotStatus == False):
            img = openSpot(img, spot)
        else:
            img = closedSpot(img, spot)
        i+=1

    return img

def openSpot(img, spot):
    font = cv2.FONT_HERSHEY_SIMPLEX
    x, y = int((spot.x1 + spot.x2)/2) , int((spot.y1 + spot.y2)/2)
    img = cv2.rectangle(img, (spot.x1, spot.y1), (spot.x2, spot.y2), (0,255,0), 2 )
    img = cv2.putText(img, str(spot.spotNum), (x,y), font, 0.8, (255, 255, 255), 2, cv2.LINE_AA)
    return img

def closedSpot(img, spot):
    font = cv2.FONT_HERSHEY_SIMPLEX
    x, y = int((spot.x1 + spot.x2)/2) , int((spot.y1 + spot.y2)/2)
    img = cv2.rectangle(img, (spot.x1, spot.y1), (spot.x2, spot.y2), (0,0,255), 2 )
    img = cv2.putText(img, str(spot.spotNum), (x,y), font, 0.8, (255, 255, 255), 2, cv2.LINE_AA)
    return img
