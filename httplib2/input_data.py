def get_input():
    """
    Gets the user input
    :return: start city name, list of needed regions
    """
    print('Greatings to traveller!')
    print('Enter your city: (Львів, Київ, Харків, Одеса, Запоріжжя)')
    print('                 (Lviv, Kyiv, Kharkiv, Odessa, Zaporizzia)')
    start = str(input())
    start = check_input(start)[0]
    print('Journey starts from {}'.format(start))
    print('\n\nDo you wish to visit any region deeply?'
          '\n\n if it`s Lviv, you will visit:'
          ' Івано-Франківськ, Чернівці, Тернопіль,'
          'Рівне, Луцьк, Ужгород'
          '\n\n if it`s Kyiv, you will visit:'
          'Житомир, Чернігів, Хмельницький,'
          'Вінниця, Козятин, Коростень'
          '\n\n if it`s Odessa, you will visit:'
          'Миколаїв , Херсон, Кропивницький,'
          'Черкаси, Умань, Ізмаїл'
          '\n\n if it`s Kharkiv, you will visit:'
          'Полтава, Суми'
          '\n\n if it`s Запоріжжя, you will visit: Дніпро')
    print('\n\n Choose one or more and press ENTER')
    deep_journey_regions = []
    verbose = '   '
    while verbose != '':
        verbose = str(input())
        check = check_input(verbose)
        if check[1]:
            deep_journey_regions.append(check[0])
            print(check[0])
        else:
            continue
    return start, deep_journey_regions


def check_input(start):
    """
    checks whether user made any mistakes
    :param start: inputed string
    :return: start sity name, additional verbose
    """

    if (start == 'Kyiv') or (start == 'k') or (start == 'Київ') \
            or (start == 'Ky') or (start == 'kyiv') or (start == 'KYIV'):
        verb = True
        start = 'Київ'
    elif (start == 'Lviv') or (start == 'l') or (start == 'Львів') \
            or (start == 'Lv') or (start == 'lviv') \
            or (start == 'LVIV '):
        verb = True
        start = 'Львів'
    elif (start == 'Kharkiv') or (start == 'Харків') or (start == 'Kh') \
            or (start == 'kharkiv') or (start == 'kh'):
        verb = True
        start = 'Харків'
    elif (start == 'Odessa') or (start == 'Одеса') or (start == 'o') \
            or (start == 'odessa') or (start == 'Od') \
            or (start == 'ODESSA'):
        verb = True
        start = 'Одеса'
    elif (start == 'Запоріжжя') or (start == 'Zaporizzia') or (start == 'z') \
            or (start == 'zaporizzia') or (start == 'Za') \
            or (start == 'ZAPORIZZIA'):
        verb = True
        start = 'Запоріжжя'
    elif start == '':
        verb = False
        start = 'Київ'
    else:
        print('Your place is not in a list')
        verb = False
        start = 'Київ'
    return start, verb
