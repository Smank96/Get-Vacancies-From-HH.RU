import json
from abc import ABC, abstractmethod


class Fileworker(ABC):
    @abstractmethod
    def add_vacancies_to_json(self, data):
        pass

    @abstractmethod
    def read_file(self):
        pass

    @abstractmethod
    def delete_vacancies(self):
        pass


class JSONSaver(Fileworker):
    """Класс для работы с json файлами."""
    def __init__(self):
        self.__file_name = "data/vacancies.json"

    def set_filename(self, new_filename):
        """Сеттер названия json файла."""
        self.__file_name = new_filename

    def add_vacancies_to_json(self, vacancies: list[object]):
        """Преобразует список экземпляров класса Vacancy в набор данных для json и сохраняет в json файл."""
        # Открываем файл на чтение, сохраняем все данные в переменную.
        with open(self.__file_name, "r", encoding="utf-8") as file:
            data = json.load(file)

        # Добавляем вакансии в список вакансий из файла.
        data.extend(vacancies)

        # Открываем файл на чтение, перезаписываем весь файл новой переменной.
        with open(self.__file_name, "w", encoding="utf-8") as file:
            json.dump(data, file, default=lambda x: x.__dict__, indent=4, ensure_ascii=False)

    def read_file(self) -> list[dict]:
        """Читает сохраненные вакансии из json файла.
        Возвращает список словарей."""
        with open(self.__file_name, "r", encoding="utf-8") as file:
            data = json.load(file)

        return data

    def delete_vacancies(self):
        """Очищает файл vacancies.json."""
        with open(self.__file_name, "w") as file:
            json.dump([], file)
