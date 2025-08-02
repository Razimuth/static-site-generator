import unittest
from blocks import BlockType, block_to_block_type
from markdown_to_html import markdown_to_html_node
    
class TestBlockTypes(unittest.TestCase):
    def test_paragraph(self):
        markdown = "This is a paragraph block test"
        block = block_to_block_type(markdown)
        self.assertEqual(BlockType.PARAGRAPH, block)

    def test_heading1(self):
        markdown = "# This is a h1 headding block test."
        block = block_to_block_type(markdown)
        self.assertEqual(BlockType.HEADING, block)

    def test_heading2(self):
        markdown = "## This is a h2 headding block test."
        block = block_to_block_type(markdown)
        self.assertEqual(BlockType.HEADING, block)

    def test_heading3(self):
        markdown = "### This is a h3 headding block test."
        block = block_to_block_type(markdown)
        self.assertEqual(BlockType.HEADING, block)

    def test_heading4(self):
        markdown = "#### This is a h4 headding block test."
        block = block_to_block_type(markdown)
        self.assertEqual(BlockType.HEADING, block)

    def test_heading5(self):
        markdown = "##### This is a h5 headding block test."
        block = block_to_block_type(markdown)
        self.assertEqual(BlockType.HEADING, block)

    def test_heading6(self):
        markdown = "###### This is a h6 headding block test."
        block = block_to_block_type(markdown)
        self.assertEqual(BlockType.HEADING, block)

    def test_code(self):
        markdown = "```This is a code block test.\n```This is second line of a code block."
        block = block_to_block_type(markdown)
        self.assertEqual(BlockType.CODE, block)

    def test_quote(self):
        markdown = ">This is a quote block test.\n>This is second line of a quote block."
        block = block_to_block_type(markdown)
        self.assertEqual(BlockType.QUOTE, block)

    def test_unordered_list(self):
        markdown = "- This is an unordered list block test.\n- This is second line of an unordered lsy block."
        block = block_to_block_type(markdown)
        self.assertEqual(BlockType.UNORDERED_LIST, block)

    def test_ordered_list(self):
        markdown = "1. This is an ordered list block test.\n2. This is second line of an ordered list block."
        block = block_to_block_type(markdown)
        self.assertEqual(BlockType.ORDERED_LIST, block)


    def test_block_paragraph(self):
        text = """
This is **bolded** paragraph text in a p tag here

This is another paragraph with _italic_ text and `code` here

"""
        node = markdown_to_html_node(text)
        
 #       print(f"parentnode {node}")
        
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
         )

    def test_paragraph(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p></div>",
        )

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_lists(self):
        md = """
- This is a list
- with items
- and _more_ items

1. This is an `ordered` list
2. with items
3. and more items

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is a list</li><li>with items</li><li>and <i>more</i> items</li></ul><ol><li>This is an <code>ordered</code> list</li><li>with items</li><li>and more items</li></ol></div>",
        )

    def test_headings(self):
        md = """
# this is an h1

this is paragraph text

## this is an h2
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>this is an h1</h1><p>this is paragraph text</p><h2>this is an h2</h2></div>",
        )

    def test_blockquote(self):
        md = """
> This is a
> blockquote block

this is paragraph text

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a blockquote block</blockquote><p>this is paragraph text</p></div>",
        )

    def test_code(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )


if __name__ == "__main__":
    unittest.main()
