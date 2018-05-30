import json
import requests

# Search of all cities that starts with "ль"
headers = {'User-Agent':  'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:59.0) Gecko/20100101 Firefox/59.0'}
params = {"term": "Тернопіль"}
r = requests.post("https://booking.uz.gov.ua/train_search/station/", params=params, headers=headers)
response = json.loads(r.text)

print(json.dumps(response, sort_keys=True, indent=4, ensure_ascii=False))

# # Search of all possible trains
# data = {"from": "2218500", "to": "2200001", "date": "2018-05-29", "time": "00:00"}
# r = requests.post("https://booking.uz.gov.ua/train_search/", data=data, headers=headers)
# response = json.loads(r.text)

print(json.dumps(response, indent=4, ensure_ascii=False))

# STATIONS = [('Львів', 2218000), ("Київ", 2200001),
#                 ("Івано-Франківськ", 2218200),
#                 ("Кропивницький", 2208410), ("Житомир", 2200400),
#                 ("Запоріжжя", 2210730), ("Луцьк", 2218060),
#                 ("Миколаїв", 2208536),("Одеса", 2208001), ("Полтава", 2207803),
#                 ("Рівне", 2218400), ("Суми", 2204450),
#                 ("Тернопіль", 2218300), ("Ужгород", 2218095),
#                 ("Харків", 2204001), ("Херсон", 2208530),
#                 ("Хмельницький", 2200300), ("Черкаси", 2208340),
#                 ("Чернівці", 2218500), ("Чернігів", 2200779)]

