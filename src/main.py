from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode

def main():
    textnode = TextNode("Hello World", TextType.LINK, "http://localhost:8888")

    print(textnode)

    
    
    
if __name__ == "__main__":
        main()