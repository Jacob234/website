import unittest

from htmlnode import HTMLNode

"""
HTMLNode (tag, value, children, prompts):

tag (string): represents the HTML tag ("p", "a", "h1")
value (string): represents value
children (list of HTMLNode objects): representing children
prompts (dictionary of k-v pairs): represents attributes of HTML tag


An HTMLNode without a tag will just render as raw text
An HTMLNode without a value will be assumed to have children
An HTMLNode without children will be assumed to have a value
An HTMLNode without props simply won't have any attributes
"""


class TestHTMLNode(unittest.TestCase):

    def setUp(self):
        self.empty_node = HTMLNode()
        self.para_node = HTMLNode("p", "This is a paragraph")
        self.link_node = HTMLNode("a", "Click me", props={"href":"hi.com"})
        self.parent_node = HTMLNode("p", children=[self.para_node, self.link_node])


    
    
    def test_constructor(self):
        self.assertIsNone(self.empty_node.tag)
        self.assertEqual(self.para_node.tag, "p")
        self.assertEqual(self.link_node.value, "Click me")

    def test_props_to_html(self):
        self.assertEqual(self.empty_node.props_to_html(), "")
        self.assertEqual(self.para_node.props_to_html(), "")
        self.assertEqual(self.link_node.props_to_html(), ' href="hi.com"')

    def test_props_to_html_multiple_props(self):
        node = HTMLNode(props={"class": "btn", "id": "submit"})
        self.assertIn(' class="btn"', node.props_to_html())
        self.assertIn(' id="submit"', node.props_to_html())

    def test_repr(self):
        expected = "HTMLNode(tag='p', value='This is a paragraph', children=None, props=None)"
        self.assertEqual(repr(self.para_node), expected)

if __name__ == "__main__":
    unittest.main()