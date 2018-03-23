from camThread import camThread
from parkingMap import parkingMap
from time import sleep
from blobDetector import countPixels
import pymysql
import sys
from dataTable import *
from copy import copy


def setup(waitTime, frameName, mapFile):
    global map
    map = parkingMap(mapFile)
    global video
    host="iqparking.cj04po7n3mhl.us-west-2.rds.amazonaws.com"
    port=3306
    dbname="ParkingLot"
    user="IQParking"
    password="Cmps411_2"
    global conn
    conn = pymysql.connect(host, user=user, port=port, passwd=password, db=dbname, connect_timeout=5)
    video = camThread(waitTime, frameName, map, 0)
    video.start()
    sleep(5)

def initDatabase():
    count = 0
    createTable(conn)
    while count < len(map.lotMap):
        spot = map.lotMap[count]
        insertData(conn, spot.spotNum, spot.spotStatus)
        count += 1
    queryData(conn)



setup(50, 'Parking Lot', 'map.txt')
initDatabase()

while True:
    count = 0
    if video.isAlive() == False:
        break
    f = open('spots.txt', 'w')
    while count < len(map.lotMap):
        frame = 'frame.jpg'
        spot = map.lotMap[count]
        spot.spotStatus = countPixels(spot.cropImage(video.currFrame))
        if spot.spotStatus == True:
            f.write("Occupied ")
        else:
            f.write("Availabe ")
        updateData(conn, spot.spotNum, spot.spotStatus)
        count += 1
    f.close()
    copy()
    queryData(conn)

conn.close()
