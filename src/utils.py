
def filter_vacancies(vacancies_list, filter_words):
    """Фильтр вакансий по заданному запросу от пользователя."""
    pass


def get_vacancies_by_salary(filtered_vacancies, salary_range):
    """Получает вакансии по заданному диапазону зарплаты."""
    pass


def get_top_vacancies(vacancies_list, n):
    """Сортировка списка экземпляров класса Vacancy по зарплате.
     Возвращает список топ N вакансий."""
    sorted_list = list(sorted(vacancies_list, key=lambda x: x.salary, reverse=True))
    return sorted_list[:n]


def print_vacancies(vacancies_list):
    """Вывод вакансий на экран."""
    for vacancy in vacancies_list:
        print(vacancy)



