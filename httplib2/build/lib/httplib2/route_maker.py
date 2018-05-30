# This is main executive function
# Just press RUN
# Copyright Yaroslav Halonko, Ukrainian Catholic University


from main_fold.stations_data.regions import LvivRegion, SouthRegion, \
    SouthWestRegion, OdessaRegion, DnieperRegion, CrossRoute
from main_fold.input.input_data import get_input
from main_fold.return_class.returning import *
from main_fold.time_class.time_data import CurTime


def main_route(input_tuple, curtime, result, start='Київ'):
    """
    Mail recursive function, creates all routes
    :param input_tuple: gets a main city and list of regions
    that user wishes to visit
    :param curtime: time of arrival
    :param result: Result() class instance
    :param start:
    :return: Resulting list of all routes
    """

    place, deep = input_tuple
    currtime = curtime
    curr_region = check_region(place)
    stations = make_st_list(curr_region.name)
    nexts = make_st_list(stations.BREAKPOINTS[1])

    deep = check_route_deep(deep, stations)

    next_city = nexts.BREAKPOINTS[0]

    if not deep:
        if stations.array()[1].station_name() == start:
            stations.get_to_another_city(place, next_city, currtime, stations)
            return result
        next_city, new_date, result = \
            stations.get_to_another_city(place, next_city,
                                         currtime, stations)
        return main_route((next_city, deep), new_date, result, start)
    else:
        if curr_region.name == deep[0]:
            new_date, result = create_reg_route(curr_region.name, currtime,
                                                result)
            new_date.day = new_date.day + 1
            if stations.array()[1].st_name == start:
                stations.get_to_another_city(place, next_city, new_date,
                                             stations)
                return result
            else:
                next_city, new_date, result = \
                    stations.get_to_another_city(place, next_city,
                                                 new_date, stations)
                del deep[0]

            return main_route((next_city, deep), new_date, result, start)
        else:
            # Creating a route between two main cities
            next_city, new_date, result = \
                stations.get_to_another_city(place, next_city,
                                             currtime, stations)
            return main_route((next_city, deep), new_date, result, start)


def create_reg_route(region, times, result):
    """

    :param region: CurrRegion instance
    :param times: CurTime() instance
    :param result: Result()
    :return: new CurTime instance,
    updated Return() instance
    """
    reg = check_region(region)
    reg.get_stations(reg.BREAKPOINTS)
    return reg.region_across(times, result)


def make_st_list(start):
    """
    :param start: name of start region
    :return: returns CrossRoute instance
    with sorted list sequence
    """
    route = CrossRoute(start)
    route.get_all_stations()
    return route


def check_route_deep(deep, m_route):
    """
    :param deep: list of regions to be
     observed better
    :param m_route: Main route class
    :return: sorted list of regions
    user wants to go across
    """
    result = []
    for i in m_route.array():
        for j in deep:
            if i.station_name() == j:
                result.append(i.station_name())
            else:
                continue
    return result


def check_region(region_center):
    """
    :param region_center: name of city
    :return: Current region instance
    """
    if region_center == 'Львів':
        return LvivRegion()
    if region_center == 'Київ':
        return SouthWestRegion()
    if region_center == 'Харків':
        return SouthRegion()
    if region_center == 'Одеса':
        return OdessaRegion()
    if region_center == 'Запоріжжя':
        return DnieperRegion()


def main():
    """
    The main function to run the project
    :return: List of defaultdict objects,
    all routes together
    """
    result = Return()
    start = get_input()
    result = main_route(start, CurTime(), result, start[0])
    return result


main()
