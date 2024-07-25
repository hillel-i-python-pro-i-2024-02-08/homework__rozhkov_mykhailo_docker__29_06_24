import logging
import typer
from helpers import (
    init_app_settings,
    print_table,
    fill_table_with_fake_data,
    set_faker_settings,
    init_table,
    get_number_of_people,
    get_faker_seed,
)


app = typer.Typer()


@app.command()
def generate_random_text(
    count: int = typer.Option(default=10, help="Number of fake people data to be generated"),
    seed: int = typer.Option(default=None, help="Seed for generating fake data"),
) -> None:
    """
    Generates and displays a table of fake human data.

    :param count: Number of fake human data entries to generate.
    :param seed: Seed for generating fake data.
    :return: None
    """
    logging.info("Start of function execution")
    # Init fake seed and count
    seed = get_faker_seed(seed)
    count = get_number_of_people(count)

    fake = set_faker_settings(seed)

    logging.info(f"Using seed {seed} for faking")
    logging.info(f"Number of people to generate: {count}")

    # Create and fill table with fake data
    table = init_table()
    fill_table_with_fake_data(count, fake, table)

    print_table(table)

    logging.info("Function completed")


if __name__ == "__main__":
    try:
        init_app_settings()
        app()
    except Exception as e:
        logging.warning(f"The program ended with the following error:\n{e}")
