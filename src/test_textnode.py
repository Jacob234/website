import unittest

from textnode import TextNode, text_node_to_html_node
from htmlnode import LeafNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_dif(self):
        node = TextNode("text", "bold")
        node2 = TextNode("text", "underline")
        self.assertNotEqual(node, node2)

    def test_url(self):
        node = TextNode("text", "bold", "None")
        node2 = TextNode("text", "underline", None)
        self.assertNotEqual(node, node2)

    
class TestTextNodeToHtmlNode(unittest.TestCase):
    def setUp(self):
        self.text_type_text = "text"
        self.text_type_bold = "bold"
        self.text_type_italic = "italic"
        self.text_type_code = "code"
        self.text_type_link = "link"
        self.text_type_image = "image"
        
        self.link = "https://www.google.com"
        self.text = "Sample text"

        self.bold_text = TextNode(self.text, self.text_type_bold)
        self.italic_text = TextNode(self.text, self.text_type_italic)
        self.text_text = TextNode(self.text, self.text_type_text)
        self.code_text = TextNode(self.text, self.text_type_code)
        self.link_text = TextNode(self.text, self.text_type_link, self.link)
        self.image_text = TextNode(self.text, self.text_type_image, self.link)

    def test_text_node(self):
        node = text_node_to_html_node(self.text_text)
        self.assertIsInstance(node, LeafNode)
        self.assertIsNone(node.tag)
        self.assertEqual(node.value, self.text)
        self.assertIsNone(node.props)

    def test_bold_node(self):
        node = text_node_to_html_node(self.bold_text)
        self.assertIsInstance(node, LeafNode)
        self.assertEqual(node.tag, "b")
        self.assertEqual(node.value, self.text)
        self.assertIsNone(node.props)

    def test_italic_node(self):
        node = text_node_to_html_node(self.italic_text)
        self.assertIsInstance(node, LeafNode)
        self.assertEqual(node.tag, "i")
        self.assertEqual(node.value, self.text)
        self.assertIsNone(node.props)

    def test_code_node(self):
        node = text_node_to_html_node(self.code_text)
        self.assertIsInstance(node, LeafNode)
        self.assertEqual(node.tag, "code")
        self.assertEqual(node.value, self.text)
        self.assertIsNone(node.props)

    def test_link_node(self):
        node = text_node_to_html_node(self.link_text)
        self.assertIsInstance(node, LeafNode)
        self.assertEqual(node.tag, "a")
        self.assertEqual(node.value, self.text)
        self.assertEqual(node.props, {"href": self.link})

    def test_image_node(self):
        node = text_node_to_html_node(self.image_text)
        self.assertIsInstance(node, LeafNode)
        self.assertEqual(node.tag, "img")
        self.assertEqual(node.props, {"src": self.link, "alt": self.text})

    def test_invalid_type(self):
        invalid_node = TextNode(self.text, "invalid_type")
        with self.assertRaises(ValueError):
            text_node_to_html_node(invalid_node)



    

        



if __name__ == "__main__":
    unittest.main()