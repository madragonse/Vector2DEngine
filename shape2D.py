from typing import List
from line2D import Line2D
from point2D import Point2D 
import math
import matrixOp

class Shape2D:

    def __init__(self, position):
        self.__lines = []
        self.__position:Point2D = Point2D(position)
        self.__rotation_matrix = [[1,1],[1,1]]
        self.__rotation_angle = 0
        self.__matrix_op = matrixOp.Matrix_op()


    def addLine(self, line:Line2D):
        self.__lines.append(line)
    

    def rotate(self, angle):
        self.__rotation_angle += angle
        if self.__rotation_angle > 360:
            self.__rotation_angle = self.__rotation_angle % 360
        if self.__rotation_angle < 0:
            self.__rotation_angle += 360
        rad = (self.__rotation_angle / 180) * math.pi
        sin_res = math.sin(rad)
        cos_res = math.cos(rad)
        self.__rotation_matrix = [[cos_res, sin_res], [-sin_res, cos_res]]

    def getLinesToDraw(self):
        ret = []
        
        for line in self.__lines:
            tem = line.getPoints()
            for i in range(0, tem.__len__()):
                tem[i] = self.__matrix_op.multiply_vector(self.__rotation_matrix, tem[i])
                tem[i][0] += self.__position.getX()
                tem[i][1] += self.__position.getY()
            ret.append(tem)
        return ret
    def move(self, v):
        self.__position.move(v)


    
