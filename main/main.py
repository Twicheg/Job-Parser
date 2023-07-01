from utils import filter_vacancies, sort_vacancies, get_top_vacancies
from jsonsaver import JSONSaver


def user_interaction():
    """Функция для общения с пользователем"""
    try:
        chose_platform = int(
            input(
                'На какой платформе искать вакансии?\n1:"HeadHunter"\n2:"SuperJob\n3:оба варианта\n4:Выход\n'))

        search_vacancy = input("Введите название вакансии: ")
        filter_words = input("Введите ключевые слова для фильтрации вакансий: ")
        top_n = int(input("Введите количество вакансий для вывода в топ N: "))
        if ' ' in filter_words:
            filter_words = filter_words.split()
    except Exception as e:
        print(e)
        print('Выставленны значения - оба варианта , топ 10 , search_vacancy = "python" ')
        chose_platform = 3
        top_n = 10
        search_vacancy = 'python'
        filter_words = ''
    if chose_platform == 4:
        quit('Досвидания')

    filtered_vacancies = filter_vacancies(search_vacancy, filter_words, chose_platform)
    sorted_vacancies = sort_vacancies(filtered_vacancies)
    top_vacancies = get_top_vacancies(sorted_vacancies, top_n)

    if not top_vacancies:
        if int(input('Результатов нет , попробовать еще раз?\n1:да\n2:выход')) == 1:
            user_interaction()
        else:
            quit('Досвидания')

    json = JSONSaver()
    try:
        choice = int(
            input('1:Просмотр результатов поиска\n2:Просмотр сохраненных результатов\n3:Удаление вакансии по id\n4:выход\n'))
    except Exception:
        choice = 4

    if choice == 1:
        for vacancy in top_vacancies:
            print(vacancy)
            chose = int(input('Сохранить вакансию?\n1:да\n2:нет\n3:выход\n4:в начало\n'))
            if chose == 1:
                json.add_vacancy(vacancy)
            if chose == 2:
                continue
            if chose == 3:
                break
            if chose == 4:
                user_interaction()
        json.save_to_file()
    if choice == 2:
        json.get_vacancies_by_salary(input('Введите минимальную з/п\n'))
    if choice == 3:
        json.delete_vacancy(int(input('Введите id\n')))
    if choice == 4:
        quit('Exit')
    print('Программа завершена')


if __name__ == "__main__":
    user_interaction()
