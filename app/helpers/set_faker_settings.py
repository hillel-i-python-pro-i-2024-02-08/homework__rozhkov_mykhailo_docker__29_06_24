from faker import Faker


def set_faker_settings(seed: int) -> Faker:
    """
    Sets up the Faker instance with the specified seed.

    :param seed: Seed for generating fake data.
    :return: An instance of the Faker class.
    """
    Faker.seed(seed)
    fake = Faker("uk_UA")
    return fake
