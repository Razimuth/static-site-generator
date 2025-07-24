import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This tests TextType equality", TextType.BOLD)
        node2 = TextNode("This tests TextType equality", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This tests TextType equality", TextType.ITALIC)
        node2 = TextNode("This tests TextType equality", TextType.BOLD)
        self.assertNotEqual(node, node2)
 
    def test_not_eq_2(self):
        node = TextNode("This tests text here", TextType.TEXT)
        node2 = TextNode("This tests text now", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This tests link url", TextType.LINK, "http://localhost:8888")
        node2 = TextNode("This tests link url", TextType.LINK, "http://localhost:8888")
        self.assertEqual(node, node2)

    def test_not_eq_url(self):
        node = TextNode("This tests link url", TextType.LINK, "http://localhost:8888")
        node2 = TextNode("This tests link url", TextType.LINK, "http://localhost:7777")
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = TextNode("This tests repr", TextType.LINK, "http://localhost:8888")
        self.assertEqual(
            "TextNode(This tests repr, link, http://localhost:8888)", repr(node)
        )


if __name__ == "__main__":
    unittest.main()
