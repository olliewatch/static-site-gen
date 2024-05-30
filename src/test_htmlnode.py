import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_no_props(self):
        node = HTMLNode()
        self.assertEqual(node.props_to_html(), '', "Failed for no properties")

    def test_single_prop(self):
        node = HTMLNode(props={"href": "https://www.google.com"})
        result = node.props_to_html()
        self.assertEqual(result, ' href="https://www.google.com"', "Failed for a single property")

    def test_multiple_props(self):
        node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
        result = node.props_to_html()
        expected = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(result, expected, "Failed for multiple properties")

if __name__ == '__main__':
    unittest.main()
    print("All tests passed!")
