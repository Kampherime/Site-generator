class HTMLNode:
    # Each of the properties defaults to none because there are cases for each.
    '''No tag infers raw text
    No value assumes children
    No children assumes value
    No props has no attributes'''

    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("Not yet implemented")

    def props_to_html(self):
        return_string = ""
        if self.props is None:
            return return_string
        for key, value in self.props.items():
            return_string += f" {key}={value}"
        return return_string.strip()

    def __repr__(self):
        print(f"HTML Tag: {self.tag}, Value: {self.value}, Children: {self.children}, Properties: {self.props}")

    def __eq__(self, other):
        if (self.tag == other.tag and self.value == other.value and
           self.children == other.children and self.props == other.props):
            return True
        return False


class LeafNode(HTMLNode):

    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
        if self.value is None:
            raise ValueError("LeafNodes cannot have no value")

    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode has no value")
        elif self.tag is None:
            return self.value
        elif self.props is None:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        else:
            prop_to_html = self.props_to_html()
            return f"<{self.tag} {prop_to_html}>{self.value}</{self.tag}>"


class ParentNode(HTMLNode):

    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
        if self.children is None:
            raise Exception("Parent nodes must have children (they're parent nodes (most parents have kids by definition...))")

    def to_html(self):
        if self.tag is None:
            raise ValueError("Tag must be provided for ParentNodes")
        if self.children is None:
            raise ValueError("ParentNodes must have children.")
        # trying to return a string representing the HTML tag of the node, and its children, recursively...
        # each recursion generating a new node instance.
        return_string = ""
        for child in self.children:
            return_string += child.to_html()
        if self.props is None:
            return f"<{self.tag}>{return_string}</{self.tag}>"
        return  f"<{self.tag} {self.props_to_html()}>{return_string}</{self.tag}>"

