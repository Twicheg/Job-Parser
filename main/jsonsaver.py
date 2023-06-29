from abc import ABC, abstractmethod


class AbstractSaverMethod(ABC):
    @abstractmethod
    def add_vacancy(self, vacancy):
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy):
        pass


class JSONSaver(AbstractSaverMethod):
    def add_vacancy(self, vacancy):
        print(vacancy, file=open('result.json', 'a'))

    def delete_vacancy(self, vacancy):
        pass
