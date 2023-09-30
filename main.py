import typer
from typing_extensions import Annotated
from rich import print as rprint
from typing import Optional
import os


def print_output(file_name: str, file_size: int, line_count: int, count_byte: bool, line: bool) -> None:
    formatted_file_size = ('{:>8}'.format(file_size))
    formatted_line_count = ('{:>8}'.format(line_count))
    rprint(
        f'[blue]{formatted_line_count} ' if line else "", end="")
    rprint(f"[yellow]{formatted_file_size} " if count_byte else "", end="")
    rprint(f"[green]{file_name}")


def main(file_name: str, count_byte: Annotated[Optional[bool], typer.Option('-c')] = False, line: Annotated[Optional[bool], typer.Option('-l')] = False) -> None:
    # get the file size in bytes
    file_size = 0
    line_count = 0

    try:
        file_size = os.path.getsize(file_name)
        with open(file_name, 'r') as file:
            line_count = len(list(enumerate(file)))

        print_output(file_name, file_size, line_count, count_byte, line)
    except:
        rprint(f"file not found: [red]{file_name}")


if __name__ == "__main__":
    typer.run(main)
