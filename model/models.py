from dataclasses import dataclass


@dataclass
class Vacancy:
    title: str
    code: str
    type: str
    link: str

    def __str__(self):
        return f"Vacancy for `{self.title}` with code {self.code} at URL: {self.link}"
