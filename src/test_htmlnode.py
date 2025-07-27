import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_not_eq(self):
        node = HTMLNode("p", "This is a paragraph tag", ["child1", "child2"], {"href": "https://www.google.com", "target": "_blank",})
        node2 = HTMLNode("a", "This is a paragraph tag", ["child1", "child2"], {"href": "https://www.google.com", "target": "_blank",})
        self.assertNotEqual(node, node2)
 
    def test_not_eq_2(self):
        node = HTMLNode("p", "This is a paragraph tag", ["child1", "child2"], {"href": "https://www.google.com", "target": "_blank",})
        node2 = HTMLNode("p", "This is a tag", ["child1", "child2"], {"href": "https://www.google.com", "target": "_blank",})
        self.assertNotEqual(node, node2)

    def test_props_to_html(self):
        node = HTMLNode("p", "This is a paragraph tag", ["child1", "child2"], {"href": "https://www.google.com", "target": "_blank",})
        actual = node.props_to_html()
        self.assertEqual(' href="https://www.google.com" target="_blank"', actual)

    def test_values(self):
        node = HTMLNode("p", "This is a paragraph tag", ["child1", "child2"], {"href": "https://www.google.com", "target": "_blank",})
        self.assertEqual(node.tag, "p",)
        self.assertEqual(node.value, "This is a paragraph tag",)
        self.assertEqual(node.children, ["child1", "child2"],)
        self.assertEqual(node.props, {"href": "https://www.google.com", "target": "_blank",})

    def test_repr(self):
        node = HTMLNode("p", "This is a paragraph tag", None, {"href": "https://www.google.com", "target": "_blank",})
        actual = node.__repr__()
        self.assertEqual("HTMLNode(p, This is a paragraph tag, children: None, {'href': 'https://www.google.com', 'target': '_blank'})", actual)

class TestToHTML(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_b(self):
        node = LeafNode("b", "Hello, world!")
        self.assertEqual(node.to_html(), "<b>Hello, world!</b>")

    def test_leaf_to_html_i(self):
        node = LeafNode("i", "Hello, world!")
        self.assertEqual(node.to_html(), "<i>Hello, world!</i>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span><b>grandchild</b></span></div>")

    def test_to_html_multichildre(self):
        node = ParentNode("p", [LeafNode("b", "Bold text"), LeafNode(None, "Normal text"),
                                LeafNode("i", "Italic text"), LeafNode(None, "Normal text"), ])
        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>Italic text</i>Normal text</p>")

    def test_to_html_enbeddedchildre(self):
        node = ParentNode("p", [LeafNode("b", "Bold text"), ParentNode("p", [LeafNode(None, "Normal text")]),
                                LeafNode("i", "Italic text"), LeafNode(None, "Normal text"), ])
        self.assertEqual(node.to_html(), "<p><b>Bold text</b><p>Normal text</p><i>Italic text</i>Normal text</p>")

    def test_to_html_headings(self):
        node = ParentNode("h1", [LeafNode("b", "Bold text"), LeafNode(None, "Normal text"),
                                LeafNode("i", "Italic text"), LeafNode(None, "Normal text"), ])
        self.assertEqual(node.to_html(), "<h1><b>Bold text</b>Normal text<i>Italic text</i>Normal text</h1>")


if __name__ == "__main__":
    unittest.main()
