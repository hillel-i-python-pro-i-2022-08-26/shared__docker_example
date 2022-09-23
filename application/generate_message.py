from faker import Faker

from application.typing import T_MESSAGE

faker = Faker()


def generate_message() -> T_MESSAGE:
    return f"Hello, {faker.unique.first_name()}"
