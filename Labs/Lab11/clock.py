class Time(object):

    def __init__(self, hours=0, minutes=0, seconds=0):
        """
        construct a time using 3 integers
        :param hours:
        :param minutes:
        :param seconds:
        """

        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds

    def __repr__(self):
        """
        :return string as a formal representation of time:
        """

        out_str = "Class Time: {:02d}:{:02d}:{:02d}"\
            .format(self.__hours, self.__minutes, self.__seconds)

        return out_str

    def __str__(self):
        """
        :return string 00:00:00 as formal representation of time:
        """

        out_str = "{:02d}:{:02d}:{:02d}" \
            .format(self.__hours, self.__minutes, self.__seconds)

        return out_str

    def from_str(self, time_str):
        """ Convert a string 00:00:00 into a Time. """

        hours, minutes, seconds = [int(n) for n in time_str.split(':')]

        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds