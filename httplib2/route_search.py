import requests
import json
from httplib2.time_data import CurTime
from httplib2.returning import RouteInfo


def search_routes(station1_num, station2_num, date, time):
    """
    :param station1_num: number of departure station
    :param station2_num: number of arrival station
    :param date: formatted departure date
    :param time: formatted departure time
    :return: dict of API response
    """
    head = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64;'
                          ' rv:59.0) Gecko/20100101 Firefox/59.0'}
    data = {"from": str(station1_num), "to": str(station2_num),
            "date": date, "time": time}
    r = requests.post("https://booking.uz.gov.ua/train_search/",
                      data=data, headers=head)
    response = json.loads(r.text)
    return response


def make_response(depart, arrive, date, time):
    """
    :param depart: departure station num
    :param arrive: arrival station num
    :param date: formatted departure date
    :param time: formatted departure time
    :return:
    """
    response = search_routes(depart, arrive, date, time)

    while response['data'] == 'Введена невірна дата' or \
            not response['data']['list']:
        times = CurTime()
        times = times.make_new_date(date, '09:00')
        max_day = 30
        max_month = 12
        if times.month == 1 or times.month == 3 or times.month == 5 or \
                times.month == 7 or times.month == 8 or times.month == 10 or \
                times.month == 12:
            max_day = 31
        elif times.month == 4 or times.month == 6 or times.month == 9 or \
                times.month == 11:
            max_day = 30
        elif times.month == 2:
            max_day = 28
        if times.day < max_day:
            times.day = times.day + 1
        else:
            times.day = 1
            if times.month < max_month:
                times.month = times.month + 1
            else:
                times.month = 1
                times.year = times.year + 1
        date = times.format_date()
        time = times.format_time()
        response = search_routes(depart, arrive, date, time)
    return response


def make_route(data):
    """
    :param data: dict of API response
    :return: RouteInfo() instance,
    CurTime() instance arrival
    """
    departure = CurTime()
    date_dep = data['data']['list'][0]['from']['srcDate']
    time_dep = data['data']['list'][0]['from']['time']
    departure = departure.make_new_date(date_dep, time_dep)
    wr_format_date = data['data']['list'][0]['to']['date']
    time_arr = data['data']['list'][0]['to']['time']
    arr_day = departure.get_day(wr_format_date)
    if departure.is_smaller(arr_day):
        arr_day = departure.day + 1
        arrival = CurTime(year=departure.year, month=departure.month,
                          day=arr_day,
                          hour=departure.reformat_time(time_arr)[0],
                          minute=departure.reformat_time(time_arr)[1])
    else:
        arrival = CurTime(year=departure.year, month=departure.month,
                          day=departure.day,
                          hour=departure.reformat_time(time_arr)[0],
                          minute=departure.reformat_time(time_arr)[1])

    information = RouteInfo()
    information.get_train_route(data)
    information.add({'Departure date': departure.format_date()})
    information.add({'Departure time': departure.format_time()})
    information.add({'Arrival date': arrival.format_date()})
    information.add({'Arrival time': arrival.format_time()})
    print(information)
    return information, arrival
