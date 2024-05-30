class TextNode:
    def __init__(self, text, text_type, url = None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, diff):
        return self.text == diff.text and self.text_type == diff.text_type and self.url == diff.url

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
    
    