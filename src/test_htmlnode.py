import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("div", "This is a div", [], {"class": "container"})
        node2 = HTMLNode("div", "This is a div", [], {"class": "container"})
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = HTMLNode("div", "This is a div", [], {"class": "container"})
        node2 = HTMLNode("div", "This is a div", [], {"class": "container-fluid"})
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = HTMLNode("p", "Paragraph", [], {"style": "color: red;"})
        expected_repr = "HTMLNode(tag=p, value=Paragraph, children=[], props={'style': 'color: red;'})"
        self.assertEqual(repr(node), expected_repr)

    def test_props_to_html(self):
        node = HTMLNode("a", "Link", [], {"href": "https://example.com", "target": "_blank"})
        expected_html = ' href="https://example.com" target="_blank"'
        self.assertEqual(node.props_to_html(), expected_html)

if __name__ == "__main__":
    unittest.main()