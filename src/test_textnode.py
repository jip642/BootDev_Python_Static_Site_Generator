import unittest
from textnode import TextNode
from sitetypes import TextType

class TestTextNode(unittest.TestCase):
    def test_uq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

        node3 = TextNode("This is a text node", TextType.BOLD, None)
        node4 = TextNode("This is a text node", TextType.BOLD, None)
        self.assertEqual(node3, node4)

        node5 = TextNode("This is a text node", TextType.BOLD, "https://boot.dev")
        node6 = TextNode("This is a text node", TextType.BOLD, "https://boot.dev")
        self.assertEqual(node5, node6)

        node7 = TextNode("This is a text node", TextType.BOLD, "https://boot.dev")
        node8 = TextNode("This is a text node", TextType.BOLD, "https://boot.dev")
        self.assertEqual(node7, node8)

        self.assertEqual(node, node3)
        self.assertNotEqual(node, node5)

if __name__ == "__main__":
    unittest.main()
