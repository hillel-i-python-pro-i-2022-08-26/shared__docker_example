from application.services.faker_obj import faker
from application.typing import T_MESSAGE


def generate_message() -> T_MESSAGE:
    return f"Hello, {faker.unique.first_name()}"
