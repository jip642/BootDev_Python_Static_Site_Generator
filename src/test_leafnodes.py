import unittest
from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        leaf_node = LeafNode("h1", "Hello, world!")
        self.assertEqual(leaf_node.to_html(), "<h1>Hello, world!</h1>")
        leaf_node = LeafNode("p", "Hello, world!")
        self.assertEqual(leaf_node.to_html(), "<p>Hello, world!</p>")
        leaf_node = LeafNode("a", "Hello, world!", {"href": "https://www.google.com"})
        self.assertEqual(leaf_node.to_html(), '<a href="https://www.google.com">Hello, world!</a>')
        leaf_node = LeafNode("p", "Hello, world!", {"class": "bold"})
        self.assertEqual(leaf_node.to_html(), '<p class="bold">Hello, world!</p>')


if __name__ == "__main__":
    unittest.main()