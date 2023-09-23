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

def get_lines_of_file(fin):
    with open(fin) as f:
        lines = f.readlines()
    return len(lines)

@click.command("ccwc")
@click.option("-c", "--bytes", is_flag=True, help="print the byte counts", default=False)
@click.option("-l", "--lines", is_flag=True, help="print the newline counts", default=False)
@click.argument('filename', type=click.Path(exists=True))
def ccwc(bytes, lines, filename):
    """ccwc - print newline, word, and byte counts for each file"""
    if bytes:
        c_bytes = get_size_of_file(filename)
        print(c_bytes, filename)
    if lines:
        l_lines = get_lines_of_file(filename)
        print(l_lines, filename)