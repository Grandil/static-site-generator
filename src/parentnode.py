from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag: str, children: list, props: dict | None = None):
        super().__init__(tag, "", children, props)

    def to_html(self):
        
        if self.tag == "":
            raise ValueError("ParentNode must have a tag to convert to HTML")
        
        if self.children == [] or self.children == None:
            raise ValueError("ParentNode must have children")
        
        child_strings = ""
        for child in self.children:
            child_strings += child.to_html()

        #print(f"<{self.tag}{self.props_to_html()}>{child_strings}</{self.tag}>")
        return f"<{self.tag}{self.props_to_html()}>{child_strings}</{self.tag}>"