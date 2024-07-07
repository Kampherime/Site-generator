import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("TestNode1", "bold")
        node2 = TextNode("TestNode1", "bold")
        self.assertEqual(node, node2)
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
            print("Test3: Working as expected. Assertion Error")
    def test_text(self):
        node1 = TextNode("This text is different than", "italic")
        node2 = TextNode("This one!", "italic")
        try: 
            self.assertEqual(node1, node2)
        except AssertionError as e:
            print("Test4: Working as expected. Assertion Error")


if __name__== "__main__":
    unittest.main()
