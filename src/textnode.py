from htmlnode import LeafNode

class TextNode():

    def __init__(self, text, text_type, url = None):
        self.text = text
        self.text_type = text_type
        self.url = url



    def __eq__(self, other):
        if (self.text == other.text and self.text_type == other.text_type and self.url == other.url):
            return True
        else:
            return False

    def __repr__(self):
        return(f"TextNode({self.text}, {self.text_type}, {self.url})")
    

def text_node_to_html_node(text_node):
    type = text_node.text_type

    valid_types_props_dict = {"text" : None, "bold" : "b", "italic" : "i", "code" : "code", "link" : "a", "image" : "img"}


    if type == "link":
        node = LeafNode("a", text_node.text, {"href" : text_node.url})
        return node
    elif type == "image":
        node = LeafNode("img", "", {"src":text_node.url, "alt":text_node.text})
        return node
    elif type in valid_types_props_dict:
        node = LeafNode(valid_types_props_dict[type], text_node.text)
        return node
    else:
        raise ValueError
