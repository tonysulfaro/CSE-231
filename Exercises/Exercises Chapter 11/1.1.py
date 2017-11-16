class Student(object):

    def __init__(self, score = 10):
        self.__score = score

    def add_score(self):
        self.__score += 10

    def decrease_score(self):
        self.__score -= 10

    def __str__(self):
        return str(self.__score)