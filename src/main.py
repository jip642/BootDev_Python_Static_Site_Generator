import os
import textnode
from copyover import copy_over

src = os.path.join(os.getcwd(), "static")
dest = os.path.join(os.getcwd(), "public")

def main():
    node = textnode.TextNode("This is some anchor text", "link", "https://boot.dev")
    print(node.__repr__())

    copy_over(src, dest)

main()