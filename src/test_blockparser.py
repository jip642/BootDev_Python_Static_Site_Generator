import unittest
from blockparser import markdown_to_blocks, block_to_block_type
from sitetypes import BlockType

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