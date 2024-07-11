import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    
    def test_equality(self):
        htmlnode_1 = HTMLNode("p", "hi hello hi")
        htmlnode_2 = HTMLNode("p", "hi hello hi")
        self.assertEqual(htmlnode_1, htmlnode_2)
    
    def test_props_to_html(self):
        htmlnode = HTMLNode("p", "hi hello hi", None, {"test1" : "testing", "test2": "testing"})
        print(htmlnode.props_to_html())
    
    def test_edge_cases(self):
        htmlnode = HTMLNode("p", "hi hello hello hello :3c", None, None)
        print(htmlnode.props_to_html())
    
    def test_leaf_node(self):
        test1 = LeafNode("p", "hewwo", None)
        print(f"LeafNode HTML: {test1.to_html()}")
        try:
            test2 = LeafNode(None, None, None)
        except ValueError as e:
            print(e)
        test3 = LeafNode("a", "link", {"href": '"https://www.google.com/"'})
        try:
            test4 = LeafNode(None, "testing children", "HTMLNode", None)
        except Exception as e:
            print(f"Functioning as intended. Exception: {e}")

        print(f"Testing links representation in HTML/Test3: {test3.to_html()}")
        test5 = LeafNode("a", "link2", ({"href": '"https://www.google.com/"', "test2": '"testing"'}))
        print(f"Testing to see if multiple properties function: {test5.to_html()}")
        
    def test_parent_node(self):
        test1 = ParentNode("p",
                           [
                               LeafNode("b", "text"),
                               LeafNode(None, "more text")
                            ], None)
        print(test1.to_html())
        test2 = ParentNode("div",
                           [
                               ParentNode("p",
                                          [
                                              LeafNode("b", "test"),
                                              LeafNode("p", "more test :3"),
                                              ParentNode("p", 
                                                         [
                                                            LeafNode("p", "Indents go crazy :P")
                                                        ])
                                              ]),
                                ParentNode("p", 
                                              [
                                              LeafNode("b", "Lets make it worse")
                                              ])
                                            ])
        print(f"Gods this is ugly: {test2.to_html()}")
        try:
            test3 = ParentNode("div", None, None)
            print(test3.to_html())
        except Exception as e:
            print(f"This one isn't as bad: {e}")

if __name__ == "__main__":
    unittest.main()
