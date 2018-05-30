from httplib2.stations import StationArray


class LvivRegion(StationArray):
    """
    Class for Lviv railway region
    """
    HEAD = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64;'
                          ' rv:59.0) Gecko/20100101 Firefox/59.0'}
    BREAKPOINTS = ['Львів', 'Івано-Франківськ', 'Чернівці',
                   "Кам'янець-Подільський", 'Хмельницький',
                   'Тернопіль', 'Львів',
                   'Рівне', 'Луцьк', 'Львів',  'Ужгород']

    def __init__(self):
        super().__init__()
        self.name = 'Львів'

    def array(self):
        return self._arr


class SouthWestRegion(StationArray):
    """
    Class for Kyiv railway region representation
    """
    HEAD = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64;'
                          ' rv:59.0) Gecko/20100101 Firefox/59.0'}
    BREAKPOINTS = ['Київ', 'Біла Церква', 'Вінниця', 'Житомир', 'Коростень-Пз',
                   'Київ', 'Чернігів']

    def __init__(self):
        super().__init__()
        self.name = 'Київ'

    def array(self):
        return self._arr


class OdessaRegion(StationArray):
    """
    Class for Odessa railway region representation
    """
    HEAD = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64;'
                          ' rv:59.0) Gecko/20100101 Firefox/59.0'}
    BREAKPOINTS = ['Одеса', 'Миколаїв', 'Херсон', 'Миколаїв', 'Черкаси']

    def __init__(self):
        super().__init__()
        self.name = 'Одеса'

    def array(self):
        return self._arr


class DnieperRegion(StationArray):
    """
    Class for Dnieper railway region representation
    """

    HEAD = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64;'
                          ' rv:59.0) Gecko/20100101 Firefox/59.0'}
    BREAKPOINTS = ['Запоріжжя', 'Дніпро-Головний']

    def __init__(self):
        super().__init__()
        self.name = 'Запоріжжя'

    def array(self):
        return self._arr


class SouthRegion(StationArray):
    """
    Class for Kharkiv railway region
    """
    HEAD = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64;'
                          ' rv:59.0) Gecko/20100101 Firefox/59.0'}
    BREAKPOINTS = ['Харків', 'Суми', 'Конотоп', 'Київ', 'Полтава']

    def __init__(self):
        super().__init__()
        self.name = 'Харків'

    def array(self):
        return self._arr


class CrossRoute(StationArray):
    """
    Class for ukrainian raliway representation
    """
    HEAD = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64;'
                          ' rv:59.0) Gecko/20100101 Firefox/59.0'}
    BREAKPOINTS = ['Львів', 'Одеса', 'Запоріжжя', 'Харків', 'Київ']

    def __init__(self, startpos='Київ'):
        super().__init__()
        self.startpos = startpos

    def array(self):
        return self._arr

    def get_all_stations(self):
        """
        :return: sorted list of main cities
        """
        while self.BREAKPOINTS[0] != self.startpos:
            self.BREAKPOINTS.append(self.BREAKPOINTS[0])
            del self.BREAKPOINTS[0]
        self.get_stations(self.BREAKPOINTS)
        return self.array()
