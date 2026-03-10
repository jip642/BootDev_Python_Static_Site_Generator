from parentnode import ParentNode
from inlineparser import text_to_textnodes
from textnode import TextNode
from sitetypes import BlockType, TextType
from blockparser import markdown_to_blocks, block_to_block_type
from classifiers import text_node_to_html_node


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []

    for block in blocks:
        block_type = block_to_block_type(block)

        if block_type == BlockType.PARAGRAPH:
            children.append(paragraph_to_html(block))

        elif block_type == BlockType.HEADING:
            children.append(heading_to_html(block))

        elif block_type == BlockType.CODE:
            children.append(code_to_html(block))

        elif block_type == BlockType.QUOTE:
            children.append(quote_to_html(block))

        elif block_type == BlockType.UNORDERED_LIST:
            children.append(unordered_list_to_html(block))

        elif block_type == BlockType.ORDERED_LIST:
            children.append(ordered_list_to_html(block))

    return ParentNode("div", children)


def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    return [text_node_to_html_node(n) for n in text_nodes]

def paragraph_to_html(block):
    text = block.replace("\n", " ")
    children = text_to_children(text)
    return ParentNode("p", children)

def heading_to_html(block):
    level = len(block) - len(block.lstrip("#"))
    text = block[level + 1 :]
    children = text_to_children(text)
    return ParentNode(f"h{level}", children)

def code_to_html(block):
    lines = block.split("\n")[1:-1]
    text = "\n".join(lines)

    text_node = TextNode(text, TextType.CODE)
    code_child = text_node_to_html_node(text_node)

    return ParentNode("pre", [ParentNode("code", [code_child])])

def quote_to_html(block):
    lines = block.split("\n")
    stripped = [line.lstrip("> ").strip() for line in lines]
    text = " ".join(stripped)

    children = text_to_children(text)
    return ParentNode("blockquote", children)

def unordered_list_to_html(block):
    lines = block.split("\n")
    items = []

    for line in lines:
        text = line[2:]
        items.append(ParentNode("li", text_to_children(text)))

    return ParentNode("ul", items)

def ordered_list_to_html(block):
    lines = block.split("\n")
    items = []

    for line in lines:
        text = line.split(". ", 1)[1]
        items.append(ParentNode("li", text_to_children(text)))

    return ParentNode("ol", items)

