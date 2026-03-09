import textnode

def main():
    node = textnode.TextNode("This is some anchor text", "link", "https://boot.dev")
    print(node.__repr__())

main()