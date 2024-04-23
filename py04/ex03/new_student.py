import random
import string
from dataclasses import dataclass, field


def getlogin(name: str, surname: str):
    return name[0].capitalize() + surname.lower()


def generate_id() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass()
class Student:
    name: str = field(init=True)
    surname: str = field(init=True)
    active: bool = field(init=True, default=True)
    login: str = field(init=False)
    id: str = field(init=False)

    def __post_init__(self):
        self.login = getlogin(self.name, self.surname)
        self.id = generate_id()
