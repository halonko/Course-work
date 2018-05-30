class Return(object):
    """
    Class for result representation
    """

    def __init__(self):
        self.resulting_list = []

    def add(self, route):
        """
        :param route: adding RouteInfo instance to the list
        :return:
        """
        self.resulting_list.append(route)

    def __repr__(self):
            return str(self.resulting_list)


class RouteInfo(object):
    """
    Class for information representation
    """
    def __init__(self):
        from collections import defaultdict
        self.dictionary = defaultdict()

    def get_train_route(self, data):
        """
        Adds info to the
        :param data: dict of API response
        :return: None
        """
        self.add({'num': data['data']['list'][0]['num']})
        self.add({'travelTime': data['data']['list'][0]['travelTime']})
        dep_station = data['data']['list'][0]['from']['station']
        arr_station = data['data']['list'][0]['to']['station']
        route = dep_station + ' to ' + arr_station
        self.add({'route': route})

    def add(self, data):
        self.dictionary.update(data)

    def information(self):
        return self.dictionary

    def __str__(self):
        return f'{self.dictionary}'
