# main.py

import logging
import os
from faker import Faker
import typer
from dotenv import load_dotenv
from rich.console import Console
from rich.table import Table

app = typer.Typer()

load_dotenv()

if not os.path.exists("logs"):
    os.makedirs("logs")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("logs/app.log"), logging.StreamHandler()],
)


@app.command()
def generate_random_text(
    count: int = typer.Option(default=10, help="Count of fake humans data to generate"),
    seed: int = typer.Option(default=None, help="Seed for random text generation"),
):
    logging.info("Start of function execution")

    if seed:
        logging.info("Using seed for fake from args")
    else:
        seed_from_dotenv = os.getenv("FAKER__SEED")
        if seed_from_dotenv:
            logging.info("Using seed for fake from .env ")
        else:
            logging.info("Using random seed for fake")
        seed = seed_from_dotenv if seed_from_dotenv else Faker().random_int()

    count_from_dotenv = os.getenv("HUMANS_COUNT")
    count = int(count_from_dotenv) if count_from_dotenv else count

    Faker.seed(seed)
    fake = Faker("uk_UA")

    logging.info(f"Using seed {seed} for faking")
    logging.info(f"Number of people to generate: {count}")

    table = Table(title="Fake humans data")

    table.add_column("Name")
    table.add_column("Age", justify="right")
    table.add_column("Adress")
    table.add_column("Phone number")

    for _ in range(count):
        random_name = f"{fake.last_name()} {fake.first_name()}"
        random_age = fake.random_int(min=0, max=100)
        random_adress = fake.address()
        random_phone_number = fake.numerify("+38 (0##) ###-##-##")

        logging.info(
            f"Generated human with next data: {random_name}, {random_age}, {random_adress}, {random_phone_number}"
        )

        table.add_row(random_name, str(random_age), random_adress, random_phone_number)

    console = Console()
    console.print(table)

    logging.info("The function has been completed")


if __name__ == "__main__":
    try:
        app()
    except Exception as e:
        logging.warning(f"The program failed with the following error:\n{e}")
