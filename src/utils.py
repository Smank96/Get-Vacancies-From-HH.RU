def get_top_vacancies(vacancies: list[object], n: int) -> list[object]:
    """Сортировка списка экземпляров класса Vacancy по зарплате.
     Возвращает список топ N вакансий."""
    sorted_list = list(sorted(vacancies, key=lambda x: x.salary, reverse=True))
    return sorted_list[:n]


def print_vacancies(vacancies: list[object]):
    """Вывод вакансий на экран."""
    for vacancy in vacancies:
        print(vacancy)


def filter_vacancies(vacancies: list[object], filter_words: list[str]) -> list[object]:
    """Фильтр вакансий по заданному запросу от пользователя.
    Поиск ключевых слов происходит в аттрибуте requirement/"""
    filtered_vacancies = []

    # если ключевые слова не заданны, то возвращается исходный список вакансий.
    if len(filter_words) == 0:
        return vacancies

    for vacancy in vacancies:
        for word in filter_words:
            if word in vacancy.requirement:
                filtered_vacancies.append(vacancy)

    if len(filtered_vacancies) != 0:
        return filtered_vacancies
    else:
        print("Не найдено совпадений по ключевым словам.")
        # Вернёт пустой список.
        return filtered_vacancies
