from data_layer.data_storage import fetch_existing_codes_from_storage, store_vacancies_in_storage
from business.email_provider import send_vacancies_via_email, MailEngine
from business.logic import get_vacancies_from_website


mail_engine = MailEngine()
existing_codes = fetch_existing_codes_from_storage()
vacancies = get_vacancies_from_website()

new_vacancies = [vacancy for vacancy in vacancies if vacancy.code not in existing_codes]


if new_vacancies:
    print("RED ALERT. RED ALERT")
    for vacancy in new_vacancies:
        print(vacancy)

    # Save the new list
    send_vacancies_via_email(mail_engine, new_vacancies)
    store_vacancies_in_storage(vacancies)
else:
    print("Sorry. No new vacancies today.")
