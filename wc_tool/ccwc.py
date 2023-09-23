import click
import os

def read_file(fin):
    content = None
    with open(fin) as f_in:
        content = f_in.read()
    return content

def get_size_of_file(fin):
    size = os.path.getsize(fin)
    return size

@click.command("ccwc")
@click.option("-c", "--bytes", is_flag=True, help="print the byte counts", default=False)
@click.argument('filename', type=click.Path(exists=True))
def ccwc(bytes, filename):
    """ccwc - print newline, word, and byte counts for each file"""
    if bytes:
        print(get_size_of_file(filename))