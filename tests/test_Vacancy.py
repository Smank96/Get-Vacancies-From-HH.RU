import pytest
from src.Vacancy import Vacancy


@pytest.fixture()
def collection():
    vacansies = [
        {
            "name": "Разработчик",
            "area": {"name": "Москва"},
            "alternate_url": "https://hh.ru/",
            "salary": {"from": 80000, "currency": "RUB"},
            "snippet": {"requirement": "Опыт 3 года"}
        },
        {
            "name": "Курьер",
            "area": {"name": "Кисловодск"},
            "alternate_url": "https://hh.ru/",
            "salary": {"from": 70000, "currency": "RUB"},
            "snippet": {"requirement": "Без опыта"}
        },
        {
            "name": "Водитель",
            "area": {"name": "Питер"},
            "alternate_url": "https://hh.ru/",
            "salary": {"from": 75000, "currency": "RUB"},
            "snippet": {"requirement": "Опыт от 1 года"}
        },
        {
            "name": None,
            "area": {"name": None},
            "alternate_url": None,
            "salary": None,
            "snippet": {"requirement": None}
        }
    ]

    return vacansies


def test_str(collection):
    vacancy = Vacancy("Разработчик", "Москва", "https://hh.ru/", 80000, "RUB", "Опыт 3 года")

    expected_string = (f"Название вакансии: Разработчик\n"
                       f"Город: Москва\n"
                       f"Ссылка: https://hh.ru/\n"
                       f"Зарплата: 80000 RUB\n"
                       f"Требования: Опыт 3 года\n")

    assert str(vacancy) == expected_string


def test_validate_salary(collection):
    result = Vacancy._validate_salary(collection[0])
    empty_result = Vacancy._validate_salary(collection[3])

    assert result == 80000
    assert empty_result == 0


def test_validate_currency(collection):
    result = Vacancy._validate_currency(collection[0])
    empty_result = Vacancy._validate_currency(collection[3])

    assert result == "RUB"
    assert empty_result == ""


def test_lt(collection):
    vacancies = Vacancy.cast_to_object_list(collection)

    assert vacancies[1] < vacancies[0]
    assert vacancies[1] < vacancies[2]


def test_gt(collection):
    vacancies = Vacancy.cast_to_object_list(collection)

    assert vacancies[0] > vacancies[1]
    assert vacancies[0] > vacancies[2]


def test_cast_to_object_list(collection):
    result = Vacancy.cast_to_object_list(collection)

    assert len(result) == 4
    assert result[0].vacancy_name == "Разработчик"
    assert result[0].city == "Москва"
    assert result[0].url == "https://hh.ru/"
    assert result[0].salary == 80000
    assert result[0].currency == "RUB"
    assert result[0].requirement == "Опыт 3 года"

    assert result[1].vacancy_name == "Курьер"
    assert result[1].city == "Кисловодск"
    assert result[1].url == "https://hh.ru/"
    assert result[1].salary == 70000
    assert result[1].currency == "RUB"
    assert result[1].requirement == "Без опыта"

    assert result[3].vacancy_name == "Отсутствует"
    assert result[3].city == "Отсутствует"
    assert result[3].url == "Отсутствует"
    assert result[3].salary == 0
    assert result[3].currency == ""
    assert result[3].requirement == "Отсутствует"
