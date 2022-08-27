import click
import csv
from .parser import est_info
from tabulate import tabulate


@click.command()
@click.option('--estc_numbers', is_flag=False, default=[], required=True,
              metavar='<estc_numbers>', type=click.STRING, help='ESTC numbers')
def main(estc_numbers):
    # split input by ',' and remove whitespace
    estc_numbers = [c.strip() for c in estc_numbers.split(',')]
    result = est_info(estc_numbers)
    with open("output.csv","w+") as output_csv:
        csv_writer = csv.writer(output_csv,delimiter=',')
        csv_writer.writerows(result)
    print(tabulate(result, headers='keys', tablefmt='fancy_grid', showindex=False,
                   maxcolwidths=[10, 30, 30, 30, 20, 30, 30, 30, 30]))


if __name__ == "__main__":
    main()
