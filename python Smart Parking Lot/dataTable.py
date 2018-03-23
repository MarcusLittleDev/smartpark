import pymysql
import sys
import logging

host="iqparking.cj04po7n3mhl.us-west-2.rds.amazonaws.com"
port=3306
dbname="ParkingLot"
user="IQParking"
password="Cmps411_2"

# logger = logging.getLogger()
# logger.setLevel(logging.INFO)
#
# try:
#     conn = pymysql.connect(host, user=user, port=port, passwd=password, db=dbname, connect_timeout=5)
# except:
#     logger.error("ERROR: Unexpected error: Could not connect to MySql instance.")
#     sys.exit()
#
# logger.info("SUCCESS: Connection to RDS mysql instance succeeded")
#
# # prepare a cursor object using cursor() method
# cursor = conn.cursor()
#
#
# # execute SQL query using execute() method.
def createTable(conn):
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS PARKINGSPOTS")

    sql = """CREATE TABLE PARKINGSPOTS (
        SPOTID  INT NOT NULL,
        SPOTSTATUS  BOOL NOT NULL )"""

    cursor.execute(sql)

def insertData(conn, spotNum, spotStatus):
    cursor = conn.cursor()
    sql = "INSERT INTO PARKINGSPOTS (SPOTID, SPOTSTATUS) \
        VALUES ('%d', '%d')" % (spotNum, spotStatus)

    try:
        cursor.execute(sql)
        conn.commit()
    except:
        conn.rollback()

def updateData(conn, spotNum, spotStatus):
    cursor = conn.cursor()
    sql = "UPDATE PARKINGSPOTS SET SPOTSTATUS = '%d' \
                                WHERE SPOTID = '%d' \
                                " % (spotStatus, spotNum)
    try:
        cursor.execute(sql)
        conn.commit()
    except:
        conn.rollback()


def queryData(conn):
    f = open('spotStatus.txt', 'w')
    cursor = conn.cursor()
    sql = "SELECT * FROM PARKINGSPOTS"

    try:
        cursor.execute(sql)
        results = cursor.fetchall()

        for row in results:
            spotId = row[0]
            spotStatus= bool(row[1])
            print("spotId = %d, spotStatus = %s" % \
                (spotId, spotStatus))
            f.write("spotId = %d, spotStatus = %s" % \
                (spotId, spotStatus))
    except:
        print("Error: unable to fetch data")
    f.close()
