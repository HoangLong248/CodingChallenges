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

def get_words_of_files(fin):
    with open(fin) as f:
        words = f.read().split()
    return len(words)

@click.command("ccwc")
@click.option("-c", "--bytes", is_flag=True, help="print the byte counts", default=False)
@click.option("-l", "--lines", is_flag=True, help="print the newline counts", default=False)
@click.option("-w", "--words", is_flag=True, help="print the word counts")
@click.argument('filename', type=click.Path(exists=True))
def ccwc(bytes, lines, words, filename):
    """ccwc - print newline, word, and byte counts for each file"""
    if bytes:
        num_bytes = get_size_of_file(filename)
        print(num_bytes, filename)
    if lines:
        num_lines = get_lines_of_file(filename)
        print(num_lines, filename)
    if words:
        num_words = get_words_of_files(filename)
        print(num_words, filename)