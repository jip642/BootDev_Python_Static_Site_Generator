import unittest
from textnode import TextNode
from sitetypes import TextType, BlockType
from classifiers import text_node_to_html_node, block_to_block_type


class TestNodeTypes(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

        node2 = TextNode("This is bold text", TextType.BOLD)
        html_node2 = text_node_to_html_node(node2)
        self.assertEqual(html_node2.tag, "b")
        self.assertEqual(html_node2.value, "This is bold text")

        node3 = TextNode("This is a test image", TextType.IMAGE, "https://www.testiamge.com")
        html_node3 = text_node_to_html_node(node3)
        self.assertEqual(html_node3.tag, "img")
        self.assertEqual(html_node3.value, "")
        self.assertEqual(html_node3.props, {"src": "https://www.testiamge.com", "alt": "This is a test image"})




class TestBlockTypes(unittest.TestCase):

    def test_heading(self):
        block = "# Heading text"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)


    def test_paragraph(self):
        block = "This is a normal paragraph."
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)


    def test_code_block(self):
        block = "```\nprint('hello')\n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)


    def test_quote_block(self):
        block = ">This is a quote\n>Another quote line"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)


    def test_unordered_list(self):
        block = "- item one\n- item two\n- item three"
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)


    def test_ordered_list(self):
        block = "1. first\n2. second\n3. third"
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)


    def test_invalid_ordered_list(self):
        block = "1. first\n3. third"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)


    def test_multiline_paragraph(self):
        block = "This is a paragraph\nthat continues on another line."
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)