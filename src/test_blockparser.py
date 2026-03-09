import unittest
from blockparser import markdown_to_blocks

class TestBlockParser(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )
    
    def test_markdown_to_blocks_single_block(self):
        md = """
This is a single paragraph with no breaks
    """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is a single paragraph with no breaks",
            ],
        )

    def test_markdown_to_blocks_multiple_paragraphs(self):
        md = """
First paragraph

Second paragraph

Third paragraph
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "First paragraph",
                "Second paragraph",
                "Third paragraph",
            ],
        )


    def test_markdown_to_blocks_extra_blank_lines(self):
        md = """

First paragraph


Second paragraph


"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "First paragraph",
                "Second paragraph",
            ],
        )


    def test_markdown_to_blocks_extra_blank_lines(self):
        md = """

First paragraph


Second paragraph


"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "First paragraph",
                "Second paragraph",
            ],
        )

    def test_markdown_to_blocks_list_block(self):
        md = """
- Item one
- Item two
- Item three

Paragraph after list
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "- Item one\n- Item two\n- Item three",
                "Paragraph after list",
            ],
        )