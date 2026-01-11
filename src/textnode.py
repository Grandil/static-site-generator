from enum import Enum

class TextType(Enum):
    PLAIN = 1 #text (plain)
    BOLD = 2 #**Bold text**
    ITALIC = 3 #_Italic text_
    CODE = 4 #`Code text`
    LINK = 5 #Links, in this format: [anchor text](url)
    IMAGE = 6 #Images, in this format: ![alt text](url)

class TextNode():
    def __init__(self, text: str, text_type: 'TextType', url: str = None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return (
            self.text == other.text
            and self.text_type == other.text_type
            and self.url == other.url
        )
    
    def __repr__(self):
        return f"TextNode({self.text!r}, {self.text_type.value!r}, {self.url!r})"