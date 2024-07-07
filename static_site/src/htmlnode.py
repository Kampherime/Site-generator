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
        if self.props == None:
            return return_string
        for key, value in self.props.items():
            return_string += f" {key}={value}"
        return return_string.strip()

    def __repr__(self):
        print(f"HTML Tag: {self.tag}, Value: {self.value}, Children: {self.children}, Properties: {self.props}")

    def __eq__(self, other):
        if self.tag == other.tag and self.value == other.value and self.children == other.children and self.props == other.props:
            return True
        return False
