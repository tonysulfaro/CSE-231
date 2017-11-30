class Example(object):

    def __init__(self, string=''):
        self.__string = string

    def __sub__(self, other):
        pass

    def __gt__(self, other):
        return len(self.__string) > len(other.__string)

    def __str__(self):
        pass