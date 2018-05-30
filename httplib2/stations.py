from httplib2.route_search import *
# from main_fold.return_class.returning import Return


class StationArray(object):
    HEAD = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64;'
                          ' rv:59.0) Gecko/20100101 Firefox/59.0'}

    def __init__(self):
        self._arr = list()

    def add(self, station):
        """
        :param station:
        :return: appends informaition to the list
        """
        self._arr.append(station)

    def array(self):
        """
        :return: Basic data structure
        """
        return self._arr

    def __delete__(self, index=-1):
        """
        :param index: index of the element
        """
        del self._arr[index]

    def __getitem__(self, index):
        return self._arr[index]

    def __str__(self):
        return str(self._arr)

    @staticmethod
    def get_station_num(params, headers):
        """
        :param params: params for API,
        consists of name of the place
        :param headers: params of brouser
        :return: station number, or personal identifier
        """
        r = requests.post("https://booking.uz.gov.ua/train_search/station/",
                          params=params, headers=headers)
        response = json.loads(r.text)
        return response[0]['value']

    def get_stations(self, st_list):
        """
        :param st_list: list of stations names
        :return: appends Station class instance
         to initialized list
        """
        for city in st_list:
            param = {"term": city}
            num = self.get_station_num(param, self.HEAD)
            self.add(Station(city, num))

    def get_to_another_city(self, st1, st2, time, result):
        """
        :param st1: departure station
        :param st2: arrival station
        :param time: Curtime() instance,
        represents departure time
        :param result: Result() instance
        :return:
        """
        date = time.format_date()
        time = time.format_time()
        self.get_stations([st1, st2])
        response = make_response(self.array()[0].station_number(),
                                 self.array()[1].station_number(), date, time)
        route_info, new_date = make_route(response)
        result.add(route_info)
        return st2, new_date, result

    def region_across(self, curtime, result):
        """
        Creates the route across the region centers
        :param curtime: CurTime() instance
        :param result: Result() instance
        :return: new CurTime() instance,
         updated Result() instance
        """
        date = curtime.format_date()
        time = curtime.format_time()
        for attribute in range(len(self.array())):
            try:
                depart = self.array()[attribute].station_number()
                arrive = self.array()[attribute + 1].station_number()
                response = make_response(depart, arrive, date, time)
                route_info, new_date = make_route(response)
                result.add(route_info)
                date = new_date.format_date()
                time = new_date.format_time()
            except IndexError:
                depart = self.array()[-1].station_number()
                arrive = self.array()[0].station_number()
                response = make_response(depart, arrive, date, time)
                route_info, new_date = make_route(response)
                result.add(route_info)
                return new_date, result


class Station(object):
    """
    Class for station number representation
    """
    def __init__(self, name, number):
        self.st_name = name
        self.st_num = number

    def station_name(self):
        """
        :return: name of the station
        """
        return self.st_name

    def station_number(self):
        """
        :return: number of the station
        """
        return self.st_num

    def __repr__(self):
        return "{}: {}".format(self.st_name, self.st_num)
