import unittest
from htmlnode import HtmlNode

class TestHtmlNode(unittest.TestCase):
    def test_to_html(self):
        node = HtmlNode("div", "Hello World", None, {})
        self.assertEqual(node.props_to_html(), "")

        node2 = HtmlNode("p ", "Hello World", None, {"id": "test"})
        self.assertEqual(node2.props_to_html(), ' id="test"')

        node3 = HtmlNode("div", "Hello World", None, {"id": "test", "class": "test"})
        self.assertEqual(node3.props_to_html(), ' id="test" class="test"')

        node4 = HtmlNode("div", "Hello World", None, {"id": "test", "class": "test", "data-test": "test"})
        self.assertEqual(node4.props_to_html(), ' id="test" class="test" data-test="test"')

if __name__ == "__main__":
    unittest.main()
