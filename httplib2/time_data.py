import time


class CurTime(object):
    """
    A class for time representation
    """
    def __init__(self, year=time.localtime()[0], month=time.localtime()[1],
                 day=time.localtime()[2], hour=time.localtime()[3],
                 minute=time.localtime()[4]):
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute

    def reformat_date(self, formatted):
        """
        Unpacks string to usable form of day, year and month
        :param formatted: string
        :return: year, month, day
        """
        date = ['', '', '']
        for i in range(len(date)):
            try:
                while formatted[0] != '-':
                    date[i] = date[i] + formatted[0]
                    formatted = formatted[1:]
                else:
                    formatted = formatted[1:]
            except IndexError:
                break

        return int(date[0]), int(date[1]), int(date[2])


    def reformat_time(self, string):
        """
            Unpacks string to usable form of hour and minute
            :param string: string of hour and minute
            :return: hour, minute
        """
        hour, minute = '', ''
        while string[0] != ':':
            hour = hour + string[0]
            string = string[1:]
        else:
            string = string[1:]
            i = 0
            while i != 2:
                minute = minute + string[0]
                i += 1
        return int(hour), int(minute)

    def make_new_date(self, data, time):
        """
        :param data: year, month, day
        :param time: hour, minute
        :return: CurTime instance
        """
        year, month, day = self.reformat_date(data)
        hour, minute = self.reformat_time(time)
        return CurTime(year=year, month=month, day=day, hour=hour, minute=minute)

    def format_date(self):
        """
        :return: making API-frendly interface
        """
        month = str(self.month)
        day = str(self.day)
        if self.month < 10:
            month = '0' + str(self.month)
        if self.day < 10:
            day = '0' + str(self.day)

        return '{}-{}-{}'.format(self.year, month, day)

    def format_time(self):
        """

        :return: API-needed representation of time
        """
        hour = str(self.hour)
        minute = str(self.minute)
        if self.hour < 10:
            hour = '0' + str(self.hour)
        if self.minute < 10:
            minute = '0' + str(self.minute)

        return '{}:{}'.format(hour, minute)

    def get_day(self, string):
        """
        :param string: gets only day from formatted date
        :return:
        """
        while string[0] != ' ':
            string = string[1:]
        else:
            result = ''
            while string[0] != '.':
                result = result + string[0]
                string = string[1:]
        return int(result)

    def is_smaller(self, other):
        """
        :param other: day of month
        :return: True/False in case of
        bigger or smaller self day
        """
        if self.day < other:
            return True
        return False
