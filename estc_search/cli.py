import click
from .parser import est_info
from tabulate import tabulate


@click.command()
@click.option("--estc_number", prompt="estc_number", help="Search ESTC using this number")
def main(estc_number):
    result = est_info(estc_number)
    filename = "{}.csv".format(estc_number)
    result.to_csv(filename, index=False)
    print(tabulate(est_info(estc_number), headers='keys', tablefmt='fancy_grid', showindex=False, maxcolwidths=[10, 30, 30, 30, 20, 30, 30, 30]))


if __name__ == "__main__":
    main()
