from src.Parser import HeadHunterAPI
from src.Vacancy import Vacancy
from src.JSONSaver import JSONSaver
from src.utils import get_top_vacancies, print_vacancies


def user_interaction():
    """Функция для взаимодействия с пользователем."""
    # Создание экземпляра класса для работы с API сайтов с вакансиями
    hh_api = HeadHunterAPI()

    search_query = input("Введите поисковый запрос: ")

    # Получение вакансий с hh.ru в формате JSON
    hh_vacancies = hh_api.get_vacancies(search_query)

    # Преобразование набора данных из JSON в список объектов
    vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)

    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    top_vacancies = (get_top_vacancies(vacancies_list, top_n))

    # Вывод на экран
    print_vacancies(top_vacancies)

    # Сохранение информации о вакансиях в файл
    json_saver = JSONSaver()
    json_saver.save_vacancies(top_vacancies)

    # filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()

    # salary_range = input("Введите диапазон зарплат: ")  # Пример: 100000 - 150000

    # filtered_vacancies = filter_vacancies(vacancies_list, filter_words)

    # ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)

    # sorted_vacancies = sort_vacancies(ranged_vacancies)

    # top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
