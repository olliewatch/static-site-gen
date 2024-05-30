import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)
        
    def test_text_type(self):
        node = TextNode("This is a text node", "italic")
        node2 = TextNode("This is a text node", "bold")
        node3 = TextNode("This is a text node", "italic")
        self.assertNotEqual(node, node2)
        self.assertEqual(node, node3)
        
    def test_url(self):
        node = TextNode("This is a text node", "bold", "google.com")
        node2 = TextNode("This is a text node", "bold")
        node3 = TextNode("This is a text node", "bold", "google.com")
        node4 = TextNode("This is a text node", "bold", "bbc.com")
        self.assertNotEqual(node, node2)
        self.assertEqual(node, node3)
        self.assertNotEqual(node, node4)
        
    def test_repr(self):
        node = TextNode("This is a text node", "bold", "google.com")
        self.assertEqual("TextNode(This is a text node, bold, google.com)", repr(node))


if __name__ == "__main__":
    unittest.main()
    print("All tests passed!")
