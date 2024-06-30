import pytest
from src.utils import get_top_vacancies, filter_vacancies
from src.Vacancy import Vacancy


@pytest.fixture()
def collection():
    vacansies_list = []

    vacansies_list.append(Vacancy("Разработчик",
                                  "Москва",
                                  "https://hh.ru/",
                                  80000,
                                  "RUB",
                                  "Опыт 3 года"))
    vacansies_list.append(Vacancy("Курьер",
                                  "Кисловодск",
                                  "https://hh.ru/",
                                  70000, "RUB",
                                  "Без опыта"))
    vacansies_list.append(Vacancy("Водитель",
                                  "Питер",
                                  "https://hh.ru/",
                                  75000,
                                  "RUB",
                                  "Опыт от 1 года"))

    return vacansies_list


def test_get_top_vacancies(collection):
    result = get_top_vacancies(collection, 2)
    assert len(result) == 2
    assert result[0] == collection[0]
    assert result[1] == collection[2]

    empty_result = get_top_vacancies([], 5)
    assert empty_result == []


def test_filter_vacancies(collection):
    result = filter_vacancies(collection, ["Опыт 3 года"])
    assert len(result) == 1
    assert result == [collection[0]]

    empty_result = filter_vacancies(collection, ["abc abc abc"])
    assert empty_result == []
