import requests
from abc import ABC, abstractmethod


class Parser(ABC):

    @abstractmethod
    def get_vacancies(self, keyword):
        pass


class HeadHunterAPI(Parser):
    """Класс для взаимодействия с API HH.RU"""

    def __init__(self):
        self.url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': 100}
        self.vacancies = []

    def get_vacancies(self, keyword: str) -> list:
        """Получает вакансии"""
        self.params['text'] = keyword
        while self.params.get('page') != 1:
            response = requests.get(self.url, headers=self.headers, params=self.params)
            vacancies = response.json()['items']
            self.vacancies.extend(vacancies)
            self.params['page'] += 1

        return self.vacancies
