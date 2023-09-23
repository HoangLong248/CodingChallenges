import click
import os
import sys

def get_size_of_file(fin):
    n_size = len((bytes(fin, 'utf-8')))
    if n_size:
        return n_size
    return 0

def get_lines_of_file(fin):
    n_lines = fin.count('\n')
    return n_lines

def get_words_of_files(fin):
    n_words = fin.split()
    return len(n_words)

def get_char_of_files(fin):
    return len(fin)

@click.command("ccwc")
@click.option("-c", "--bytes", is_flag=True, help="print the byte counts", default=False)
@click.option("-l", "--lines", is_flag=True, help="print the newline counts", default=False)
@click.option("-w", "--words", is_flag=True, help="print the word counts", default=False)
@click.option("-m", "--chars", is_flag=True, help="print the characters counts", default=False)
@click.argument('file', type=click.File(), default=sys.stdin)
def ccwc(bytes, lines, words, chars, file):
    """ccwc - print newline, word, and byte counts for each file"""
    output = []
    console_out = ""
    filename = file.name
    fin = file.read()
    if (bytes == False) and (lines == False) and (words == False) and (chars == False):
        output.append(get_size_of_file(fin))
        output.append(get_lines_of_file(fin))
        output.append(get_words_of_files(fin))
    else:
        if bytes:
            num_bytes = get_size_of_file(fin)
            output.append(num_bytes)
        if lines:
            num_lines = get_lines_of_file(fin)
            output.append(num_lines)
        if words:
            num_words = get_words_of_files(fin)
            output.append(num_words)
        if chars:
            num_chars = get_char_of_files(fin)
            output.append(num_chars)
    
        
    for item in sorted(output):
        console_out += f"{item} "
    if file != sys.stdin:
        console_out += f"{filename}"
    print(console_out)