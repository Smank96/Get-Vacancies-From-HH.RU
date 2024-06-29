import json
from abc import ABC, abstractmethod


class Fileworker(ABC):
    @abstractmethod
    def save_vacancies(self, vacancies):
        pass


class JSONSaver(Fileworker):
    """Класс для сохранения данных полученных от api hh.ru в json"""
    def __init__(self):
        self.file_name = "../data/vacancies.json"

    def save_vacancies(self, data):
        """Добавляет вакансию в json."""
        with open(self.file_name, "w", encoding="utf-8") as file:
            json.dump(data, file, default=lambda x: x.__dict__, indent=4, ensure_ascii=False)
