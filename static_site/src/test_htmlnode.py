import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_equality(self):
        htmlnode_1 = HTMLNode("<p>", "hi hello hi")
        htmlnode_2 = HTMLNode("<p>", "hi hello hi")
        self.assertEqual(htmlnode_1, htmlnode_2)
    def test_props_to_html(self):
        htmlnode = HTMLNode("<p>", "hi hello hi", None, {"test1" : "testing", "test2": "testing"})
        print(htmlnode.props_to_html())
    def test_edge_cases(self):
        htmlnode = HTMLNode("<p>", "hi hello hello hello :3c", None, None)
        print(htmlnode.props_to_html())


if __name__ == "__main__":
    unittest.main()
