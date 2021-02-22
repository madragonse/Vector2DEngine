
class Point2D:
    
    def __init__(self, position):
        self.__position = []
        self.__position.extend(position)

    def move(self, v):
        self.__position[0] += v[0]
        self.__position[1] += v[1]

    def put(self, position):
        self.__position = []
        self.__position.extend(position)
    
    def __str__(self):
        return str(self.__position)

    def getPosition(self):
        ret = []
        ret.extend(self.__position)
        return ret

    def getX(self):
        return self.__position[0]

    def getY(self):
        return self.__position[1]