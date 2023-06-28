from abc import ABC, abstractmethod
import requests, json


class AbstractClass(ABC):
    @abstractmethod
    def get_vacancies(self):
        pass


class HeadHunterAPI(AbstractClass):
    """Класс для работы с АПИ hh.ru
    метод get_vacancies возвращает список ваканский
    для поиска в полях ваканский на сайте используется параметр self.text = 'str' """
    URL = 'https://api.hh.ru/vacancies'

    def __init__(self):
        self.__text = ''
        self.params = {'text': self.__text}
        self.header = {'User-Agent': 'User'}
        self.response = requests.get(HeadHunterAPI.URL, params=self.params, headers=self.header)
        if not self.response.ok:
            raise Exception('HeadHunterAPI problem')

    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, new: str):
        self.__text = new

    def get_vacancies(self) -> list:
        return self.response.json()


class SuperJobAPI(AbstractClass):
    """Класс для работы с АПИ hh.ru
    метод get_vacancies возвращает список ваканскийя
    для поиска по всей какансии на сайте используется ключевое слово self.keyword = 'str' """
    URL = 'https://api.superjob.ru/2.0/vacancies/'
    SECRET_KEY = 'v3.r.137642841.625c6dcb2760626b8bbac4004dafbc05551c2bdc.3b08808d21406c4c61cabbd8d11e7032f2d502b7'

    def __init__(self):
        self.__keyword = ''
        self.params = {
            'text': self.__keyword,
        }

        self.header = {"X-Api-App-Id": SuperJobAPI.SECRET_KEY}
        self.response = requests.get(SuperJobAPI.URL, params=self.params, headers=self.header)
        if not self.response.ok:
            raise Exception('SuperJobAPI problem')

    @property
    def keyword(self):
        return self.__keyword

    @keyword.setter
    def keyword(self, new: str):
        self.__keyword = new

    def get_vacancies(self) -> list:
        return self.response.json()
