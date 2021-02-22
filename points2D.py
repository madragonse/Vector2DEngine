from point2D import Point2D 

class Points2D:

    def __init__(self, points):
        self._points = []
        for point in points:
            self._points.append(Point2D(point))
        
    
    def move(self, v):
        for i in range(0, self._points.__len__()):
            self._points[i].move(v)

    
