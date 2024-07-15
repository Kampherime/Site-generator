from linksntwinks import *
from TheBeast import *
from textnode import TextNode

def text_to_textnodes(text):
    #ugly
    nodes = split_delimiter(split_delimiter(split_delimiter(split_by_images(split_by_links([TextNode(text, "text", None)])), "**", "bold"), "*", "italic"), "`", "code")
    for node in nodes:
        if node.text == "":
            nodes.remove(node)
    return nodes


