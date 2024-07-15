# creating a function called "split_delimiter" that well... splits strings :3c 
# it'll accept an argument to split strings and convert them to inline html x)
from linksntwinks import extract_markdown_links, extract_markdown_images 
import re
from textnode import TextNode #might need?

# okay lets do a bit of planning here
# what needs to happen is texttype nodes need to be split and checked for inline text
# if the node is not texttype then were gonna just add it to a list
# if the node is texttype we split it based on the delimiter and append textnodes 


#textnode: self, text, text_type, url

#there are so many issues present with that function

#im going to take a break from coding but the issues ive seen are as follows:

#bold (**) doesn't work because the program checks for one character delimiters.

#it checks every word, and therefore it wouldn't work for things like `block block`

#there are probably more :/ 

#couple problems that i need to address now.

# How am I going to take care of bold letters? 

# i could do something like, if the delimiter is in the string, split it by that part at that point

# then if its in the string again, take the beginning and end and make them a ___ block 


def split_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes: 
        if node.text_type != "text" or delimiter not in node.text:
            new_nodes.append(node)
            continue
        split_text = node.text.split(delimiter, 1)
        if delimiter not in split_text[1]:
            raise SyntaxError("Invalid markdown syntax")
        new_nodes.append(TextNode(split_text[0], "text", None))
        # if there is a split, then the first and last nodes would be text
        appendable_node = split_text[1].split(delimiter, 1)
        new_nodes.append(TextNode(appendable_node[0], text_type, None))
        new_nodes.extend(split_delimiter([TextNode(appendable_node[1], "text", None)], delimiter, text_type))

    return(new_nodes)



def split_by_images(old_nodes):
    new_nodes = []
    for node in old_nodes:
        images = extract_markdown_images(node.text)
        if node.text_type != "text" or len(images) == 0:
            new_nodes.append(node)
            continue
        split_node = re.split(r'!\[(.*?)\]\((.*?)\)', node.text, 1)
        new_nodes.extend([TextNode(split_node[0], "text", None), TextNode(split_node[1], "image", split_node[2])])
        new_nodes.extend(split_by_images([TextNode(split_node[3], "text", None)]))
    return new_nodes        

def split_by_links(old_nodes):
    new_nodes = []
    for node in old_nodes:
        links = extract_markdown_links(node.text)
        if node.text_type != "text" or len(links) == 0:
            new_nodes.append(node)
            continue
        split_node = re.split(r' \[(.*?)\]\((.*?)\)', node.text, 1)
        new_nodes.extend([TextNode(split_node[0], "text", None), TextNode(f" {split_node[1]}", "link", split_node[2])])
        new_nodes.extend(split_by_links([TextNode(split_node[3], "text", None)]))
    return new_nodes        
