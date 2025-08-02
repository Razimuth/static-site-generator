import re
from textnode import TextNode, TextType, text_node_to_html_node

def split_nodes_delimiter(old_nodes, delimiter, text_type): 
    # ex  TextNode("This is a **bold block** node", TextType.TEXT))
    new_nodes = []
    for node in old_nodes:   # text, text_type, url=None):
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
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

def extract_markdown_images(text):
    regex_exp = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(regex_exp, text)
    return matches

def extract_markdown_links(text):
    regex_exp = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(regex_exp, text)
    return matches

def split_nodes_image(old_nodes):
     # ex  TextNode("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
    new_nodes = []
    for node in old_nodes:   # text, text_type, url=None):
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        split_nodes = []
        regex_exp = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
        splits = re.split(regex_exp, node.text,)
        matches = extract_markdown_images(node.text)
        for split in splits:
            for tuple in matches:
                if len(tuple) != 2:
                    raise ValueError("invalid markdown, image section not closed")
                if split == tuple[0] or split == tuple[1]:
                    if split == tuple[0]:
                        split_nodes.append(TextNode(split, TextType.IMAGE, tuple[1]))
                    split = ""
                    break # stop for loop
            if split != "":
                split_nodes.append(TextNode(split, TextType.TEXT))
        new_nodes.extend(split_nodes)
    return new_nodes
                                
def split_nodes_link(old_nodes):
    # ex   TextNode("This is a link node", TextType.LINK, "https://www.google.com")
    new_nodes = []
    for node in old_nodes:   # text, text_type, url=None):
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        split_nodes = []
        regex_exp = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
        splits = re.split(regex_exp, node.text,)
        matches = extract_markdown_links(node.text)
        for split in splits:
            for tuple in matches:
                if len(tuple) != 2:
                    raise ValueError("invalid markdown, link section not closed")
                if split == tuple[0] or split == tuple[1]:
                    if split == tuple[0]:
                        split_nodes.append(TextNode(split, TextType.LINK, tuple[1]))
                    split = ""
                    break # stop for loop
            if split != "":
                split_nodes.append(TextNode(split, TextType.TEXT))
        new_nodes.extend(split_nodes)
    return new_nodes

def text_to_textnodes(text):
    new_nodes = [TextNode(text, TextType.TEXT)]
    new_nodes = split_nodes_delimiter(new_nodes, "**" , TextType.BOLD) 
    new_nodes = split_nodes_delimiter(new_nodes, "_" , TextType.ITALIC)
    new_nodes = split_nodes_delimiter(new_nodes, "`" , TextType.CODE)
    new_nodes = split_nodes_image(new_nodes)
    new_nodes = split_nodes_link(new_nodes)
#    print(f"\n")
#    for node in new_nodes:
#        print(f"{node}\n")
    return new_nodes

def markdown_to_blocks(markdown):
#    text = "Block 1, Line 1\nBlock 1, Line 2\n\nBlock 2, Line 1\nBlock 2, Line 2  \n\nBlock 3, Line 1"
    blocks = markdown.split('\n\n')
    new_blocks = []
    for block in blocks:
        if block == "":
            continue
        strip_lines = block.strip()    #lstrip().rstrip(" \t\r\f\v")
        new_blocks.append(strip_lines)

#    print('\n')
#    for block in new_blocks:
#        print(f"{block}\n")
    return new_blocks




"""
    blocks = markdown.split('\n\n')
    new_blocks = []
    for block in blocks:
        lines = block.splitlines(keepends=True)
        strip_lines = [line.strip() for line in lines if line.strip()]
        if strip_lines:
            new_blocks.append(strip_lines)

    print('\n')
    for block in new_blocks:
        print(f"{block}\n")
    return new_blocks

"""
"""
def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        images = extract_markdown_images(original_text)
        if len(images) == 0:
            new_nodes.append(old_node)
            continue
        for image in images:
            sections = original_text.split(f"![{image[0]}]({image[1]})", 1)
            if len(sections) != 2:
                raise ValueError("invalid markdown, image section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(
                TextNode(
                    image[0],
                    TextType.IMAGE,
                    image[1],
                )
            )
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        links = extract_markdown_links(original_text)
        if len(links) == 0:
            new_nodes.append(old_node)
            continue
        for link in links:
            sections = original_text.split(f"[{link[0]}]({link[1]})", 1)
            if len(sections) != 2:
                raise ValueError("invalid markdown, link section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes

"""