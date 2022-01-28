import sys
import re
from bs4 import BeautifulSoup


def get_img_filename(img_tag):
    regex = '[ \w-]+?(?=\.)'
    img_filename = re.search(regex, img_tag['src'])
    img_filename = img_filename.group()
    return img_filename

def add_attr_to_img_tags(attr, fp, soup):
    img_tags = soup.select(f"img:not([{attr}]), img[{attr}=\"\"]")
    for img_tag in img_tags:
        img_filename = get_img_filename(img_tag)
        text = img_filename.replace('-', ' ').title()
        img_tag[attr] = text

def main():
    args = sys.argv[1:]
    for file in args:
        with open(file) as fp:
            soup = BeautifulSoup(fp, 'html.parser')
            add_attr_to_img_tags('alt', fp, soup)
            add_attr_to_img_tags('title', fp, soup)
            with open(file+".new", "wb") as f_output:
                f_output.write(soup.prettify("utf-8"))

main()
