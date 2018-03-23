import cv2
import camThread

class parkingSpot():

    def __init__(self, x1, y1, x2, y2, spotNum):
        self.x1 = int(x1)
        self.y1 = int(y1)
        self.x2 = int(x2)
        self.y2 = int(y2)
        self.spotNum = int(spotNum)
        self.width, self.height = 40, 40
        self.spotStatus = False

    def changeStatus(self):
        if self.spotStatus == True:
            self.spotStatus = False
        else:
            self.spotStatus = True

    def cropImage(self,frame):
        fileName = "spot" + str(self.spotNum) + ".jpg"
        roi = frame[self.y1:self.y2, self.x1:self.x2]
        cv2.imwrite(fileName, roi)
        return roi
