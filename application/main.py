from application.services.generate_message import generate_message
from application.services.read_file import read_file


def main() -> None:
    print(generate_message())
    read_file()
