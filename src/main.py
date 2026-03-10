import os
import textnode
from copyover import copy_over
from generatepage import generate_pages_recursive

src = os.path.join(os.getcwd(), "static")
dest = os.path.join(os.getcwd(), "../public")
content_src = os.path.join(os.getcwd(), "content")
template = os.path.join(os.getcwd(), "template.html")
content_dest = os.path.join(os.getcwd(), "public")

def main():
    node = textnode.TextNode("This is some anchor text", "link", "https://boot.dev")
    print(node.__repr__())

    copy_over(src, dest)

    generate_pages_recursive(content_src, template, content_dest)


main()