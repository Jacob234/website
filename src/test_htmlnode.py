import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

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

"""
LeafNode (tag, value, props):

tag (string): represents the HTML tag ("p", "a", "h1")
value (string): represents value
props (dictionary of k-v pairs): represents attributes of HTML tag


A LeafNode without a tag will just render as raw text
A LeafNode must have value
A LeafNode without props simply won't have any attributes
"""


class TestLeafNode(unittest.TestCase):
    def setUp(self):
        self.empty_node = LeafNode(None, None, None)
        self.raw_leaf = LeafNode(tag = None, value = "raw text.", props = None)
        self.para_node = LeafNode("p", "This is a paragraph of text.", props=None)
        self.link_node = LeafNode("a", "Click me!", props={"href": "https://www.google.com"})


    def test_to_html(self):
        expected_para = "<p>This is a paragraph of text.</p>"
        expected_link = '<a href="https://www.google.com">Click me!</a>'

        self.assertEqual(self.para_node.to_html(), expected_para)
        self.assertEqual(self.link_node.to_html(), expected_link)

    def test_no_empty(self):
        with self.assertRaises(ValueError):
            self.empty_node.to_html()



class TestParentNode(unittest.TestCase):
    def setUp(self):
        
        self.raw_leaf = LeafNode(tag = None, value = "raw text.", props = None)
        self.para_leaf = LeafNode("p", "This is a paragraph of text.", props=None)
        self.link_leaf = LeafNode("a", "Click me!", props={"href": "https://www.google.com"})

        leaf_bundle = [self.raw_leaf, self.para_leaf, self.link_leaf]
        empty_bundle = None

        self.normal_parent = ParentNode("p", leaf_bundle, {"href": "https://www.google.com"})
        self.empty_parent = ParentNode("a", empty_bundle, {"href": "https://www.google.com"})

        self.parent_in_parent = ParentNode("p", [self.normal_parent], None)
        


    def test_provided(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")


    def test_normal_parent(self):
        expected = '<p href="https://www.google.com">raw text.<p>This is a paragraph of text.</p><a href="https://www.google.com">Click me!</a></p>'
        self.assertEqual(self.normal_parent.to_html(), expected)

    def test_empty_parent(self):
        with self.assertRaises(ValueError):
            self.empty_parent.to_html()

    def test_parent_in_parent(self):
        expected = '<p><p href="https://www.google.com">raw text.<p>This is a paragraph of text.</p><a href="https://www.google.com">Click me!</a></p></p>'
        self.assertEqual(self.parent_in_parent.to_html(), expected)

    def test_no_tag(self):
        node = ParentNode(None, [self.para_leaf], None)
        with self.assertRaises(ValueError):
            node.to_html()

if __name__ == "__main__":
    unittest.main()