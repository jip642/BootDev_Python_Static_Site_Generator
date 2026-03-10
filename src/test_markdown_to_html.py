import unittest
from markdown_to_html import markdown_to_html_node

class TestMarkdownToHTML(unittest.TestCase):

    def test_paragraph(self):
        md = "Hello world"
        node = markdown_to_html_node(md)

        self.assertEqual(node.tag, "div")
        self.assertEqual(node.children[0].tag, "p")


    def test_heading(self):
        md = "# Heading"
        node = markdown_to_html_node(md)

        self.assertEqual(node.children[0].tag, "h1")


    def test_code_block(self):
        md = "```\nprint('hello')\n```"
        node = markdown_to_html_node(md)

        self.assertEqual(node.children[0].tag, "pre")


    def test_quote(self):
        md = "> quote line"
        node = markdown_to_html_node(md)

        self.assertEqual(node.children[0].tag, "blockquote")


    def test_unordered_list(self):
        md = "- one\n- two"
        node = markdown_to_html_node(md)

        self.assertEqual(node.children[0].tag, "ul")
        self.assertEqual(len(node.children[0].children), 2)


    def test_ordered_list(self):
        md = "1. one\n2. two"
        node = markdown_to_html_node(md)

        self.assertEqual(node.children[0].tag, "ol")