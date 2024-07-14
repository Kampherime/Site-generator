from htmlnode import LeafNode


class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    def __eq__(self, node):
        if self.text == node.text and self.text_type == node.text_type and self.url == node.url:
            return True
        return False

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"

    
    def text_node_to_html_node(self):
        match(self.text_type):
            case("text"):
                return LeafNode(None, self.text)
            case("bold"):
                return LeafNode("b", self.text)
            case("italic"):
                return LeafNode("i", self.text)
            case("code"):
                return LeafNode("code", self.text)
            case("link"):
                return LeafNode("a", self.text, {"href": self.url})
            case("image"):
                return LeafNode("img", "", {"src": self.url, "alt": self.text})
            case _:
                raise Exception("Invalid TextNode Type")


'''going to list the types of nodes:
    htmlnode: tag, value, children, props
    leafnode: tag, value, props
    parentnode: tag, children, props'''

