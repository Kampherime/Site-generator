from TheBeast import split_delimiter, split_by_images, split_by_links
from textnode import TextNode
from THE_ENTITY import text_to_textnodes
import unittest


class testTheLoser(unittest.TestCase):
    def test_if_it_even_works(self):
        node1 = TextNode("Okay so we're going to try this with the `code` delimiter. ", "text", None)
        # not going to do anything with it im just going to be amazed if it works at all
        try: 
            ohmygod = split_delimiter([node1], '`', "code")
            print("holy sh** it worked")
            print(ohmygod)
        except Exception as e: 
            print(f"yeah thats exactly what i hugging expected: {e}")

    def test_some_other_things(self):       
        node2 = TextNode("So we're going to keep trying with **two bold** and another **bold** one", "text", None)
        try:
            maybe = split_delimiter([node2], '**', "bold")
            print("it worked!!!")
            print("ITS THIS ONE")
            print(maybe)
        except Exception as e:
            print(f"IT DIDNT WORK BUT ITS THIS ONE: {e}")

    def test_edge_cases(self):
        try:
            node3 = TextNode("We're going to create *bad markdown syntax", "text", None)
            split_delimiter([node3], '*', "italic")
        except SyntaxError as e:
            print(f"Working as expected: {e}")
        except Exception as e:
            print(f"Not working as expected: {e}")

    def test_multiple_nodes(self):
        node1 = TextNode("Okay so we're going to try this with the **not code** delimiter. ", "text", None)
        node2 = TextNode("So we're going to keep trying with **two bold** and another **bold** one", "text", None)
        node3 = TextNode("We're going to create **bad markdown syntax", "text", None)

        try: 
            split_delimiter([node1, node2, node3], "**", "bold")
        except SyntaxError as e:
            print(f"Expected syntax Error: {e}")
        except Exception as e:
            print(f"Unexpected exception: {e}")

        print("-----------------------------------")

        print("this one should work")
        split_delimiter([node1, node2], "**", "bold")
    
    def test_split_images(self):
        node1 = TextNode("Now we have to do something a little bit annoying. I'm going to write a paragraph where I include links to ![images](https://static.zerochan.net/Satanick.full.2589552.jpg) and links to [links](https://www.example.com/), then I have to include another example of an ![image](https://pm1.narvii.com/7464/ae3f1a47480bb1abe8fe81b8ba31ef6cd272b82dr1-720-719v2_hq.jpg) and another example of a [link :3](https://www.google.com/) to make sure everything works right. I'll test both before anything else", "text", None)
        try:
            print("LOOK HERE ---------------------------------------------------")
            split_node = split_by_images([node1])
            print(split_node)
            split_node_2 = split_by_links([node1])
            print("---------------------------------")
            print(f"second node {split_node_2}")
            print("LOOK HERE ---------------------------------------------------")
        except Exception as e:
            print(f"Error parsing image: {e}")
    
    def test_finishing_this(self):
        node1 = TextNode("These are literally just words", "text", None)
        try:
            split_node_1 = split_by_images([node1])
            split_node_2 = split_by_links([node1])
            print(split_node_1)
            print(split_node_2)
        except Exception as e:
            print(f"Error with extracting NOTHING. {e}")
        
        try: 
            node2 = TextNode("", "text", None)
            node3 = TextNode("`code block`", "code", None)
            node4 = TextNode("MORE WORDS YAY", "text", None)
            node5 = TextNode("we're testing this with a [link](https://www.google.com/) imbedded innit", "text", None)
            
            split_nodes = split_by_images([node2, node3, node4, node5])
            split_nodes_2 = split_by_links([node2, node3, node4, node5])
            print("UGHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH")
            print(split_nodes)
            print(split_nodes_2)

        except Exception as e:
            print(f"failed to wonkadoodledoo {e} (I'm so not lucid)")

    def test_text_to_textnode(self):
        test_paragraph = "This is **text** with an *italic* word and a `code block` and an ![image](https://pm1.narvii.com/6453/55ddf8e7cb11617199526c66bbcab69f9196d338_hq.jpg) and a [link](https://www.google.com/)"
        test_paragraph_2 = "2nd paragraph. *Italic*, **bold**, and `monospace`. Itemized lists look like:"
        test_paragraph_3 = '![example image](example-image.jpg "An exemplary image")'
        
        try:
            print(text_to_textnodes(test_paragraph))
            print(text_to_textnodes(test_paragraph_2))
            print(text_to_textnodes(test_paragraph_3))
        except Exception as e:
            print(f"Failed to generate text from textnodes, because of a: {e}")

