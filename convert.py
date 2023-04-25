from bs4 import BeautifulSoup
import bs4
import re
from ebooklib import epub
from tqdm import tqdm
import argparse

from pathlib import Path

def _convert_file_path(path):
    path_obj = Path(path)
    new_name = "converted-" + path_obj.name
    new_path = path_obj.with_name(new_name)
    return str(new_path)


def convert_to_bionic_str(soup: BeautifulSoup, s: str):
    new_parent = soup.new_tag("span")
    words = re.split(r'.,;:!?-|\s', s)
    for word in words:
        mid = (len(word) // 2) + 1
        first_half, second_half = word[:mid], word[mid:]
        b_tag = soup.new_tag("b")
        b_tag.append(soup.new_string(first_half))
        new_parent.append(b_tag)
        new_parent.append(soup.new_string(second_half + " "))

    return new_parent

def convert_to_bionic(content: str):
    soup = BeautifulSoup(content, 'html.parser')
    for e in soup.descendants:
        if isinstance(e, bs4.element.Tag):
            if e.name == "b":
                continue
            children = list(e.children)
            if len(children) == 1:
                if len(children[0].text):
                    children[0].replace_with(convert_to_bionic_str(soup, children[0].text))
    return str(soup).encode()

def convert_book(book_path):
    source = epub.read_epub(book_path)
    for item in tqdm(source.items):
        if item.media_type == "application/xhtml+xml":
            content = item.content.decode('utf-8')
            item.content = convert_to_bionic(content)
    epub.write_epub(_convert_file_path(book_path), source)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process a book file.')
    parser.add_argument('book_path', metavar='book_path', type=str,
                        help='the path to the book file')
    args = parser.parse_args()
    convert_book(args.book_path)
    # The path to the book file can now be accessed using `args.book_path`
