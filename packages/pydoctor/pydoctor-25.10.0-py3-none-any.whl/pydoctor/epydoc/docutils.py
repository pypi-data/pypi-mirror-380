"""
Collection of helper functions and classes related to the creation and processing of L{docutils} nodes.
"""
from __future__ import annotations

from typing import Iterable, Iterator, Optional, TypeVar, cast, TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Literal

import optparse

from docutils import nodes, utils, frontend, __version_info__ as docutils_version_info
from docutils.transforms import parts

__docformat__ = 'epytext en'

_DEFAULT_DOCUTILS_SETTINGS: Optional[optparse.Values] = None

def new_document(source: Literal['docstring', 'code'], settings: Optional[optparse.Values] = None) -> nodes.document:
    """
    Create a new L{nodes.document} using the provided settings or cached default settings.

    @returns: L{nodes.document} with a C{source} attribute that matches the provided source.
    """
    global _DEFAULT_DOCUTILS_SETTINGS
    # If we have docutils >= 0.19 we use get_default_settings to calculate and cache
    # the default settings. Otherwise we let new_document figure it out.
    if settings is None and docutils_version_info >= (0,19):
        if _DEFAULT_DOCUTILS_SETTINGS is None:
            _DEFAULT_DOCUTILS_SETTINGS = frontend.get_default_settings()

        settings = _DEFAULT_DOCUTILS_SETTINGS

    return utils.new_document(source, settings)

def _set_nodes_parent(nodes: Iterable[nodes.Node], parent: nodes.Element) -> Iterator[nodes.Node]:
    """
    Set the L{nodes.Node.parent} attribute of the C{nodes} to the defined C{parent}. 
    
    @returns: An iterator containing the modified nodes.
    """
    for node in nodes:
        node.parent = parent
        yield node

TNode = TypeVar('TNode', bound=nodes.Node)
def set_node_attributes(node: TNode, 
                        document: Optional[nodes.document] = None, 
                        lineno: Optional[int] = None, 
                        children: Optional[Iterable[nodes.Node]] = None) -> TNode:
    """
    Set the attributes of a Node and return the modified node.
    This is required to manually construct a docutils document that is consistent.

    @param node: A node to edit.
    @param document: The L{nodes.Node.document} attribute.
    @param lineno: The L{nodes.Node.line} attribute.
    @param children: The L{nodes.Element.children} attribute. Special care is taken 
        to appropriately set the L{nodes.Node.parent} attribute on the child nodes. 
    """
    if lineno is not None:
        node.line = lineno
    
    if document:
        node.document = document

    if children:
        assert isinstance(node, nodes.Element), (f'Cannot set the children on Text node: "{node.astext()}". '
                                                 f'Children: {children}')
        node.extend(_set_nodes_parent(children, node))

    return node

def build_table_of_content(node: nodes.Element, depth: int, level: int = 0) -> nodes.Element | None:
    """
    Simplified from docutils Contents transform. 

    All section nodes MUST have set attribute 'ids' to a list of strings.
    """

    def _copy_and_filter(node: nodes.Element) -> nodes.Element:
        """Return a copy of a title, with references, images, etc. removed."""
        if (doc:=node.document) is None:
            raise AssertionError(f'missing document attribute on {node}')
        visitor = parts.ContentsFilter(doc)
        node.walkabout(visitor)
        #                                 the stubs are currently imcomplete, 2024.
        return visitor.get_entry_text() # type:ignore

    level += 1
    sections = [sect for sect in node if isinstance(sect, nodes.section)]
    entries = []
    if (doc:=node.document) is None:
        raise AssertionError(f'missing document attribute on {node}')
    
    for section in sections:
        title = cast(nodes.Element, section[0]) # the first element of a section is the header.
        entrytext = _copy_and_filter(title)
        reference = nodes.reference('', '', refid=section['ids'][0],
                                    *entrytext)
        ref_id = doc.set_id(reference, suggested_prefix='toc-entry')
        entry = nodes.paragraph('', '', reference)
        item = nodes.list_item('', entry)
        if title.next_node(nodes.reference) is None:
            title['refid'] = ref_id
        if level < depth:
            subsects = build_table_of_content(section, depth=depth, level=level)
            item += subsects or []
        entries.append(item)
    if entries:
        contents = nodes.bullet_list('', *entries)
        return contents
    else:
        return None

def get_lineno(node: nodes.Element) -> int:
    """
    Get the 0-based line number for a docutils `nodes.title_reference`.

    Walk up the tree hierarchy until we find an element with a line number, then
    counts the number of newlines until the reference element is found.
    """
    # Fixes https://github.com/twisted/pydoctor/issues/237
        
    def get_first_parent_lineno(_node: nodes.Element | None) -> int:
        if _node is None:
            return 0
        
        if _node.line:
            # This line points to the start of the containing node
            # Here we are removing 1 to the result because ParseError class is zero-based
            # while docutils line attribute is 1-based.
            line:int = _node.line-1
            # Let's figure out how many newlines we need to add to this number 
            # to get the right line number.
            parent_rawsource: Optional[str] = _node.rawsource or None
            node_rawsource: Optional[str] = node.rawsource or None

            if parent_rawsource is not None and \
               node_rawsource is not None:
                if node_rawsource in parent_rawsource:
                    node_index = parent_rawsource.index(node_rawsource)
                    # Add the required number of newlines to the result
                    line += parent_rawsource[:node_index].count('\n')
        else:
            line = get_first_parent_lineno(_node.parent)
        return line

    if node.line:
        # If the line is explicitely set, assume it's zero-based
        line = node.line
        # If docutils suddenly starts populating the line attribute for
        # title_reference node, all RST xref warnings will off by 1 :/

    else:
        line = get_first_parent_lineno(node.parent)
    
    return line

def text_node(text: str, klass: str | None = None) -> nodes.inline:
    """
    Create an inline node with the given text and class.
    """
    return set_node_attributes(
        nodes.inline('', '', classes=[klass] if klass else []), 
        children=[nodes.Text(text)],
    )

# additional docutils nodes: 

class wbr(nodes.inline):
    """
    Word break opportunity.
    """
    def __init__(self) -> None:
        super().__init__('', '')

class obj_reference(nodes.title_reference):
    """
    A reference to a documentable object.
    """

class code(nodes.inline):
    """
    Like a inline[class='literal'], but more elegant.
    """
