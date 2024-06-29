import json


class JSONSaver:
    """Класс для сохранения данных полученных от api hh.ru в json"""

    def save_vacancies(self, vacancies: list):
        """Добавляет вакансию в json."""
        with open("data/vacancies.json", "w") as file:
            json.dump(vacancies, file)

    def delete_vacancy(self, vacancy):
        """Удаляет вакансию из json"""
        pass
