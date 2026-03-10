import os
import sys
import textnode
from copyover import copy_over
from generatepage import generate_pages_recursive

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
src = os.path.join(project_root, "static")
content_src = os.path.join(project_root, "content")
template = os.path.join(project_root, "template.html")
output_dir = os.path.join(project_root, "docs")

def main():
    basepath = sys.argv[1] if len(sys.argv) > 1 else "/"
    if not basepath.startswith("/"):
        basepath = "/" + basepath
    if not basepath.endswith("/"):
        basepath = basepath + "/"

    node = textnode.TextNode("This is some anchor text", "link", "https://boot.dev")
    print(node.__repr__())

    copy_over(src, output_dir)

    generate_pages_recursive(content_src, template, output_dir, basepath=basepath)


main()
