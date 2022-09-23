import json

from application.settings import INPUT_PATH


def read_file() -> None:
    path = INPUT_PATH.joinpath("some_data.json")

    content_serialized = path.read_text()

    data = json.loads(content_serialized)

    print(data)
