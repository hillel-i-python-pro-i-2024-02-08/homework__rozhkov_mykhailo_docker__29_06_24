import os


def get_number_of_people(count: int) -> int:
    """
    Gets the number of people to generate from arguments, environment variable, or uses the default value.

    :param count: The number of fake human data entries to generate.
    :return: The final count of fake human data entries to generate.
    """
    count_from_dotenv = os.getenv("HUMANS_COUNT")
    count = int(count_from_dotenv) if count_from_dotenv else count
    return count
