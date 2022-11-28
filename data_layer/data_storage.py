import json
from typing import List

from model.models import Vacancy


def fetch_existing_codes_from_storage() -> List[str]:
    try:
        with open("../existing_vacancies.json", "r") as openfile:
            EXISTING_CODES = json.load(openfile)
    except FileNotFoundError as error:
        EXISTING_CODES = ["22-670 13041", "22-661 12901"]

    return EXISTING_CODES


def store_vacancies_in_storage(vacancies: List[Vacancy]):
    with open("../existing_vacancies.json", "w") as outfile:
        json.dump([vacancy.code for vacancy in vacancies], outfile)
