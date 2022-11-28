from typing import List

import requests
from lxml import html

from conf.constants import DEPARTMENT_URL, QUERY_STRING_DICT, WEBSITE
from model.models import Vacancy


def get_vacancies_from_website() -> List[Vacancy]:
    response = requests.get(DEPARTMENT_URL, params=QUERY_STRING_DICT)
    tree = html.fromstring(response.text)
    vacancies: List[Vacancy] = []
    possible_vacancies = tree.xpath("//div[@id="content"]//ul//li")
    for vacancy in possible_vacancies:
        title = vacancy.xpath("a/div/strong")[0].text
        code = vacancy.xpath("a/div/span")[0].text
        type = vacancy.xpath("a/div/span")[1].text
        link = WEBSITE + str(vacancy.xpath("a/@href")[0])
        vacancy = Vacancy(title, code, type, link)
        vacancies.append(vacancy)

    return vacancies
