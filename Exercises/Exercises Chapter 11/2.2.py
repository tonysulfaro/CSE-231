class RockGuitars(object):

    def __init__(self, guitarist = "", guitar = ""):
        self.__guitarist = guitarist
        self.__guitar = guitar

    def __str__(self):
        out_str = "{:<20s} {:<20s}".format(self.__guitarist, self.__guitar)
        return out_str

    def add_entry(self, guitarist, guitar):
        self.__guitarist = guitarist
        self.__guitar = guitar