from utils import filter_vacancies, sort_vacancies, get_top_vacancies
from jsonsaver import JSONSaver


def user_interaction():
    try:
        chose_platform = int(
            input(
                'На какой платформе искать вакансии?\n1:"HeadHunter"\n2:"SuperJob\n3:оба варианта\n4:Выход\n'))
        top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    except Exception as e:
        print(e)
        print('Выставленны значения - оба варианта , топ 10')
        chose_platform = 3
        top_n = 10

    if chose_platform not in [1, 2, 3, 4]:
        quit()
    if chose_platform == 4:
        quit('Досвидания')

    search_vacancy = input("Введите название вакансии: ")
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ")
    if ' ' in filter_words:
        filter_words = filter_words.split()
    filtered_vacancies = filter_vacancies(search_vacancy, filter_words, chose_platform)
    sorted_vacancies = sort_vacancies(filtered_vacancies)
    top_vacancies = get_top_vacancies(sorted_vacancies, top_n)

    if not top_vacancies:
        quit('Таких нет')
    json = JSONSaver()
    choice = int(input('1:Просмотр результатов поиска\n2:Просмотр сохраненных\n3:Удаление вакансии по id\n'))
    if choice == 1:
        for vacancy in top_vacancies:
            print(vacancy)
            chose = int(input('Сохранить вакансию?\n1:да\n2:нет\n3:выход\n'))
            if chose == 1:
                json.add_vacancy(vacancy)
            if chose == 2:
                continue
            if chose == 3:
                break
        json.save_to_file()
    if choice == 2:
        try:
            json.get_vacancies_by_salary(int(input('Введите минимальную з/п\n')))
        except Exception as e:
            print(e)
    if choice == 3:
        json.delete_vacancy(int(input('Введите id\n')))

    print('Программа завершена')


if __name__ == "__main__":
    user_interaction()
