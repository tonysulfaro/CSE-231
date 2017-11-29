import math

class Vector(object):


    def __init__(self, x = 0.0, y = 0.0):
        self.__x = x
        self.__y = y

    #vector 1 is self, vector 2 is other
    def __add__(self, other):
        if type(object) == Vector:
            x = self.__x + other.__x
            y = self.__y + other.__y
            return Vector(x, y)

    def __sub__(self, other):
        if type(object) == Vector:
            x = self.__x - other.__x
            y = self.__y - other.__y
            return(x, y)

    def __mul__(self, other):
        if type(object) == Vector:
            x = self.__x * other.__x
            y = self.__y * other.__y
            return x+y

        #this just updates the value of self. doesnt return
        elif type(object) == float or type(object) == int:
            x = self.__x * other
            y = self.__y * other
            return Vector(x,y)

    def __rmul__(self, other):
        return self*other

    def __repr__(self):
        return str(self)


    def __str__(self):
        out_str = "{:6.2f}, {:6.2f}".format(self.__x, self.__y)
        return out_str

    def __eq__(self, other):
        return self.__x == other.__x and self.__y == other.__y

    def magnitude(self):
        magnitude = math.hypot(self.__x, self.__y)
        return magnitude

    def unit(self):
        mag = self.magnitude()
        if mag == 0:
            raise ValueError("Cannot convert zero vector into unit vector.")
        self.__x /= mag
        self.__y /= mag