from utils import filter_vacancies, sort_vacancies, get_top_vacancies
from jsonsaver import JSONSaver


def user_interaction():
    chose_platform = int(
        input('На каком сайте искать вакансии?\n1:"HeadHunter"\n2:"SuperJob\n3:оба варианта\n4:выход\n'))
    if chose_platform == 4:
        quit()
    search_query = input("Введите название вакансии: ")
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ")
    if ' ' in filter_words:
        filter_words = filter_words.split()
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))

    filtered_vacancies = filter_vacancies(search_query, filter_words, chose_platform)

    sorted_vacancies = sort_vacancies(filtered_vacancies)
    top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
    if not top_vacancies:
        quit()
    json = JSONSaver()
    for vacancy in top_vacancies:
        print(vacancy)
        chose = int(input('Сохранить вакансию?\n1:да\n2:нет\n3:выход\n'))
        if chose == 1:
            json.add_vacancy(vacancy)
        if chose == 2:
            json.delete_vacancy(vacancy)
        if chose == 3:
            quit('Досвидания')


if __name__ == "__main__":
    user_interaction()
