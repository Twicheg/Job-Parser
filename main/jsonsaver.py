from abc import ABC, abstractmethod
import json


class AbstractSaverMethod(ABC):
    @abstractmethod
    def add_vacancy(self, vacancy):
        pass

    @abstractmethod
    def get_vacancies_by_salary(self, salary):
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy):
        pass


class MixinSave:
    @staticmethod
    def save_to_file():
        """ Функция для сохранения в файл """
        with open(JSONSaver.PATH, 'w') as file:
            json.dump(JSONSaver.list_to_save, fp=file)


class JSONSaver(AbstractSaverMethod, MixinSave):
    """Класс для сохранения , печати и удаления экземпляров
    стандартный путь сохранения JSONSaver.PATH = 'result.json' """
    PATH = 'result.json'
    list_to_save = []
    parser_list1 = []
    parser_list2 = []
    instance_list = []

    def add_vacancy(self, vacancy):
        """ Функция для создания списка вакансий для сохранения в виде json словаря """
        JSONSaver.parser_list1.extend(JSONSaver.parser_list2)
        try:
            with open(JSONSaver.PATH, 'r') as file:
                if open(JSONSaver.PATH, 'r').read():
                    saved_vacation_list = json.loads(file.read())
                    for vacation in saved_vacation_list:
                        JSONSaver.list_to_save.append(vacation)
        except FileNotFoundError:
            raise FileNotFoundError("нет файла JSONSaver.PATH = 'result.json'")
        for instance in JSONSaver.parser_list1:
            if 'id' in instance.keys() and int(instance['id']) == int(vacancy.id):
                JSONSaver.list_to_save.append(instance)

    def get_vacancies_by_salary(self, salary):
        """ Функция для просмотра списка сохраненных вакансий """
        try:
            with open(JSONSaver.PATH, 'r') as file:
                saved_vacation_list = json.loads(file.read())
        except FileNotFoundError:
            raise FileNotFoundError("нет файла JSONSaver.PATH = 'result.json'")

        for vacation in saved_vacation_list:
            for instance in JSONSaver.instance_list:
                if vacation['id'] == instance.id and instance.payment > int(salary):
                    print('*' * 100)
                    print(instance, sep='\n')

    def delete_vacancy(self, vacancy_id):
        """ Функция для удаления ваканский из списка по id """
        try:
            with open(JSONSaver.PATH, 'r') as file:
                saved_vacation_list = json.loads(file.read())
        except FileNotFoundError:
            raise FileNotFoundError("нет файла JSONSaver.PATH = 'result.json'")
        for vacation in saved_vacation_list:
            if int(vacation['id']) == int(vacancy_id):
                del saved_vacation_list[saved_vacation_list.index(vacation)]
                print('Вакансия удалена')
                break
        else:
            print('Нет вакансии с таким id')
        with open(JSONSaver.PATH, 'w') as file:
            json.dump(saved_vacation_list, fp=file)
