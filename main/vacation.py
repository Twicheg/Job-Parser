class Vacation:
    """Класс для создания вакансий, поддерживает сравнение ваканский по з/п"""
    def __init__(self, id, vacation_name, link, payment, experience, snippet):
        self.__id = id
        self.__vacation_name = vacation_name
        self.__link = link
        self.__payment = payment
        self.__experience = experience
        self.__snippet = snippet

    @property
    def id(self):
        return self.__id

    @property
    def payment(self):
        return self.__payment

    @property
    def snippet(self):
        return self.__snippet

    @property
    def vacation_name(self):
        return self.__vacation_name

    def __le__(self, other):
        return self.payment < other

    def __eq__(self, other):
        return self.payment == other

    def __gt__(self, other):
        return self.payment > other

    def __add__(self, other):
        return self.payment + other

    def __str__(self) -> str:
        return f'{self.__link}\n{self.id}\n{self.__vacation_name}\n{self.__snippet}\n{self.__experience}\n{self.payment}'
