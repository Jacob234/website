import unittest

from htmlnode import HTMLNode


class TestTextNode(unittest.TestCase):
    def test_empty_eq(self):
        node = HTMLNode()
        node2 = HTMLNode(None, None, None, None)
        self.assertEqual(node, node2)

    def test_dif(self):
        node = HTMLNode("text", "bold")
        node2 = HTMLNode("text", "underline")
        self.assertNotEqual(node, node2)

    def test_url(self):
        node = HTMLNode("text", "bold", "None")
        node2 = HTMLNode("text", "underline", None)
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()