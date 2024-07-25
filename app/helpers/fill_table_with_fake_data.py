import logging
from faker import Faker
from rich.table import Table


def fill_table_with_fake_data(count: int, fake: Faker, table: Table) -> None:
    """
    Fills a Rich Table with randomly generated fake human data.

    :param count: The number of fake human data entries to generate.
    :param fake: An instance of the Faker class for generating fake data.
    :param table: An instance of the Rich Table class where the data will be added.
    :return: None
    """
    for _ in range(count):
        random_name = f"{fake.last_name()} {fake.first_name()}"
        random_age = fake.random_int(min=0, max=100)
        random_address = fake.address()
        random_phone_number = fake.numerify("+38 (0##) ###-##-##")

        logging.info(
            f"Generated person with the following data: {random_name}, {random_age}, {random_address}, {random_phone_number}"
        )

        table.add_row(random_name, str(random_age), random_address, random_phone_number)
