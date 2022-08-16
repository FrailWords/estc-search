import click
from .parser import est_info
from tabulate import tabulate


@click.command()
@click.option("--estc_number", prompt="estc_number", help="Search ESTC using this number")
def main(estc_number):
    print(tabulate(est_info(estc_number), headers='keys', tablefmt='fancy_grid', showindex="always", maxcolwidths=[10, 30]))


if __name__ == "__main__":
    main()
