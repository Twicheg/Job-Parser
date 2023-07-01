from vacation import Vacation
from vacations_API import HeadHunterAPI, SuperJobAPI
from jsonsaver import JSONSaver


def create_vacations_list(chose_platform):
    """ Функция для создания списка экземпляров класса Vacation
    из данных API hh.ru и API superjob.ru"""
    vacations_list = []
    hh = HeadHunterAPI()
    sj = SuperJobAPI()
    salary = 0
    parser_1 = hh.get_vacancies()
    parser_2 = sj.get_vacancies()
    JSONSaver.parser_list1 = parser_1
    JSONSaver.parser_list2 = parser_2
    if chose_platform in [1, 3]:
        for dict_ in parser_1:
            if dict_['salary'] is not None:
                if 'from' in dict_['salary'].keys():
                    salary = dict_['salary']['from']
                elif 'to' in dict_['salary'].keys():
                    salary = dict_['salary']['to']
            else:
                salary = 0

            snippet = str(dict_['snippet']['responsibility']) + str(dict_['snippet']['requirement'])
            vacations_list.append(Vacation(
                dict_['id'],
                dict_['name'],
                dict_['apply_alternate_url'],
                salary,
                dict_['experience']['name'],
                snippet))

    if chose_platform in [2, 3]:
        for dict_ in parser_2:
            if dict_['payment_from'] != 0 and dict_['payment_to'] != 0:
                salary = max(int(dict_['payment_from']), int(dict_['payment_to']))
            elif dict_['payment_from'] != 0:
                salary = int(dict_['payment_from'])
            elif dict_['payment_to'] != 0:
                salary = int(dict_['payment_to'])
            else:
                salary = 0

            vacations_list.append(Vacation(
                dict_['id'],
                dict_['profession'],
                dict_['client']['link'],
                salary,
                dict_['experience']['title'],
                dict_['candidat']))
    JSONSaver.instance_list = vacations_list
    return vacations_list


def filter_vacancies(search_vacancy, filter_words, chose_platform):
    """ Фукция для фильтра списка экзеров ваканский по заданным требованиям"""
    filtered_list = []
    if type(filter_words).__name__ == list.__name__:
        for instance in create_vacations_list(chose_platform):
            if instance.snippet:
                true_list = []
                if search_vacancy.lower() in instance.vacation_name.lower():
                    for word in filter_words:
                        if word in instance.snippet.lower():
                            true_list.append(True)
                        else:
                            true_list.append(False)
                    if False not in true_list:
                        filtered_list.append(instance)

    elif type(filter_words).__name__ == str.__name__:
        for instance in create_vacations_list(chose_platform):
            if instance.snippet:
                if search_vacancy.lower() in instance.vacation_name.lower():
                    if filter_words in instance.snippet.lower():
                        filtered_list.append(instance)
    return filtered_list


def sort_vacancies(filtered_vacancies):
    """ Функция для сортировки списка ваканский по з/п"""
    new_list = []
    for instance in filtered_vacancies:
        if instance.payment is None:
            del filtered_vacancies[filtered_vacancies.index(instance)]

    while filtered_vacancies:

        max_scale = filtered_vacancies[0].payment
        max_scale_exz = filtered_vacancies[0]
        for instance in filtered_vacancies:
            if instance.payment is not None and instance.payment != 0:
                if instance.payment > max_scale:
                    max_scale = instance.payment
                    max_scale_exz = instance
        else:
            new_list.append(max_scale_exz)
            del filtered_vacancies[filtered_vacancies.index(max_scale_exz)]

    return new_list


def get_top_vacancies(sorted_vacancies, top_n):
    """ Функция для нахождения топ N списка ваканский """
    return sorted_vacancies[:top_n]
