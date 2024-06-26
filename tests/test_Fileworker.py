import pytest
from src.Fileworker import JSONSaver
from src.Vacancy import Vacancy


def test_add_vacancies_to_json():
    saver = JSONSaver()
    saver.set_filename("test_vacancies.json")

    vacancies = [
        Vacancy("Python Developer", "Moscow", "https://hh.ru/vacancy/1", 100000, "RUR", "Python, Django"),
        Vacancy("Java Developer", "Saint Petersburg", "https://hh.ru/vacancy/2", 120000, "RUR", "Java, Spring"),
        Vacancy("JavaScript Developer", "Moscow", "https://hh.ru/vacancy/3", 110000, "RUR", "JavaScript, React")
    ]

    saver.add_vacancies_to_json(vacancies)

    saved_data = saver.read_file()
    assert len(saved_data) == 3

    assert saved_data[0]["vacancy_name"] == "Python Developer"
    assert saved_data[0]["city"] == "Moscow"
    assert saved_data[0]["url"] == "https://hh.ru/vacancy/1"
    assert saved_data[0]["salary"] == 100000
    assert saved_data[0]["currency"] == "RUR"
    assert saved_data[0]["requirement"] == "Python, Django"

    assert saved_data[1]["vacancy_name"] == "Java Developer"
    assert saved_data[1]["city"] == "Saint Petersburg"
    assert saved_data[1]["url"] == "https://hh.ru/vacancy/2"
    assert saved_data[1]["salary"] == 120000
    assert saved_data[1]["currency"] == "RUR"
    assert saved_data[1]["requirement"] == "Java, Spring"

    assert saved_data[2]["vacancy_name"] == "JavaScript Developer"
    assert saved_data[2]["city"] == "Moscow"
    assert saved_data[2]["url"] == "https://hh.ru/vacancy/3"
    assert saved_data[2]["salary"] == 110000
    assert saved_data[2]["currency"] == "RUR"
    assert saved_data[2]["requirement"] == "JavaScript, React"

    saver.delete_vacancies()
