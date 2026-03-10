import os
import sys
import textnode
from copyover import copy_over
from generatepage import generate_pages_recursive

src = os.path.join(os.getcwd(), "static")
dest = os.path.join(os.getcwd(), "../docs")
content_src = os.path.join(os.getcwd(), "content")
template = os.path.join(os.getcwd(), "template.html")
content_dest = os.path.join(os.getcwd(), "docs")

def main():
    basepath = sys.argv[1] if len(sys.argv) > 1 else "/"
    if not basepath.startswith("/"):
        basepath = "/" + basepath
    if not basepath.endswith("/"):
        basepath = basepath + "/"

    node = textnode.TextNode("This is some anchor text", "link", "https://boot.dev")
    print(node.__repr__())

    copy_over(src, dest)

    generate_pages_recursive(content_src, template, content_dest, basepath=basepath)


main()
