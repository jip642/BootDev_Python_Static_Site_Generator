import re
from sitetypes import  TextType, BlockType
from leafnode import LeafNode

def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None, text_node.text)
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.LINK:
            return LeafNode( "a", text_node.text, "href")
        case TextType.IMAGE:
            return LeafNode("img", "",  {"src": text_node.url, "alt": text_node.text})
        case _:
            raise Exception("Type is not valid")


def block_to_block_type(block):

    lines = block.split("\n")

    # Heading
    if re.match(r"^#{1,6} ", block):
        return BlockType.HEADING

    # Code block
    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE

    # Quote block
    if all(line.startswith(">") for line in lines):
        return BlockType.QUOTE

    # Unordered list
    if all(line.startswith("- ") for line in lines):
        return BlockType.UNORDERED_LIST

    # Ordered list
    ordered = True
    for i, line in enumerate(lines):
        if not line.startswith(f"{i+1}. "):
            ordered = False
            break

    if ordered:
        return BlockType.ORDERED_LIST

    # Default
    return BlockType.PARAGRAPH