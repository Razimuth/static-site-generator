from enum import Enum
from htmlnode import HTMLNode, LeafNode, ParentNode

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"
    
class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type    
        self.url = url

    def __eq__(self, other):
        return (
            self.text == other.text 
            and self.text_type == other.text_type
            and self.url == other.url
        )
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    
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
            raise ValueError(f"Not a valid TextType: {text_node.text_type}")
         
def split_nodes_delimiter(old_nodes, delimiter, text_type): 
    # ex  TextNode("This is a **bold block** node", TextType.TEXT))
    new_nodes = []
    for node in old_nodes:   # text, text_type, url=None):
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        # node =  TextNode("This is a **bold block node", TextType.TEXT)
        split_nodes = []
        splits = node.text.split(delimiter)
        if len(splits) % 2 == 0:
            raise ValueError("Not valid markdown")
            continue
        for i in range(len(splits)):
            if splits[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(splits[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(splits[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes

"""
def split_nodes_delimiter(old_nodes, delimiter, text_type): 
    # ex  TextNode("This is a **bold block** node", TextType.TEXT))
    new_nodes = []
    split_nodes = []
    for node in old_nodes:   # text, text_type, url=None):
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
       #     print(f"new_nodes  {new_nodes}")
        else:
           # node =  TextNode("This is a **bold block node", TextType.TEXT)
            split_nodes = node.text.split(delimiter, 1)
            new_nodes.append(TextNode(split_nodes[0], node.text_type, node.url))
#            print(f"split_nodes  {split_nodes}")
            split_nodes = node.text.split(delimiter, 2)
            if len(split_nodes) == 2:
                raise Exception("Not valid markdown")
            else:
                new_nodes.append(TextNode(split_nodes[1], text_type, node.url))
                new_nodes.append(TextNode(split_nodes[2], node.text_type, node.url))
#            print(f"split_nodes  {split_nodes} splits {len(split_nodes)}")
#            print(f"new_nodes  {new_nodes}")
    return new_nodes
"""