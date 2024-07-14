from TheBeast import split_delimiter
from textnode import TextNode
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


