from abc import ABC, abstractmethod
import requests, json


class AbstractAPIClass(ABC):
    @abstractmethod
    def get_vacancies(self):
        pass


class HeadHunterAPI(AbstractAPIClass):
    """Класс для работы с АПИ hh.ru
    """
    URL = 'https://api.hh.ru/vacancies'

    def __init__(self):
        self.__text = 'Python'
        self.params = {'text': self.__text,
                       'per_page': 100}
        self.header = {'User-Agent': 'User'}
        self.vacations_list = []
        self.response = requests.get(HeadHunterAPI.URL)
        if not self.response.ok:
            raise Exception('HeadHunterAPI problem')

    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, new: str):
        self.__text = new

    def get_vacancies(self):
        """метод get_vacancies возвращает список ваканский
    для поиска слова в полях ваканскии на сайте используется параметр self.text = 'str' """

        self.vacations_list = requests.get(HeadHunterAPI.URL, params=self.params, headers=self.header)
        return self.vacations_list.json()['items']


class SuperJobAPI(AbstractAPIClass):
    """Класс для работы с АПИ hh.ru"""
    URL = 'https://api.superjob.ru/2.0/vacancies/'
    SECRET_KEY = 'v3.r.137642841.625c6dcb2760626b8bbac4004dafbc05551c2bdc.3b08808d21406c4c61cabbd8d11e7032f2d502b7'

    def __init__(self):
        self.__keyword = 'Python'
        self.params = {
            'keyword': self.__keyword,
        }
        self.header = {"X-Api-App-Id": SuperJobAPI.SECRET_KEY}
        self.vacations_list = []
        self.response = requests.get(SuperJobAPI.URL, headers=self.header)
        if not self.response.ok:
            raise Exception('SuperJobAPI problem')

    @property
    def keyword(self):
        return self.__keyword

    @keyword.setter
    def keyword(self, new: str):
        self.__keyword = new

    def get_vacancies(self):
        """метод get_vacancies возвращает список ваканский
    для поиска слова в полях ваканскии на сайте используется параметр self.keyword= 'str'  """

        self.vacations_list = requests.get(SuperJobAPI.URL, params=self.params, headers=self.header)
        return self.vacations_list.json()['objects']

