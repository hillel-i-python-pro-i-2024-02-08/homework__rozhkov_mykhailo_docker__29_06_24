from rich.table import Table


def init_table() -> Table:
    """
    Initializes a Rich Table for storing fake human data.

    :return: An instance of the Rich Table class.
    """
    table = Table(title="Fake Human Data")

    table.add_column("Name")
    table.add_column("Age", justify="right")
    table.add_column("Address")
    table.add_column("Phone Number")
    return table
