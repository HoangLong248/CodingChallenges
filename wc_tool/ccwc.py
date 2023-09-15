import click

@click.command("ccwc")
@click.option("-c", "--bytes", is_flag=True, help="print the byte counts", default=False)
@click.argument('filename', type=click.File(), default="-", required=False)
def ccwc(bytes, filename):
    """ccwc - print newline, word, and byte counts for each file"""
    click.echo("Hello World")
    click.echo(file=filename)