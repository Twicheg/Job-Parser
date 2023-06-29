from abc import ABC, abstractmethod


class AbstractSaverMethod(ABC):
    @abstractmethod
    def add_vacancy(self, vacancy):
        pass

    @abstractmethod
    def get_vacancies_by_salary(self):
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy):
        pass


class JSONSaver(AbstractSaverMethod):
    def add_vacancy(self, vacancy):
        pass

    def get_vacancies_by_salary(self):
        pass

    def delete_vacancy(self, vacancy):
        pass
