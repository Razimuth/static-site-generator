import re
from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import HTMLNode, LeafNode, ParentNode
from markdown import ( text_to_textnodes, markdown_to_blocks )
from blocks import BlockType, block_to_block_type


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        html_node = block_to_html_node(block)
        children.append(html_node)
    return ParentNode("div", children, None)


def block_to_html_node(block):
    block_type = block_to_block_type(block)
    if block_type == BlockType.PARAGRAPH:
        return paragraph_to_html_node(block)
    if block_type == BlockType.HEADING:
        return heading_to_html_node(block)
    if block_type == BlockType.CODE:
        return code_to_html_node(block)
    if block_type == BlockType.ORDERED_LIST:
        return olist_to_html_node(block)
    if block_type == BlockType.UNORDERED_LIST:
        return ulist_to_html_node(block)
    if block_type == BlockType.QUOTE:
        return quote_to_html_node(block)
    raise ValueError("invalid block type")


def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children


def paragraph_to_html_node(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p", children)


def heading_to_html_node(block):
    level = 0
    for char in block:
        if char == "#":
            level += 1
        else:
            break
    if level + 1 >= len(block):
        raise ValueError(f"invalid heading level: {level}")
    text = block[level + 1 :]
    children = text_to_children(text)
    return ParentNode(f"h{level}", children)


def code_to_html_node(block):
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError("invalid code block")
    text = block[4:-3]
    raw_text_node = TextNode(text, TextType.TEXT)
    child = text_node_to_html_node(raw_text_node)
    code = ParentNode("code", [child])
    return ParentNode("pre", [code])


def olist_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[3:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ol", html_items)


def ulist_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[2:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ul", html_items)


def quote_to_html_node(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("invalid quote block")
        new_lines.append(line.lstrip(">").strip())
    content = " ".join(new_lines)
    children = text_to_children(content)
    return ParentNode("blockquote", children)






"""
def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    list_parentnodes = []
    for block in blocks:
        block_type = block_to_block_type(block)
        match block_type:
#            case BlockType.HEADING:
#                new_htmlnode = heading_htmlnode(block)
#            case BlockType.CODE:
#                new_htmlnode = code_htmlnode(block)
#            case BlockType.QUOTE:
#                new_htmlnode = quote_htmlnode(block)
#            case BlockType.UNORDERED_LIST:
#                new_htmlnode = unordered_list_htmlnode(block)
#            case BlockType.ORDERED_LIST:
#                new_htmlnode = ordered_list_htmlnode(block)
            case BlockType.PARAGRAPH:
                new_parentnode = paragragh_htmlnode(block)
            case _:
                raise ValueError("Not a valid BlockType")
        list_parentnodes.append(new_parentnode)

    return ParentNode("div", list_parentnodes)

def text_to_children(text):
    pass


    
def paragragh_htmlnode(block):
    list_textnodes = []
    list_leafnodes = []
    block_list_leafnodes = []
    lines = block.split("\n")
#    print(f"num lines = {len(lines)}")

    #for line in lines:
    node = TextNode(block, TextType.TEXT)
#    print(node.text)

    list_textnodes = text_to_textnodes(node.text)
    for textnode in list_textnodes:
        list_leafnodes.append(text_node_to_html_node(textnode))
 
#    block_list_leafnodes.append(list_leafnodes)

#    print(f"block {list_leafnodes}")

    return ParentNode("p", list_leafnodes)






"""
"""
1. have parentnode with div tag,
2 markdown_to_blocks with children list of htmlnode blocks
3 each htmlnode for that block with tag of block
4 each htmlnode block has children list of lists of leafnodes 
5 split nodes creates list of textnodes of a textnode of type text_node_to_html_node
6 for each line of block, make as textnode text, use split_nodes and text_to_textnodes to make list of text_to_textnodes
7 use text_node_to_html_node for each textnode to convert to LeafNode
8 use to_html of leafnode to convert to html 
9 use         node = markdown_to_html_node(md)
              html = node.to_html()
10 ParentNode( div [LeafNode]




.. creates blocks

    test_markdown_to_blocks2(self):
        markdown_text = """
"""
# This is a heading

This is a paragraph of text. It has some **bold** and _italic_ words inside of it.

- This is the first list item in a list block
- This is a list item
- This is another list item
"""
"""        new_blocks = markdown_to_blocks(markdown_text)
        self.assertListEqual(
            [
            "# This is a heading",
            "This is a paragraph of text. It has some **bold** and _italic_ words inside of it.",
            "- This is the first list item in a list block\n- This is a list item\n- This is another list item",
            ], new_blocks,
        )

.. each line of block
use text_to_textnodes on each line to list of textnodes

use text_node_to_html_node on each textnode in list of text_to_textnodes to create leafnodes

this is paragraph line
put in textnode with TextType.TEXT
        node = TextNode(
            "This is **bold text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)",
            TextType.TEXT,
        )

run new_nodes = text_to_textnodes(node.text)
([
            TextNode("This is ", TextType.TEXT),
            TextNode("bold text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
            ], new_nodes,
now has list of textnodes stored as new_nodes
def text_node_to_html_node(text_node): #elf, text, text_type, url=None
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None, text_node.text) # (self, tag, value, props=None):
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.LINK:
            return LeafNode("a", text_node.text, { "href": text_node.url })
        case TextType.IMAGE:
            return LeafNode("img", "", { "src": text_node.url, "alt": text_node.text })
        case _:
run text_node_to_html_node on each textnode to create and return a leafnode 

append each leafnode to create a list of leafnodes for each line


       node = ParentNode("p", [LeafNode("b", "Bold text"), ParentNode("p", [LeafNode(None, "Normal text")]),
                                LeafNode("i", "Italic text"), LeafNode(None, "Normal text"), ])
        self.assertEqual(node.to_html(), "<p><b>Bold text</b><p>Normal text</p><i>Italic text</i>Normal text</p>")



def __init__(self, tag=None, value=None, children=None, props=None):
#   ParentNode("div",[ list of leafnodes created by text_to_html], props)    
    
    return ParentNode()

def heading_htmlnode(block):
    if block.startswith("# "):
        return HTMLNode("h1", )

def code_htmlnode(block):
  #  <pre> </pre>  used to keep unformatted text
    pass
def quote_htmlnode(block):
    pass
def unordered_list_htmlnode(block):
    pass
def ordered_list_htmlnode(block):
    pass
def paragraph_htmlnode(block):
    pass

def aaaaatext_node_to_html_node(text_node): #elf, text, text_type, url=None
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None, text_node.text) # (self, tag, value, props=None):
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.LINK:
            return LeafNode("a", text_node.text, { "href": text_node.url })
        case TextType.IMAGE:
            return LeafNode("img", "", { "src": text_node.url, "alt": text_node.text })
        case _:
            raise ValueError(f"Not a valid TextType: {text_node.text_type}")
"""
"""   some sample html
  
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ title }}</title>
</head>
<body>
    <h1>Welcome, {{ name }}!</h1>
    <p>This is a sample HTML page generated using Jinja2.</p>
    <ul>
        {% for item in items %}
        <li>{{ item }}</li>
        {% endfor %}
    </ul>
</body>
</html>
"""