import unittest

from textnode import TextNode, TextType, text_node_to_html_node

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
            "TextNode(This tests repr, link, http://localhost:8888)", repr(node) )

class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("This is a bold node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a bold node")

    def test_italic(self):
        node = TextNode("This is an italic node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is an italic node")

    def test_link(self):
        node = TextNode("This is a link node", TextType.LINK, "https://www.google.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a link node")
        self.assertEqual(html_node.props, { "href": "https://www.google.com" } ) 
        
    def test_image(self):
        node = TextNode("This is an image", TextType.IMAGE, "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, { "src": "https://www.boot.dev", "alt": "This is an image"} )


if __name__ == "__main__":
    unittest.main()
