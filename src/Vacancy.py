class Vacancy:
    """Класс для описания вакансии."""

    def __init__(self,
                 vacancy_name: str,
                 city: str,
                 url: str,
                 salary: int,
                 currency: str,
                 requirement: str):
        self.vacancy_name = self.__validate_data(vacancy_name)
        self.city = self.__validate_data(city)
        self.url = self.__validate_data(url)
        self.salary = salary
        self.currency = currency
        self.requirement = self.__validate_data(requirement)

    def __str__(self):
        return (f"Название вакансии: {self.vacancy_name}\n"
                f"Город: {self.city}\n"
                f"Ссылка: {self.url}\n"
                f"Зарплата: {self.salary} {self.currency}\n"
                f"Требования: {self.requirement}\n")

    def __lt__(self, other) -> bool:
        """Метод для сравнения зарплаты между экземплярами класса Vacancy (знак меньше "<")."""
        if self.salary < other.salary:
            return True
        else:
            return False

    def __gt__(self, other) -> bool:
        """Метод для сравнения зарплаты между экземплярами класса Vacancy (знак больше ">")."""
        if self.salary > other.salary:
            return True
        else:
            return False

    @staticmethod
    def __validate_data(data):
        """Метод для проверки наличия данных."""
        if data:
            return data
        else:
            return "Отсутствует"

    @staticmethod
    def _validate_salary(vacancy: dict):
        """Метод для проверки указана зарплата ли зарплата.
        Если да - преобразует строку в число и возвращает его.
        Если нет - возвращает 0."""
        if vacancy.get('salary') and vacancy.get('salary').get('from'):
            return int(vacancy.get('salary').get('from'))
        return 0

    @staticmethod
    def _validate_currency(vacancy: dict):
        """Метод для проверки указан ли валюта для зарплаты.
        Если да - возвращает её.
        Если нет - возвращает пустую строку."""
        if vacancy.get('salary') and vacancy.get('salary').get('currency'):
            return vacancy.get('salary').get('currency')
        return ""

    @staticmethod
    def cast_to_object_list(vacancies: list) -> list[object]:
        """Преобразование данных полученных от API HH.RU в список экземпляров класса Vacancy и возвращает его."""
        vacancies_list = []

        for vacancy in vacancies:
            vacancies_list.append(Vacancy(vacancy_name=vacancy.get('name'),
                                          city=vacancy.get('area').get('name'),
                                          url=vacancy.get('alternate_url'),
                                          salary=Vacancy.__validate_salary(vacancy),
                                          currency=Vacancy.__validate_currency(vacancy),
                                          requirement=vacancy.get('snippet').get('requirement')))

        return vacancies_list
