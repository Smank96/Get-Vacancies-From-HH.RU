def get_top_vacancies(vacancies: list[object], n: int) -> list[object]:
    """Сортировка списка экземпляров класса Vacancy по зарплате.
     Возвращает список топ N вакансий."""
    sorted_list = list(sorted(vacancies, key=lambda x: x.salary, reverse=True))
    return sorted_list[:n]


def print_vacancies(vacancies: list[object]):
    """Вывод вакансий на экран."""
    for vacancy in vacancies:
        print(vacancy)


def filter_vacancies(vacancies: list[object], filter_words) -> list[object]:
    """Фильтр вакансий по заданному запросу от пользователя."""
    pass
