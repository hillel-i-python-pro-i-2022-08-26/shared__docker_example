import datetime
import json
import random

# noinspection PyPackageRequirements
from ulid import microsecond as ulid

from application.services.faker_obj import faker
from application.settings import OUTPUT_PATH


def generate_file() -> None:
    data = {
        "name": faker.unique.first_name(),
        "age": random.randint(0, 100),
        "datetime": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    }

    data_raw = json.dumps(data, indent=2)

    file_path = OUTPUT_PATH.joinpath(f"{ulid.new().uuid}.json")

    file_path.write_text(data_raw)
