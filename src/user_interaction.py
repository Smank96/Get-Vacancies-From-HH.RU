from src.Parser import HeadHunterAPI
from src.Vacancy import Vacancy
from src.Fileworker import JSONSaver
from src.utils import get_top_vacancies, print_vacancies, filter_vacancies


def user_interaction():
    """Функция для взаимодействия с пользователем."""
    # Создание экземпляра класса для работы с API HH.ru.
    hh_api = HeadHunterAPI()

    search_query = input("Введите поисковый запрос: ")

    # Получение вакансий с hh.ru в формате JSON.
    hh_vacancies = hh_api.get_vacancies(search_query)

    # Преобразование данных из JSON в список экземпляров класса Vacancy.
    vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)

    try:
        top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    except ValueError:
        print("Для ввода допустимы только целые числа.")
        # Завершение программы.
        return

    # Получение списка топ N вакансий.
    top_vacancies = get_top_vacancies(vacancies_list, top_n)

    # filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()

    # filtered_vacancies = filter_vacancies(vacancies_list, filter_words)

    # Вывод списка вакансий на экран.
    print_vacancies(top_vacancies)

    # Создание экземпляра класса для работы с json файлами.
    json_saver = JSONSaver()
    # Сохранение информации о вакансиях в файл.
    json_saver.save_vacancies(top_vacancies)
