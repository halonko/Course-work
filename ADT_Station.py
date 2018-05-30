# from main_fold.return_class.returning import Return


class StationArray(object):
    """
    .. note::
    Helloo
    """
    HEAD = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64;'
                          ' rv:59.0) Gecko/20100101 Firefox/59.0'}
    def __init__(self):
        self._arr = list()

    def add(self, station):
        raise NotImplementedError

    def array(self):
        raise NotImplementedError

    def __delete__(self, index=-1):
        raise NotImplementedError

    def __getitem__(self, index):
        raise NotImplementedError

    def __str__(self):
        raise NotImplementedError

    @staticmethod
    def get_station_num(params, headers):
        raise NotImplementedError

    def get_stations(self, st_list):
        raise NotImplementedError

    def get_to_another_city(self, st1, st2, time, result):
        raise NotImplementedError

    def region_across(self, curtime, result):
        raise NotImplementedError


class Station(object):
    """
    Class for station number representation
    """
    def __init__(self, name, number):
        self.st_name = name
        self.st_num = number

    def station_name(self):
        raise NotImplementedError

    def station_number(self):
        raise NotImplementedError

    def __repr__(self):
        raise NotImplementedError
