class Line():

    def __init__(self, coor1, coor2):

        self.coor1 = coor1
        self.coor2 = coor2


    def distance(self):
        x1, x2 = self.coor1
        y1, y2 = self.coor2
        x = (x1 - y1) ** 2
        y = (x2 - y2) ** 2
        xy = (x + y) ** 1/2
        print(xy)

    def slope(self):
        x1, x2 = self.coor1
        y1, y2 = self.coor2
        y = x2 - y2
        x = x1 - y1
        yx = y/x
        print(yx)


myline = Line((4, 3), (9, 4.5))

myline.distance()
myline.slope()
