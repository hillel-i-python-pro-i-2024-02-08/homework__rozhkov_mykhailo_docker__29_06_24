from rich.console import Console
from rich.table import Table


def print_table(table: Table) -> None:
    """
    Prints the table in the console.

    :param table: An instance of the Rich Table class to print.
    :return: None
    """
    console = Console()
    console.print(table)
