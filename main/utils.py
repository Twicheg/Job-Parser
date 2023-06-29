from vacation import Vacation
from vacations_API import HeadHunterAPI, SuperJobAPI


def create_vacations_list(chose_platform):
    vacations_list = []
    h = HeadHunterAPI()
    s = SuperJobAPI()
    if chose_platform != 2:
        for i in h.get_vacancies():
            try:
                if i['salary']['from'] and i['salary']['to']:
                    salary = max(i['salary']['from'], i['salary']['to'])
                elif i['salary']['from']:
                    salary = i['salary']['from']
                elif i['salary']['to']:
                    salary = i['salary']['from']
            except TypeError:
                salary = 0
            snippet = str(i['snippet']['responsibility']) + str(i['snippet']['requirement'])
            vacations_list.append(Vacation(
                i['id'],
                i['name'],
                i['apply_alternate_url'],
                salary,
                i['experience']['name'],
                snippet))

    elif chose_platform != 1:
        for i in s.get_vacancies():
            vacations_list.append(Vacation(
                i['id'],
                i['profession'],
                i['client']['link'],
                i['payment_from'] if i['payment_from'] > 0 else i['payment_to'],
                i['experience']['title'],
                i['candidat']))
    return vacations_list


def filter_vacancies(search_query, filter_words, chose_platform):
    filtered_list = []
    true_list = []
    if type(filter_words).__name__ == list.__name__:
        for i in create_vacations_list(chose_platform):
            if i.snippet:
                if search_query.lower() in i.vacation_name.lower():
                    for j in filter_words:
                        if j in i.snippet:
                            true_list.append(True)
                    if False not in true_list:
                        filtered_list.append(i)
                    true_list = []
    elif type(filter_words).__name__ == str.__name__:
        for i in create_vacations_list(chose_platform):
            if i.snippet:
                if search_query.lower() in i.vacation_name.lower():
                    if filter_words in i.snippet.lower().replace(',', ' ').split():
                        filtered_list.append(i)
    return filtered_list


def sort_vacancies(filtered_vacancies):
    payment_list = []
    new_list = []
    for i in filtered_vacancies:
        if i.payment is not None and i.payment != 0:
            payment_list.append(i.payment)
    payment_list.sort(reverse=True)
    for j in payment_list:
        for i in filtered_vacancies:
            if j == i.payment:
                new_list.append(i)
                filtered_vacancies.remove(i)
    return new_list


def get_top_vacancies(sorted_vacancies, top_n):
    return sorted_vacancies[:top_n]
