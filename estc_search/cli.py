import click


@click.command()
@click.option("--query", prompt="Query String", help="Search ESTC using this query string")
def main(query):
    click.echo(f"Hello, {query}!")


if __name__ == "__main__":
    main()
