from htmlnode import *
from textnode import *

# def test_to_html():
#     node = HTMLNode(tag="p")
#     assert node.to_html() == ""
# def test_props_to_html():
#     node = HTMLNode(props={"href": "https://google.com", "target": "_blank"})
#     assert node.props_to_html() == ' href="https://google.com" target="_blank"'
# def test_repr():
#     node = HTMLNode(tag="p", value="content", children=None, props=None)
#     expected = 'HTMLNode(tag="p", value="content", children=None, props=None)'
#     assert repr(node) == expected

def test_leaf_to_html_p(self):
    node = LeafNode("p", "Hello, world!")
    self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

def test_to_html_with_children(self):
    child_node = LeafNode("span", "child")
    parent_node = ParentNode("div", [child_node])
    self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

def test_to_html_with_grandchildren(self):
    grandchild_node = LeafNode("b", "grandchild")
    child_node = ParentNode("span", [grandchild_node])
    parent_node = ParentNode("div", [child_node])
    self.assertEqual(
        parent_node.to_html(),
        "<div><span><b>grandchild</b></span></div>",
    )
def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

def test_headings(self):
    node = ParentNode(
        "h2",
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ],
    )
    self.assertEqual(
        node.to_html(),
        "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
    )
