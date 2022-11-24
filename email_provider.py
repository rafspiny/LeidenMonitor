from typing import List

from models import Vacancy
from secrets import MAILJET_API_KEY, MAILJET_API_SECRET

from mailjet_rest import Client
from email_config import NAME as recipient_name, EMAIL as recipient_email

EMAIL_TEMPLATE = f"""
Hi {recipient_name},
This is an automated message.
I found new vacancies for the department of your choice:
"""

HTML_TEMPLATE = f"""
<h3>Hi {recipient_name}</h3>,<br\>
Please review the latest opening position at the department of you choice of the Leiden university.
<br/>
"""


class MailEngine:
    def __init__(self):
        try:
            self.mailer = Client(auth=(MAILJET_API_KEY, MAILJET_API_SECRET), version='v3.1')
        except Exception as error:
            print('An exception occurred: {}'.format(error))
            raise error

    def send_email(self, message):
        """
        Send an email using the mailjet API.
        """
        try:
            result = self.mailer.send.create(data=message)
            if result.status_code != 200:
                print(result.status_code)
                print(result.json())
                raise Exception("Unable to send email")
        except Exception as error:
            print('An exception occurred: {}'.format(error))


def _generate_html_list(vacancies: List[Vacancy]) -> str:
    return "<ul><br\>" + "<br/>".join(
        [f"<li>{vacancy.title} available <a href='{vacancy.link}'>here</a> with code {vacancy.code}</li>" for vacancy in vacancies]
    ) + "</ul>"


def send_vacancies_via_email(engine: MailEngine, vacancies: List[Vacancy]):
    data = {
        'Messages': [
            {
                "From": {
                    "Email": "info@rafspiny.eu",
                    "Name": "Raffaele-bot"
                },
                "To": [
                    {
                        "Email": recipient_email,
                        "Name": recipient_name
                    }
                ],
                "Subject": "New opening at Lat faculty in Leiden",
                "TextPart": EMAIL_TEMPLATE + "\n".join([str(vacancy) for vacancy in vacancies]),
                "HTMLPart": HTML_TEMPLATE + _generate_html_list(vacancies) + "<br />May the delivery force be with you!",
                "CustomID": "AppGettingStartedTest"
            }
        ]
    }

    engine.send_email(message=data)