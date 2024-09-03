import unittest

from textnode import TextNode


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


if __name__ == "__main__":
    unittest.main()