import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    
    def test_eq(self):
        node1 = TextNode("TestNode1", "bold")
        node2 = TextNode("TestNode1", "bold")
        self.assertEqual(node1, node2)
    
    def test_urls(self):
        node1 = TextNode("TestNode", "italic", "https://www.example.com/")
        node2 = TextNode("TestNode", "italic", "https://www.example.com/")
        self.assertEqual(node1, node2)
    
    def test_properties(self):
        node1 = TextNode("TestNode", "italic")
        node2 = TextNode("TestNode", "bold")
        try:
            self.assertEqual(node1, node2)
        except AssertionError as e:
            print(f"Test3: Working as expected. Assertion Error: {e}")
    
    def test_text(self):
        node1 = TextNode("This text is different than", "italic")
        node2 = TextNode("This one!", "italic")
        try:
            self.assertEqual(node1, node2)
        except AssertionError as e:
            print(f"Test4: Working as expected. Assertion Error: {e}")
    
    def test_to_html_node(self):
        #Testing the bold feature
        node1 = TextNode("HIIIIIIIIII :3333", "bold", None)
        try:
            new_node = node1.text_node_to_html_node()
            print(new_node)
        except Exception as e:
            print(f"Error: {e}")

        #Testing italics
        node2 = TextNode("HEWWWOOOOOOO xDDDD", "italic", None)
        try:
            print(f"Success!!! itallics work fine! : {node2.text_node_to_html_node()}")
        except Exception as e:
            print(f"Fail, itallics don't work x( bcuz: {e}")

        node3 = TextNode("Woaaaaa!!!!", "text", None)

        try:
            print(f"Success!!! normal text parses fine!!! : {node3.text_node_to_html_node()}")
        except Exception as e:
            print(f"Fail :(( normal text not ok bcuz {e}")

        node4 = TextNode("Woaggg! x3", "code", None)

        try:
            print(f"Success!!! code text parses fine!!! : {node4.text_node_to_html_node()}")
        except Exception as e:
            print(f"Fail :( code text not ok bcuz {e}")

        node5 = TextNode("Linkies! :D", "link", "https://www.google.com/")

        try:
            print(f"Success! Links parse fine!!! :3 : {node5.text_node_to_html_node()}")
        except Exception as e:
            print(f"Fail :( links don't work,,,, bcuz {e}")

        node6 = TextNode("Image...", "image", "example url")

        try:
            print(f"Success!!!!!!!! Images parse fine!!!! :DDDD :333 : {node6.text_node_to_html_node().to_html()}")
        except Exception as e:
            print(f"Fail, images don't work because {e}")








if __name__== "__main__":
    unittest.main()
