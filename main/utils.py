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
        for i in parser_1:
            if i['salary'] is not None:
                if 'from' in i['salary'].keys():
                    salary = i['salary']['from']
                elif 'to' in i['salary'].keys():
                    salary = i['salary']['to']
            else:
                salary = 0

            snippet = str(i['snippet']['responsibility']) + str(i['snippet']['requirement'])
            vacations_list.append(Vacation(
                i['id'],
                i['name'],
                i['apply_alternate_url'],
                salary,
                i['experience']['name'],
                snippet))

    if chose_platform in [2, 3]:
        for i in parser_2:
            if i['payment_from'] != 0 or i['payment_to'] != 0:
                salary = max(int(i['payment_from']), int(i['payment_to']))
            else:
                salary = 0

            vacations_list.append(Vacation(
                i['id'],
                i['profession'],
                i['client']['link'],
                salary,
                i['experience']['title'],
                i['candidat']))
    JSONSaver.instance_list = vacations_list
    return vacations_list


def filter_vacancies(search_vacancy, filter_words, chose_platform):
    """ Фукция для фильтра списка экзеров ваканский по заданным требованиям"""
    filtered_list = []
    if type(filter_words).__name__ == list.__name__:
        for i in create_vacations_list(chose_platform):
            if i.snippet:
                true_list = []
                if search_vacancy.lower() in i.vacation_name.lower():
                    for j in filter_words:
                        if j in i.snippet.lower():
                            true_list.append(True)
                        else:
                            true_list.append(False)
                    if False not in true_list:
                        filtered_list.append(i)

    elif type(filter_words).__name__ == str.__name__:
        for i in create_vacations_list(chose_platform):
            if i.snippet:
                if search_vacancy.lower() in i.vacation_name.lower():
                    if filter_words in i.snippet.lower():
                        filtered_list.append(i)
    return filtered_list


def sort_vacancies(filtered_vacancies):
    """ Функция для сортировки списка ваканский по з/п"""
    new_list = []
    for i in filtered_vacancies:
        if i.payment is None:
            del filtered_vacancies[filtered_vacancies.index(i)]

    while filtered_vacancies:

        max_scale = filtered_vacancies[0].payment
        max_scale_exz = filtered_vacancies[0]
        for i in filtered_vacancies:
            if i.payment is not None and i.payment != 0:
                if i.payment > max_scale:
                    max_scale = i.payment
                    max_scale_exz = i
        else:
            new_list.append(max_scale_exz)
            del filtered_vacancies[filtered_vacancies.index(max_scale_exz)]

    return new_list


def get_top_vacancies(sorted_vacancies, top_n):
    """ Функция для нахождения топ N списка ваканский """
    return sorted_vacancies[:top_n]
