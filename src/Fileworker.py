import json
from abc import ABC, abstractmethod


class Fileworker(ABC):
    @abstractmethod
    def save_vacancies(self, data):
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
        self.file_name = "../data/vacancies.json"

    def save_vacancies(self, data: list[object]):
        """Преобразует список экземпляров класса Vacancy в набор данных для json и сохраняет в json файл."""
        with open(self.file_name, "w", encoding="utf-8") as file:
            json.dump(data, file, default=lambda x: x.__dict__, indent=4, ensure_ascii=False)

    def read_file(self):
        pass

    def delete_vacancies(self):
        pass
