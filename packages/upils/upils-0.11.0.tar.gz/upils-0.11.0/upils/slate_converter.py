"""
Module to convert a SlateJS rich-text to plain-text.

Based on the go-utils slate_converter https://github.com/kumparan/go-utils/blob/master/slate_converter.go
"""

import json
import re
from dataclasses import dataclass, field
from itertools import chain, islice, tee
from typing import Any, Dict, Iterable, Iterator, List, Tuple

# Regular expressions
MULTIPLE_DOTS_REGEX = re.compile(r"\.+")
DOT_SPACE_REGEX = re.compile(r"\.\s")

# Constants
COMMA_SEPARATOR = ","
DOT_SEPARATOR = "."
NEWLINE = "\n"
PUNCTUATION_MARKS = ".,:;!?"
SENTENCE_SEPARATOR = ". "
SPACE_SEPARATOR = " "

NODE_TYPE_HEADING_LARGE = "heading-large"
NODE_TYPE_HEADING_MEDIUM = "heading-medium"
NODE_TYPE_PARAGRAPH = "paragraph"
NODE_TYPE_BULLETED_LIST = "bulleted-list"
NODE_TYPE_NUMBERED_LIST = "numbered-list"
NODE_TYPE_LIST_ITEM = "list-item"
NODE_TYPE_INLINE = "inline"
NODE_TYPE_CAPTION = "caption"
NODE_TYPE_FIGURE = "figure"
NODE_TYPE_LINK = "link"


@dataclass
class SlateLeaf:
    """Represents a text element with optional formatting."""

    object: str = "leaf"
    text: str = ""
    marks: List[Any] = field(default_factory=list)

    @classmethod
    def from_dict(cls, leaf: Dict) -> "SlateLeaf":
        """Create an instance of SlateLeaf from a leaf dictionary."""
        return cls(
            object=leaf.get("object", "leaf"),
            text=leaf.get("text", ""),
            marks=leaf.get("marks", []),
        )


@dataclass
class SlateNode:
    """Represents a hierarchical document structure."""

    object: str = "block"
    type: str = ""
    nodes: List["SlateNode"] = field(default_factory=list)
    leaves: List[SlateLeaf] = field(default_factory=list)
    is_last_in_list: bool = False

    @classmethod
    def from_dict(cls, node: Dict) -> "SlateNode":
        """Create an instance of SlateNode from a node dictionary."""
        nodes = [SlateNode.from_dict(node_data) for node_data in node.get("nodes", [])]
        leaves = [
            SlateLeaf.from_dict(leaf_data) for leaf_data in node.get("leaves", [])
        ]

        return cls(
            object=node.get("object", "block"),
            type=node.get("type", ""),
            nodes=nodes,
            leaves=leaves,
        )

    def ensure_ends_with_punctuation(self) -> None:
        """Ensures that the last leaf of a paragraph node ends with punctuation."""
        # Case 1: If this node has leaves, check the last leaf's text.
        if self.leaves:
            last_slate_leaf = self.leaves[-1]
            if last_slate_leaf.text and not ends_with_punctuation(last_slate_leaf.text):
                last_slate_leaf.text += SENTENCE_SEPARATOR
            self.leaves[-1] = last_slate_leaf

        # Case 2: Check last child node's leaves.
        if self.nodes and self.nodes[-1].leaves:
            last_node = self.nodes[-1]
            last_slate_leaf = last_node.leaves[-1]
            if last_slate_leaf.text and not ends_with_punctuation(last_slate_leaf.text):
                last_slate_leaf.text += SENTENCE_SEPARATOR
            last_node.leaves[-1] = last_slate_leaf


@dataclass
class SlateDocument:
    """Represents the root structure of a Slate document."""

    nodes: List[SlateNode] = field(default_factory=list)

    @classmethod
    def from_dict(cls, document: Dict) -> "SlateDocument":
        """Create an instance of SlateDocument from a document dictionary."""
        document = document.get("document", {"nodes": []})
        nodes = [
            SlateNode.from_dict(node_data) for node_data in document.get("nodes", [])
        ]
        return cls(nodes=nodes)

    @classmethod
    def parse(cls, document_json: str) -> "SlateDocument":
        """Parses a Slate document JSON string into a SlateDocument struct."""
        try:
            document_dict = json.loads(document_json)
            return cls.from_dict(document_dict)
        except json.JSONDecodeError as error:
            raise error

    def to_plain_text(self) -> str:
        """Converts a Slate document into a plain-text format."""
        text = serialize_slate_nodes(self.nodes, NEWLINE, SPACE_SEPARATOR)
        text = re.sub(r"\n+", NEWLINE, text)
        return text.strip()


def serialize_slate_nodes(
    nodes: List[SlateNode], node_separator: str, leaf_separator: str
) -> str:
    """Recursively processes nodes and its content into a plain-text format."""
    result = []
    modified_slate_node_separator = node_separator

    for node in nodes:
        # Handle paragraph nodes by ensuring they end with punctuation.
        if node.type == NODE_TYPE_PARAGRAPH:
            node.ensure_ends_with_punctuation()

        # Recursively process child nodes.
        if node.nodes:
            if node.type in [
                NODE_TYPE_HEADING_LARGE,
                NODE_TYPE_CAPTION,
                NODE_TYPE_FIGURE,
            ]:
                continue
            if node.type == NODE_TYPE_HEADING_MEDIUM:
                modified_slate_node_separator = SENTENCE_SEPARATOR
            elif node.type in [NODE_TYPE_BULLETED_LIST, NODE_TYPE_NUMBERED_LIST]:
                node.nodes[-1].is_last_in_list = True
                temp = serialize_slate_nodes(
                    node.nodes, modified_slate_node_separator, leaf_separator
                )
                cleaned = clean_up_list(temp)
                result.append(cleaned)
                continue
            elif node.type == NODE_TYPE_INLINE:
                modified_slate_node_separator = SPACE_SEPARATOR
                serialized_inline = (
                    serialize_slate_nodes(
                        node.nodes, modified_slate_node_separator, leaf_separator
                    )
                    + leaf_separator
                )
                result.append(serialized_inline)
            elif node.type == NODE_TYPE_LINK:
                modified_slate_node_separator = SPACE_SEPARATOR
                serialized_link = serialize_slate_nodes(
                    node.nodes, modified_slate_node_separator, leaf_separator
                )
                result.append(serialized_link)
            elif node.type == NODE_TYPE_LIST_ITEM:
                modified_slate_node_separator = COMMA_SEPARATOR
                if node.is_last_in_list:
                    modified_slate_node_separator = SENTENCE_SEPARATOR
                serialized_list_item = (
                    serialize_slate_nodes(
                        node.nodes, modified_slate_node_separator, leaf_separator
                    )
                    + leaf_separator
                )
                result.append(serialized_list_item)
            else:
                serialized_default_type = serialize_slate_nodes(
                    node.nodes, SPACE_SEPARATOR, leaf_separator
                )
                serialized_default_type = serialized_default_type.strip()
                if (
                    modified_slate_node_separator == COMMA_SEPARATOR
                    and ends_with_punctuation(serialized_default_type)
                ):
                    serialized_default_type = (
                        serialized_default_type[:-1] + modified_slate_node_separator
                    )
                elif modified_slate_node_separator == NEWLINE:
                    serialized_default_type += modified_slate_node_separator
                result.append(serialized_default_type)
        elif node.leaves:
            result.append(serialize_slate_leaves(node.leaves, leaf_separator))

    return "".join(result)


def serialize_slate_leaves(leaves: List[SlateLeaf], separator: str) -> str:
    """
    Joins leaf texts with the given separator while trimming spaces around
    marked leaves (bold, italic, underline) to avoid unwanted spacing.

    Rules:
    - Both neighbors have marks → strip leading/trailing spaces.
    - Only previous leaf has marks → strip trailing space.
    - Only next leaf has marks → strip leading space.
    - No marked neighbors → keep text as is.
    """
    leaf_texts = []
    for prev_leaf, current_leaf, next_leaf in previous_and_next_item(leaves):
        if not current_leaf.text:
            continue

        is_prev_leaf_has_marks = bool(getattr(prev_leaf, "marks", []))
        is_next_leaf_has_marks = bool(getattr(next_leaf, "marks", []))

        # Condition 1: If previous and next leaf has marks, then strip whitespaces in front and in the end
        if is_prev_leaf_has_marks and is_next_leaf_has_marks:
            leaf_texts.append(current_leaf.text.strip())
        # Condition 2: If previous leaf has marks, then strip trailing whitespace
        elif is_prev_leaf_has_marks:
            leaf_texts.append(current_leaf.text.rstrip())
        # Condition 3: If next leaf has marks, then strip leading whitespace
        elif is_next_leaf_has_marks:
            leaf_texts.append(current_leaf.text.lstrip())
        # Condition 4: If previous and next leaf has no marks, then append text as is
        else:
            leaf_texts.append(current_leaf.text)

    return separator.join(leaf_texts)


def clean_up_list(text: str) -> str:
    """Cleans up the serialized list by removing excessive punctuation."""
    cleaned = MULTIPLE_DOTS_REGEX.sub(SENTENCE_SEPARATOR, text)
    return DOT_SPACE_REGEX.sub(DOT_SEPARATOR, cleaned)


def ends_with_punctuation(text: str) -> bool:
    """Checks if text ends with punctuation."""
    if not text:
        return False
    return text[-1] in PUNCTUATION_MARKS


def previous_and_next_item(items: Iterable[Any]) -> Iterator[Tuple[Any, Any, Any]]:
    """Yield (previous, current, next) tuples from the given iterable."""

    prev_items, current_items, next_items = tee(
        items, 3
    )  # 3 is the number of iterators we need from tee(): prev, current, next
    prev_items = chain([None], prev_items)  # prepend None to align previous
    next_items = chain(islice(next_items, 1, None), [None])  # append None to align next

    return zip(prev_items, current_items, next_items)
