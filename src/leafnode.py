from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag: str | None = None, value: str | None = None, props: dict | None = None):
        super().__init__(tag, value, [], props)

    def to_html(self):
        if self.value == None:
            raise ValueError("LeafNode value cannot be None")
        
        if self.tag == None:
            return self.value
        
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self) -> str:
        return f"LeafNode(tag={self.tag}, value={self.value}, props={self.props})"