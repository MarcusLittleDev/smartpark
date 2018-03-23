from parkingSpot import parkingSpot


class parkingMap():

    def __init__(self, coordinates):
        self.coordinates = self.readFile(coordinates)
        self.lotMap = self.createMap()


    def readFile(self, spots):

        array = []
        with open(spots) as f:
            read_data = f.read()
        for word in read_data.split():
            array.append(int(word))

        return array

    def createMap(self):
        count = 0
        spotNum = 1
        lotMap = []

        while(count < len(self.coordinates)):
            spot = parkingSpot(self.coordinates[count], self.coordinates[count + 1],self.coordinates[count + 2], self.coordinates[count + 3], str(spotNum))
            lotMap.append(spot)
            count += 4
            spotNum += 1

        return lotMap
