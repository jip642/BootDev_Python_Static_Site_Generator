import unittest
from textnode import TextNode
from sitetypes import TextType
from inlineparser import (
    split_nodes_delimiter,
    extract_markdown_images, 
    extract_markdown_links,
    split_nodes_image,
    split_nodes_link,
    text_to_textnodes
    )


class TestParser(unittest.TestCase):
#### Test Main Parser Function
    # 1️⃣ basic code split
    def test_split_code(self):
        node = TextNode("This is `code` text", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" text", TextType.TEXT),
        ]

        self.assertEqual(new_nodes, expected)

    # 2️⃣ bold split
    def test_split_bold(self):
        node = TextNode("Hello **world**!", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)

        expected = [
            TextNode("Hello ", TextType.TEXT),
            TextNode("world", TextType.BOLD),
            TextNode("!", TextType.TEXT),
        ]

        self.assertEqual(new_nodes, expected)

    # 3️⃣ multiple delimiters
    def test_multiple_code_sections(self):
        node = TextNode("A `b` and `c` test", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

        expected = [
            TextNode("A ", TextType.TEXT),
            TextNode("b", TextType.CODE),
            TextNode(" and ", TextType.TEXT),
            TextNode("c", TextType.CODE),
            TextNode(" test", TextType.TEXT),
        ]

        self.assertEqual(new_nodes, expected)

    # 4️⃣ node not TEXT should remain unchanged
    def test_non_text_nodes_unchanged(self):
        node = TextNode("bold text", TextType.BOLD)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

        self.assertEqual(new_nodes, [node])

    # 5️⃣ unmatched delimiter should raise exception
    def test_unmatched_delimiter(self):
        node = TextNode("This is `broken text", TextType.TEXT)

        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "`", TextType.CODE)

    # 6️⃣ list with multiple nodes
    def test_multiple_nodes(self):
        nodes = [
            TextNode("Hello ", TextType.TEXT),
            TextNode("world", TextType.BOLD),
            TextNode(" `code` here", TextType.TEXT),
        ]

        new_nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)

        expected = [
            TextNode("Hello ", TextType.TEXT),
            TextNode("world", TextType.BOLD),
            TextNode(" ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" here", TextType.TEXT),
        ]

        self.assertEqual(new_nodes, expected)

    # 7️⃣ delimiter at beginning
    def test_delimiter_at_start(self):
        node = TextNode("`code` text", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

        expected = [
            TextNode("code", TextType.CODE),
            TextNode(" text", TextType.TEXT),
        ]

        self.assertEqual(new_nodes, expected)


#### Test Image Extraction Function
    def test_extract_single_image(self):
        text = "Here is an image ![cat](https://example.com/cat.png)"
        self.assertEqual(
        extract_markdown_images(text),
        [("cat", "https://example.com/cat.png")]
        )


    def test_extract_multiple_images(self):
        text = "![cat](cat.png) and ![dog](dog.jpg)"
        self.assertEqual(extract_markdown_images(text),[
            ("cat", "cat.png"),
            ("dog", "dog.jpg"),
        ])


    def test_extract_image_empty_alt(self):
        text = "Image: ![](image.png)"
        self.assertEqual(extract_markdown_images(text),[
            ("", "image.png")
        ])


    def test_extract_image_no_images(self):
        text = "This text has no images."
        self.assertEqual(extract_markdown_images(text),[])


    def test_extract_images_with_text_around(self):
        text = "Start ![logo](logo.svg) middle ![icon](icon.png) end"
        self.assertEqual(extract_markdown_images(text),[
            ("logo", "logo.svg"),
            ("icon", "icon.png"),
        ])

#### Test Link Extraction Function
    def test_extract_single_link(self):
        text = "Visit [Google](https://google.com)"
        self.assertEqual(extract_markdown_links(text),
        [
            ("Google", "https://google.com")
        ])


    def test_extract_multiple_links(self):
        text = "[OpenAI](https://openai.com) and [GitHub](https://github.com)"
        self.assertEqual(extract_markdown_links(text),
            [
                ("OpenAI", "https://openai.com"),
                ("GitHub", "https://github.com"),
            ])


    def test_extract_link_empty_text(self):
        text = "Check this [](https://example.com)"
        self.assertEqual(extract_markdown_links(text),
        [
            ("", "https://example.com")
        ])


    def test_extract_links_no_links(self):
        text = "There are no markdown links here."
        self.assertEqual(extract_markdown_links(text) ,[])


    def test_links_do_not_require_text_around(self):
        text = "[one](1.com) [two](2.com) [three](3.com)"
        self.assertEqual(extract_markdown_links(text),
        [
            ("one", "1.com"),
            ("two", "2.com"),
            ("three", "3.com"),
        ])

##### Test split_nodes_images(old_nodes)
#### Test Image Node Splitting

    def test_split_single_image(self):
        node = TextNode("Hello ![cat](cat.png) world", TextType.TEXT)

        result = split_nodes_image([node])

        expected = [
            TextNode("Hello ", TextType.TEXT),
            TextNode("cat", TextType.IMAGE, "cat.png"),
            TextNode(" world", TextType.TEXT),
        ]

        self.assertEqual(result, expected)


    def test_split_multiple_images(self):
        node = TextNode("A ![cat](cat.png) and ![dog](dog.jpg) test", TextType.TEXT)

        result = split_nodes_image([node])

        expected = [
            TextNode("A ", TextType.TEXT),
            TextNode("cat", TextType.IMAGE, "cat.png"),
            TextNode(" and ", TextType.TEXT),
            TextNode("dog", TextType.IMAGE, "dog.jpg"),
            TextNode(" test", TextType.TEXT),
        ]

        self.assertEqual(result, expected)


    def test_split_image_at_start(self):
        node = TextNode("![cat](cat.png) starts text", TextType.TEXT)

        result = split_nodes_image([node])

        expected = [
            TextNode("cat", TextType.IMAGE, "cat.png"),
            TextNode(" starts text", TextType.TEXT),
        ]

        self.assertEqual(result, expected)


    def test_split_image_at_end(self):
        node = TextNode("Text before ![cat](cat.png)", TextType.TEXT)

        result = split_nodes_image([node])

        expected = [
            TextNode("Text before ", TextType.TEXT),
            TextNode("cat", TextType.IMAGE, "cat.png"),
        ]

        self.assertEqual(result, expected)


    def test_split_no_images(self):
        node = TextNode("Just normal text", TextType.TEXT)

        result = split_nodes_image([node])

        expected = [
            TextNode("Just normal text", TextType.TEXT)
        ]

        self.assertEqual(result, expected)


##### Test split_nodes_link(old_nodes)
#### Test Link Node Splitting

    def test_split_single_link(self):
        node = TextNode("Visit [Google](google.com)", TextType.TEXT)

        result = split_nodes_link([node])

        expected = [
            TextNode("Visit ", TextType.TEXT),
            TextNode("Google", TextType.LINK, "google.com"),
        ]

        self.assertEqual(result, expected)


    def test_split_multiple_links(self):
        node = TextNode("[One](1.com) and [Two](2.com)", TextType.TEXT)

        result = split_nodes_link([node])

        expected = [
            TextNode("One", TextType.LINK, "1.com"),
            TextNode(" and ", TextType.TEXT),
            TextNode("Two", TextType.LINK, "2.com"),
        ]

        self.assertEqual(result, expected)


    def test_split_link_at_start(self):
        node = TextNode("[Google](google.com) is useful", TextType.TEXT)

        result = split_nodes_link([node])

        expected = [
            TextNode("Google", TextType.LINK, "google.com"),
            TextNode(" is useful", TextType.TEXT),
        ]

        self.assertEqual(result, expected)


    def test_split_link_at_end(self):
        node = TextNode("Search at [Google](google.com)", TextType.TEXT)

        result = split_nodes_link([node])

        expected = [
            TextNode("Search at ", TextType.TEXT),
            TextNode("Google", TextType.LINK, "google.com"),
        ]

        self.assertEqual(result, expected)


    def test_split_no_links(self):
        node = TextNode("Just plain text", TextType.TEXT)

        result = split_nodes_link([node])

        expected = [
            TextNode("Just plain text", TextType.TEXT)
        ]

        self.assertEqual(result, expected)




###### Test text_to_textnodes()
    def test_text_to_textnodes(self):
        text = "Hello **world**"
        result = text_to_textnodes(text)

        expected = [
            TextNode("Hello ", TextType.TEXT),
            TextNode("world", TextType.BOLD),
        ]

        self.assertEqual(result, expected)

#### Test Full Markdown Parsing Pipeline

    def test_text_to_textnodes_code(self):
        text = "This is `code` text"
        result = text_to_textnodes(text)

        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" text", TextType.TEXT),
        ]

        self.assertEqual(result, expected)


    def test_text_to_textnodes_bold(self):
        text = "Hello **world**"
        result = text_to_textnodes(text)

        expected = [
            TextNode("Hello ", TextType.TEXT),
            TextNode("world", TextType.BOLD),
        ]

        self.assertEqual(result, expected)


    def test_text_to_textnodes_italic(self):
        text = "This is _italic_ text"
        result = text_to_textnodes(text)

        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" text", TextType.TEXT),
        ]

        self.assertEqual(result, expected)


    def test_text_to_textnodes_image(self):
        text = "Look ![cat](cat.png)"
        result = text_to_textnodes(text)

        expected = [
            TextNode("Look ", TextType.TEXT),
            TextNode("cat", TextType.IMAGE, "cat.png"),
        ]

        self.assertEqual(result, expected)


    def test_text_to_textnodes_link(self):
        text = "Visit [Google](google.com)"
        result = text_to_textnodes(text)

        expected = [
            TextNode("Visit ", TextType.TEXT),
            TextNode("Google", TextType.LINK, "google.com"),
        ]

        self.assertEqual(result, expected)


    def test_text_to_textnodes_mixed(self):
        text = "Text **bold** and _italic_ with `code`"
        result = text_to_textnodes(text)

        expected = [
            TextNode("Text ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" and ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" with ", TextType.TEXT),
            TextNode("code", TextType.CODE),
        ]

        self.assertEqual(result, expected)

    def test_text_to_textnodes_complex(self):
        text = "Hello **bold** ![img](img.png) and [link](url.com)"
        result = text_to_textnodes(text)

        expected = [
            TextNode("Hello ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" ", TextType.TEXT),
            TextNode("img", TextType.IMAGE, "img.png"),
            TextNode(" and ", TextType.TEXT),
            TextNode("link", TextType.LINK, "url.com"),
        ]

        self.assertEqual(result, expected)        

if __name__ == "__main__":
    unittest.main()