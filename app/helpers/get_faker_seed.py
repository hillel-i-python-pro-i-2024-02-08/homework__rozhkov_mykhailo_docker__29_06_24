import logging
import os
from faker import Faker


def get_faker_seed(seed: int) -> int:
    """
    Gets the seed for the fake data generator from arguments, environment variable, or uses a random value.

    :param seed: Seed for generating fake data.
    :return: The final seed for generating fake data.
    """
    if seed:
        logging.info("Using a seed for fake data from args")
    else:
        seed_from_dotenv = os.getenv("FAKER__SEED")
        if seed_from_dotenv:
            logging.info("Using a seed for fake data from .env")
        else:
            logging.info("Using a random seed for fake data")
        seed = seed_from_dotenv if seed_from_dotenv else Faker().random_int()
    return seed
