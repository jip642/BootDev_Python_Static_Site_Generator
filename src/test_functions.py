import unittest
from textnode import TextNode
from sitetypes import TextType
from functions import text_node_to_html_node


class TestTextToHTML(unittest.TestCase):
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

