class Example(object):

    def __init__(self, v1=0, v2=0):
        self.__v1 = v1
        self.__v2 = v2

    def __str__(self):
        out_string = 'Value 1:{:2.1f}, Value 2:{:2.1f}'.format(self.__v1, self.__v2)
        return out_string

    def __add__(self, other):
        x = self.__v1 + other.__v1
        y = self.__v2 + other.__v2
        return Example(x, y)