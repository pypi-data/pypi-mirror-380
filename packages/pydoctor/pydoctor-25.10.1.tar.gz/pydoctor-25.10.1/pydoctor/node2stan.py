"""
Helper function to convert L{docutils} nodes to Stan tree.
"""
from __future__ import annotations

from functools import partial
from itertools import chain
import re
import optparse
from typing import Any, Callable, Iterable, List, Union, TYPE_CHECKING
from docutils.writers import html4css1
from docutils import nodes, frontend, __version_info__ as docutils_version_info

from twisted.web.template import Tag
if TYPE_CHECKING:
    from twisted.web.template import Flattenable
    from pydoctor.epydoc.markup import DocstringLinker
    from pydoctor.epydoc.docutils import obj_reference, code, wbr

from pydoctor.epydoc.docutils import get_lineno
from pydoctor.epydoc.doctest import colorize_codeblock, colorize_doctest
from pydoctor.stanutils import flatten, html2stan

def node2html(node: nodes.Node, docstring_linker: 'DocstringLinker') -> List[str]:
    """
    Convert a L{docutils.nodes.Node} object to HTML strings.
    """
    if (doc:=node.document) is None:
        raise AssertionError(f'missing document attribute on {node}')
    visitor = HTMLTranslator(doc, docstring_linker)
    node.walkabout(visitor)
    return visitor.body

def node2stan(node: Union[nodes.Node, Iterable[nodes.Node]], docstring_linker: 'DocstringLinker') -> Tag:
    """
    Convert L{docutils.nodes.Node} objects to a Stan tree.

    @param node: An docutils document or a fragment of document.
    @return: The element as a stan tree.
    @note:  Any L{nodes.Node} can be passed to that function, the only requirement is 
        that the node's L{nodes.Node.document} attribute is set to a valid L{nodes.document} object.
    """
    html = []
    if isinstance(node, nodes.Node):
        html += node2html(node, docstring_linker)
    else:
        for child in node:
            html += node2html(child, docstring_linker)
    return html2stan(''.join(html))


def gettext(node: Union[nodes.Node, List[nodes.Node]]) -> List[str]:
    """Return the text inside the node(s)."""
    filtered: List[str] = []
    if isinstance(node, (nodes.Text)):
        filtered.append(node.astext())
    elif isinstance(node, (list, nodes.Element)):
        for child in node[:]:
            filtered.extend(gettext(child))
    return filtered


_TARGET_RE = re.compile(r'^(.*?)\s*<(?:URI:|URL:)?([^<>]+)>$')
_VALID_IDENTIFIER_RE = re.compile('[^0-9a-zA-Z_]')

def _valid_identifier(s: str) -> str:
    """Remove invalid characters to create valid CSS identifiers. """
    return _VALID_IDENTIFIER_RE.sub('', s)

class HTMLTranslator(html4css1.HTMLTranslator):
    """
    Pydoctor's HTML translator.
    """
    # we use the class attribute and the instance attribute in two different manner,
    # for now this is not playing well with type checkers.
    settings: optparse.Values | None = None # type: ignore
    body: List[str]

    def __init__(self,
            document: nodes.document,
            docstring_linker: 'DocstringLinker'
            ):
        self._linker = docstring_linker

        # Set the document's settings.
        if self.settings is None:
            if docutils_version_info >= (0,19):
                # Direct access to OptionParser is deprecated from Docutils 0.19
                settings = frontend.get_default_settings(html4css1.Writer())
            else:
                settings = frontend.OptionParser([html4css1.Writer()]).get_default_values()
            
            # Save default settings as class attribute not to re-compute it all the times
            self.__class__.settings = settings
        else:
            #                        yes "optparse.Values" and "docutils.frontend.Values" are compatible.
            settings = self.settings # type: ignore
        
        document.settings = settings

        super().__init__(document)

        # don't allow <h1> tags, start at <h2>
        # h1 is reserved for the page title. 
        self.section_level += 1

        # All documents should be created with pydoctor.epydoc.docutils.new_document() helper
        # such that the source attribute will always be one of the supported values.
        self._document_is_code = is_code = document.attributes.get('source') == 'code'
        if is_code:
            # Do not wrap links in <code> tags if we're renderring a code-like parsed element.
            self._link_xref = self._linker.link_xref
        else:
            self._link_xref = lambda target, label, lineno: Tag('code')(self._linker.link_xref(target, label, lineno))


    # Handle interpreted text (crossreferences)
    def visit_title_reference(self, node: nodes.title_reference) -> None:
        lineno = get_lineno(node)
        self._handle_reference(node, link_func=partial(self._link_xref, lineno=lineno))
    
    # Handle internal references
    def visit_obj_reference(self, node: obj_reference) -> None:
        if node.attributes.get('is_annotation'):
            self._handle_reference(node, link_func=partial(self._linker.link_to, is_annotation=True))
        else:
            self._handle_reference(node, link_func=self._linker.link_to)
    
    def _handle_reference(self, node: nodes.title_reference, link_func: Callable[[str, "Flattenable"], "Flattenable"]) -> None:
        label: "Flattenable"
        if 'refuri' in node.attributes:
            # Epytext parsed or manually constructed nodes.
            label, target = node2stan(node.children, self._linker), node.attributes['refuri']
        else:
            # RST parsed.
            m = _TARGET_RE.match(node.astext())
            if m:
                label, target = m.groups()
            else:
                label = target = node.astext()
        
        # Support linking to functions and methods with () at the end
        if target.endswith('()'):
            target = target[:len(target)-2]

        self.body.append(flatten(link_func(target, label)))
        raise nodes.SkipNode()

    def visit_code(self, node: code) -> None:
        self.body.append(self.starttag(node, 'code', suffix=''))
    
    def depart_code(self, node: code) -> None:
        self.body.append('</code>')

    def should_be_compact_paragraph(self, node: nodes.Element) -> bool:
        if self.document.children == [node]:
            return True
        else:
            return super().should_be_compact_paragraph(node)

    def visit_document(self, node: nodes.document) -> None:
        pass

    def depart_document(self, node: nodes.document) -> None:
        pass

    def starttag(self, node: nodes.Element, tagname: str, suffix: str = '\n', *args: Any, **attributes: Any) -> str:
        """
        This modified version of starttag makes a few changes to HTML
        tags, to prevent them from conflicting with epydoc.  In particular:
          - existing class attributes are prefixed with C{'rst-'}
          - existing names are prefixed with C{'rst-'}
          - hrefs starting with C{'#'} are prefixed with C{'rst-'}
          - hrefs not starting with C{'#'} are given target='_top'
          - all headings (C{<hM{n}>}) are given the css class C{'heading'}
        """

        to_list_names = {'name':'names', 
                         'id':'ids', 
                         'class':'classes'}

        # Get the list of all attribute dictionaries we need to munge.
        attr_dicts = [attributes]
        if isinstance(node, nodes.Element):
            attr_dicts.append(node.attributes)
        # I must say we are keeping this for historical reason and I am not sure this
        # code path is even used in production.
        if isinstance(node, dict): # type: ignore
            attr_dicts.append(node)  # type: ignore
        # Munge each attribute dictionary.  Unfortunately, we need to
        # iterate through attributes one at a time because some
        # versions of docutils don't case-normalize attributes.
        for attr_dict in attr_dicts:
            # Prefix all CSS classes with "rst-"; and prefix all
                # names with "rst-" to avoid conflicts.
            done = set()
            for key, val in tuple(attr_dict.items()):
                if key.lower() in ('class', 'id', 'name'):
                    list_key = to_list_names[key.lower()]
                    attr_dict[list_key] = [f'rst-{cls}' if not cls.startswith('rst-') 
                                      else cls for cls in sorted(chain(val.split(), 
                                        attr_dict.get(list_key, ())))]
                    del attr_dict[key]
                    done.add(list_key)
            for key, val in tuple(attr_dict.items()):
                if key.lower() in ('classes', 'ids', 'names') and key.lower() not in done:
                    attr_dict[key] = [f'rst-{cls}' if not cls.startswith('rst-') 
                                      else cls for cls in sorted(val)]
                elif key.lower() == 'href':
                    if attr_dict[key][:1]=='#':
                        href = attr_dict[key][1:]
                        # We check that the class doesn't alrealy start with "rst-"
                        if not href.startswith('rst-'):
                            attr_dict[key] = f'#rst-{href}'
                    else:
                        # If it's an external link, open it in a new
                        # page.
                        attr_dict['target'] = '_top'

        # For headings, use class="heading"
        if re.match(r'^h\d+$', tagname):
            attributes['class'] = ' '.join([attributes.get('class',''),
                                            'heading']).strip()

        return super().starttag(node, tagname, suffix, *args, **attributes)

    def visit_doctest_block(self, node: nodes.doctest_block) -> None:
        pysrc = node[0].astext()
        if node.get('codeblock'):
            self.body.append(flatten(colorize_codeblock(pysrc)))
        else:
            self.body.append(flatten(colorize_doctest(pysrc)))
        raise nodes.SkipNode()


    # Other ressources on how to extend docutils:
    # https://docutils.sourceforge.io/docs/user/tools.html
    # https://docutils.sourceforge.io/docs/dev/hacking.html
    # https://docutils.sourceforge.io/docs/howto/rst-directives.html
    # docutils apidocs:
    # http://code.nabla.net/doc/docutils/api/docutils.html#package-structure

    # this part of the HTMLTranslator is based on sphinx's HTMLTranslator:
    # https://github.com/sphinx-doc/sphinx/blob/3.x/sphinx/writers/html.py#L271
    def _visit_admonition(self, node: nodes.Element, name: str) -> None:
        self.body.append(self.starttag(
            node, 'div', CLASS=('admonition ' + _valid_identifier(name))))
        node.insert(0, nodes.title(name, name.title()))
        self.set_first_last(node)
    
    if TYPE_CHECKING:
        # docutils stubs are a work in progress, so this copes with it.
        def depart_admonition(self, node: nodes.Admonition) -> None: # type: ignore
            pass

    def visit_note(self, node: nodes.note) -> None:
        self._visit_admonition(node, 'note')

    def depart_note(self, node: nodes.note) -> None:
        self.depart_admonition(node)

    def visit_warning(self, node: nodes.warning) -> None:
        self._visit_admonition(node, 'warning')

    def depart_warning(self, node: nodes.warning) -> None:
        self.depart_admonition(node)

    def visit_attention(self, node: nodes.attention) -> None:
        self._visit_admonition(node, 'attention')

    def depart_attention(self, node: nodes.attention) -> None:
        self.depart_admonition(node)

    def visit_caution(self, node: nodes.caution) -> None:
        self._visit_admonition(node, 'caution')

    def depart_caution(self, node: nodes.caution) -> None:
        self.depart_admonition(node)

    def visit_danger(self, node: nodes.danger) -> None:
        self._visit_admonition(node, 'danger')

    def depart_danger(self, node: nodes.danger) -> None:
        self.depart_admonition(node)

    def visit_error(self, node: nodes.error) -> None:
        self._visit_admonition(node, 'error')

    def depart_error(self, node: nodes.error) -> None:
        self.depart_admonition(node)

    def visit_hint(self, node: nodes.hint) -> None:
        self._visit_admonition(node, 'hint')

    def depart_hint(self, node: nodes.hint) -> None:
        self.depart_admonition(node)

    def visit_important(self, node: nodes.important) -> None:
        self._visit_admonition(node, 'important')

    def depart_important(self, node: nodes.important) -> None:
        self.depart_admonition(node)

    def visit_tip(self, node: nodes.tip) -> None:
        self._visit_admonition(node, 'tip')

    def depart_tip(self, node: nodes.tip) -> None:
        self.depart_admonition(node)

    def visit_wbr(self, node: wbr) -> None:
        self.body.append('<wbr></wbr>')
    
    def depart_wbr(self, node: wbr) -> None:
        pass

    def visit_seealso(self, node: nodes.Element) -> None:
        self._visit_admonition(node, 'see also')

    def depart_seealso(self, node: nodes.Admonition) -> None:
        self.depart_admonition(node)

    def visit_versionmodified(self, node: nodes.Element) -> None:
        self.body.append(self.starttag(node, 'div', CLASS=node['type']))

    def depart_versionmodified(self, node: nodes.Element) -> None:
        self.body.append('</div>\n')
