import json


class Vacancy:
    """Класс для описания вакансии."""

    def __init__(self,
                 vacancy_name: str,
                 city: str,
                 url: str,
                 salary: int,
                 currency: str,
                 requirement: dict):
        self.vacancy_name = self.validate_data(vacancy_name)
        self.city = self.validate_data(city)
        self.url = self.validate_data(url)
        self.salary = salary
        self.currency = currency
        self.requirement = self.validate_data(requirement)

    def __str__(self):
        return (f"Название вакансии: {self.vacancy_name}\n"
                f"Город: {self.city}\n"
                f"Ссылка: {self.url}\n"
                f"Зарплата: {self.salary} {self.currency}\n"
                f"Требования: {self.requirement}\n")

    # def __lt__(self, other):
    #     if self.salary != 0:
    #         salary1 = int(self.salary.split()[0])
    #     else:
    #         salary1 = self.salary
    #
    #     if other.salary != 0:
    #         salary2 = int(other.salary.split()[0])
    #     else:
    #         salary2 = other.salary
    #
    #     if salary1 < salary2:
    #         return True
    #     else:
    #         return False

    # def __gt__(self, other):
    #     if self.salary != 0:
    #         salary1 = int(self.salary.split()[0])
    #     else:
    #         salary1 = self.salary
    #
    #     if other.salary != 0:
    #         salary2 = int(other.salary.split()[0])
    #     else:
    #         salary2 = other.salary
    #
    #     if salary1 > salary2:
    #         return True
    #     else:
    #         return False

    @staticmethod
    def validate_data(data):
        if data:
            return data
        else:
            return "Отсутствует"

    @staticmethod
    def validate_salary(vacancy):
        if vacancy.get('salary') and vacancy.get('salary').get('from'):
            return int(vacancy.get('salary').get('from'))
        return 0

    @staticmethod
    def validate_currency(vacancy):
        if vacancy.get('salary') and vacancy.get('salary').get('currency'):
            return vacancy.get('salary').get('currency')
        return ""

    @staticmethod
    def cast_to_object_list(vacancies) -> list:
        """Преобразование данных из JSON в список экземпляров класса Vacancy"""

        vacancies_list = []

        for vacancy in vacancies:
            vacancies_list.append(Vacancy(vacancy_name=vacancy.get('name'),
                                          city=vacancy.get('area').get('name'),
                                          url=vacancy.get('alternate_url'),
                                          salary=Vacancy.validate_salary(vacancy),
                                          currency=Vacancy.validate_currency(vacancy),
                                          requirement=vacancy.get('snippet').get('requirement')))

        return vacancies_list
