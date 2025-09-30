#
# restructuredtext.py: ReStructuredText docstring parsing
# Edward Loper
#
# Created [06/28/03 02:52 AM]
#
"""
Epydoc parser for ReStructuredText strings.  ReStructuredText is the
standard markup language used by the Docutils project.
L{parse_docstring()} provides the primary interface to this module; it
returns a L{ParsedRstDocstring}, which supports all of the methods
defined by L{ParsedDocstring}.

L{ParsedRstDocstring} is basically just a L{ParsedDocstring} wrapper
for the C{nodes.document} class.

B{Creating C{ParsedRstDocstring}s}:

C{ParsedRstDocstring}s are created by the L{parse_docstring} function,
using the C{docutils.core.publish_string()} method, with the following
helpers:

  - An L{_EpydocReader} is used to capture all error messages as it
    parses the docstring.
  - A L{_DocumentPseudoWriter} is used to extract the document itself,
    without actually writing any output.  The document is saved for
    further processing.  The settings for the writer are copied from
    C{docutils.writers.html4css1.Writer}, since those settings will
    be used when we actually write the docstring to html.

@var CONSOLIDATED_FIELDS: A dictionary encoding the set of
'consolidated fields' that can be used.  Each consolidated field is
marked by a single tag, and contains a single bulleted list, where
each list item starts with an identifier, marked as interpreted text
(C{`...`}).  This module automatically splits these consolidated
fields into individual fields.  The keys of C{CONSOLIDATED_FIELDS} are
the names of possible consolidated fields; and the values are the
names of the field tags that should be used for individual entries in
the list.
"""
from __future__ import annotations
__docformat__ = 'epytext en'

from typing import TYPE_CHECKING, Any, Iterable, List, Optional, Sequence, Set, cast
if TYPE_CHECKING:
    from typing import TypeAlias
    
import re
from docutils import nodes

from docutils.core import publish_string
from docutils.writers import Writer
from docutils.parsers.rst.directives.admonitions import BaseAdmonition
from docutils.readers.standalone import Reader as StandaloneReader
from docutils.utils import Reporter
from docutils.parsers.rst import Directive, directives
from docutils.transforms import Transform, frontmatter

from pydoctor.epydoc.markup import Field, ObjClass, ParseError, ParsedDocstring, ParserFunction
from pydoctor.epydoc.markup.plaintext import ParsedPlaintextDocstring
from pydoctor.epydoc.docutils import new_document

CONSOLIDATED_FIELDS = {
    'parameters': 'param',
    'arguments': 'arg',
    'exceptions': 'except',
    'variables': 'var',
    'ivariables': 'ivar',
    'cvariables': 'cvar',
    'groups': 'group',
    'types': 'type',
    'keywords': 'keyword',
    }

#: A list of consolidated fields whose bodies may be specified using a
#: definition list, rather than a bulleted list.  For these fields, the
#: 'classifier' for each term in the definition list is translated into
#: a @type field.
CONSOLIDATED_DEFLIST_FIELDS = ['param', 'arg', 'var', 'ivar', 'cvar', 'keyword']

def parse_docstring(docstring: str, 
                    errors: List[ParseError], 
                    ) -> ParsedDocstring:
    """
    Parse the given docstring, which is formatted using
    ReStructuredText; and return a L{ParsedDocstring} representation
    of its contents.

    @param docstring: The docstring to parse
    @param errors: A list where any errors generated during parsing
        will be stored.
    """
    writer = _DocumentPseudoWriter()
    reader = _EpydocReader(errors) # Outputs errors to the list.

    # Credits: mhils - Maximilian Hils from the pdoc repository https://github.com/mitmproxy/pdoc
    # Strip Sphinx interpreted text roles for code references: :obj:`foo` -> `foo`
    docstring = re.sub(
        r"(:py)?:(mod|func|data|const|class|meth|attr|exc|obj):", "", docstring
    )

    publish_string(docstring, writer=writer, reader=reader,
                   settings_overrides={'report_level':10000,
                                       'halt_level':10000,
                                       'warning_stream':None})

    document = writer.document
    visitor = _SplitFieldsTranslator(document, errors)
    document.walk(visitor)

    return ParsedRstDocstring(document, visitor.fields)

def get_parser(_: ObjClass | None) -> ParserFunction:
    """
    Get the L{parse_docstring} function. 
    """
    return parse_docstring

class OptimizedReporter(Reporter):
    """A reporter that ignores all debug messages.  This is used to
    shave a couple seconds off of epydoc's run time, since docutils
    isn't very fast about processing its own debug messages.
    """

    def debug(self, *args: Any, **kwargs: Any) -> None: # type:ignore[override]
        pass

class ParsedRstDocstring(ParsedDocstring):
    """
    An encoded version of a ReStructuredText docstring.  The contents
    of the docstring are encoded in the L{_document} instance
    variable.
    """

    def __init__(self, document: nodes.document, fields: Sequence[Field]):
        self._document = document
        """A ReStructuredText document, encoding the docstring."""

        document.reporter = OptimizedReporter(
            document.reporter.source, 
            report_level=10000, halt_level=10000, 
            stream='')

        ParsedDocstring.__init__(self, fields)

    @property
    def has_body(self) -> bool:
        return any(
            isinstance(child, nodes.Text) or child.children
            for child in self._document.children
            )

    def to_node(self) -> nodes.document:
        return self._document

    def __repr__(self) -> str:
        return '<ParsedRstDocstring: ...>'

class _EpydocReader(StandaloneReader): # type:ignore[type-arg]
    """
    A reader that captures all errors that are generated by parsing,
    and appends them to a list as L{ParseError}.
    """

    def __init__(self, errors: List[ParseError]):
        self._errors = errors
        StandaloneReader.__init__(self)

    def get_transforms(self) -> list[type[Transform]]:
        # Remove the DocInfo transform, to ensure that :author: fields
        # are correctly handled.
        return [t for t in StandaloneReader.get_transforms(self)
                if t != frontmatter.DocInfo]

    def new_document(self) -> nodes.document:
        document = new_document('docstring', self.settings)
        # Capture all warning messages.
        document.reporter.attach_observer(self.report)
        # Return the new document.
        return document

    def report(self, error: nodes.system_message) -> None:
        level: int = error['level']
        is_fatal = level >= Reporter.ERROR_LEVEL

        linenum: Optional[int] = error.get('line')

        msg = ''.join(c.astext() for c in error)

        self._errors.append(ParseError(msg, linenum, is_fatal))

if TYPE_CHECKING:
    _StrWriter: TypeAlias = Writer[str]
else:
    _StrWriter = Writer

class _DocumentPseudoWriter(_StrWriter):
    """
    A pseudo-writer for the docutils framework, that can be used to
    access the document itself.  The output of C{_DocumentPseudoWriter}
    is just an empty string; but after it has been used, the most
    recently processed document is available as the instance variable
    C{document}.
    """

    document: nodes.document
    """The most recently processed document."""

    def translate(self) -> None:
        self.output = ''

class _SplitFieldsTranslator(nodes.NodeVisitor):
    """
    A docutils translator that removes all fields from a document, and
    collects them into the instance variable C{fields}

    @ivar fields: The fields of the most recently walked document.
    @type fields: C{list} of L{Field<markup.Field>}
    """

    ALLOW_UNMARKED_ARG_IN_CONSOLIDATED_FIELD = True
    """If true, then consolidated fields are not required to mark
    arguments with C{`backticks`}.  (This is currently only
    implemented for consolidated fields expressed as definition lists;
    consolidated fields expressed as unordered lists still require
    backticks for now."""

    def __init__(self, document: nodes.document, errors: List[ParseError]):
        nodes.NodeVisitor.__init__(self, document)
        self._errors = errors
        self.fields: List[Field] = []
        self._newfields: Set[str] = set()

    def visit_document(self, node: nodes.document) -> None:
        self.fields = []

    def visit_field(self, node: nodes.field) -> None:
        # Remove the field from the tree.
        node.parent.remove(node)

        # Extract the field name & optional argument
        # FIXME: https://github.com/twisted/pydoctor/issues/267
        #   Support combined parameter type and description, if the type is a single word like::
        #       :param str user_agent: user agent
        tag = node[0].astext().split(None, 1)
        tagname = tag[0]
        if len(tag)>1: 
            arg = tag[1]
        else: 
            arg = None

        # Handle special fields:
        fbody = node[1]
        assert isinstance(fbody, nodes.Element)
        if arg is None:
            for (list_tag, entry_tag) in CONSOLIDATED_FIELDS.items():
                if tagname.lower() == list_tag:
                    try:
                        self.handle_consolidated_field(fbody, entry_tag)
                        return
                    except ValueError as e:
                        estr = 'Unable to split consolidated field '
                        estr += f'"{tagname}" - {e}'
                        self._errors.append(ParseError(estr, node.line,
                                                       is_fatal=False))

                        # Use a @newfield to let it be displayed as-is.
                        if tagname.lower() not in self._newfields:
                            newfield = Field('newfield', tagname.lower(),
                                             ParsedPlaintextDocstring(tagname),
                                             (node.line or 1) - 1)
                            self.fields.append(newfield)
                            self._newfields.add(tagname.lower())

        self._add_field(tagname, arg, fbody, node.line)

    def _add_field(self,
            tagname: str,
            arg: Optional[str],
            fbody: Iterable[nodes.Node],
            lineno: int | None
            ) -> None:
        field_doc = self.document.copy()
        for child in fbody: 
            field_doc.append(child)
        field_parsed_doc = ParsedRstDocstring(field_doc, ())
        self.fields.append(Field(tagname, arg, field_parsed_doc, (lineno or 1) - 1))

    def visit_field_list(self, node: nodes.field_list) -> None:
        # Remove the field list from the tree.  The visitor will still walk
        # over the node's children.
        node.parent.remove(node)

    def handle_consolidated_field(self, body: nodes.Element, tagname: str) -> None:
        """
        Attempt to handle a consolidated section.
        """
        if len(body) != 1:
            raise ValueError('does not contain a single list.')
        if not isinstance(b0:=body[0], nodes.Element):
            # unfornutate assertion required for typing purposes
            raise ValueError('does not contain a list.')
        if isinstance(b0, nodes.bullet_list):
            self.handle_consolidated_bullet_list(b0, tagname)
        elif (isinstance(b0, nodes.definition_list) and
              tagname in CONSOLIDATED_DEFLIST_FIELDS):
            self.handle_consolidated_definition_list(b0, tagname)
        elif tagname in CONSOLIDATED_DEFLIST_FIELDS:
            raise ValueError('does not contain a bulleted list or '
                             'definition list.')
        else:
            raise ValueError('does not contain a bulleted list.')

    def handle_consolidated_bullet_list(self, items: nodes.bullet_list, tagname: str) -> None:
        # Check the contents of the list.  In particular, each list
        # item should have the form:
        #   - `arg`: description...
        n = 0
        _BAD_ITEM = ("list item %d is not well formed.  Each item must "
                     "consist of a single marked identifier (e.g., `x`), "
                     "optionally followed by a colon or dash and a "
                     "description.")
        for item in items:
            n += 1
            if not isinstance(item, nodes.list_item) or len(item) == 0:
                raise ValueError('bad bulleted list (bad child %d).' % n)
            if not isinstance(i0:=item[0], nodes.paragraph):
                if isinstance(i0, nodes.definition_list):
                    raise ValueError(('list item %d contains a definition '+
                                      'list (it\'s probably indented '+
                                      'wrong).') % n)
                else:
                    raise ValueError(_BAD_ITEM % n)
            if len(i0) == 0:
                raise ValueError(_BAD_ITEM % n)
            if not isinstance(i0[0], nodes.title_reference):
                raise ValueError(_BAD_ITEM % n)

        # Everything looks good; convert to multiple fields.
        for item in items:
            assert isinstance(item, nodes.list_item) # for typing
            # Extract the arg, item[0][0] is safe since we checked eariler for malformated list.
            arg = item[0][0].astext() # type: ignore

            # Extract the field body, and remove the arg
            fbody = cast('list[nodes.Element]', item[:])
            fbody[0] = fbody[0].copy()
            fbody[0][:] = cast(nodes.paragraph, item[0])[1:]

            # Remove the separating ":", if present
            if (len(fbody[0]) > 0 and
                isinstance(fbody[0][0], nodes.Text)):
                text = fbody[0][0].astext()
                if text[:1] in ':-':
                    fbody[0][0] = nodes.Text(text[1:].lstrip())
                elif text[:2] in (' -', ' :'):
                    fbody[0][0] = nodes.Text(text[2:].lstrip())

            # Wrap the field body, and add a new field
            self._add_field(tagname, arg, fbody, fbody[0].line)

    def handle_consolidated_definition_list(self, items: nodes.definition_list, tagname: str) -> None:
        # Check the list contents.
        n = 0
        _BAD_ITEM = ("item %d is not well formed.  Each item's term must "
                     "consist of a single marked identifier (e.g., `x`), "
                     "optionally followed by a space, colon, space, and "
                     "a type description.")
        for item in items:
            n += 1
            if (not isinstance(item, nodes.definition_list_item) or len(item) < 2 or
                not isinstance(item[-1], nodes.definition) or 
                not isinstance(i0:=item[0], nodes.Element)):
                raise ValueError('bad definition list (bad child %d).' % n)
            if len(item) > 3:
                raise ValueError(_BAD_ITEM % n)
            if not ((isinstance(i0[0], nodes.title_reference)) or
                    (self.ALLOW_UNMARKED_ARG_IN_CONSOLIDATED_FIELD and
                     isinstance(i0[0], nodes.Text))):
                raise ValueError(_BAD_ITEM % n)
            for child in i0[1:]:
                if child.astext() != '':
                    raise ValueError(_BAD_ITEM % n)

        # Extract it.
        for item in items:
            assert isinstance(item, nodes.definition_list_item) # for typing
            # The basic field.
            arg = cast(nodes.Element, item[0])[0].astext()
            lineno = item[0].line
            fbody = cast(nodes.definition, item[-1])
            self._add_field(tagname, arg, fbody, lineno)
            # If there's a classifier, treat it as a type.
            if len(item) == 3:
                type_descr = cast(nodes.Element, item[1])
                self._add_field('type', arg, type_descr, lineno)

    def unknown_visit(self, node: nodes.Node) -> None:
        'Ignore all unknown nodes'

versionlabels = {
    'versionadded':   'New in version %s',
    'versionchanged': 'Changed in version %s',
    'deprecated':     'Deprecated since version %s',
}

versionlabel_classes = {
    'versionadded':     'added',
    'versionchanged':   'changed',
    'deprecated':       'deprecated',
}

class VersionChange(Directive):
    """
    Directive to describe a change/addition/deprecation in a specific version.
    """
    class versionmodified(nodes.Admonition, nodes.TextElement):
        """Node for version change entries.
        Currently used for "versionadded", "versionchanged" and "deprecated"
        directives.
        """
    
    has_content = True
    required_arguments = 1
    optional_arguments = 1
    final_argument_whitespace = True

    def run(self) -> List[nodes.Node]:
        node = self.versionmodified()
        node.document = self.state.document
        node['type'] = self.name
        node['version'] = self.arguments[0]
        text = versionlabels[self.name] % self.arguments[0]
        if len(self.arguments) == 2:
            inodes, messages = self.state.inline_text(self.arguments[1],
                                                      self.lineno + 1)
            para = nodes.paragraph(self.arguments[1], '', *inodes)
            node.append(para)
        else:
            messages = []
        if self.content:
            self.state.nested_parse(self.content, self.content_offset, node)
        classes = ['versionmodified', versionlabel_classes[self.name]]
        if len(node):
            if isinstance(node[0], nodes.paragraph) and node[0].rawsource:
                content = nodes.inline(node[0].rawsource)
                content.source = node[0].source
                content.line = node[0].line
                content += node[0].children
                node[0].replace_self(nodes.paragraph('', '', content))

            para = cast(nodes.paragraph, node[0])
            para.insert(0, nodes.inline('', '%s: ' % text, classes=classes))
        else:
            para = nodes.paragraph('', '',
                                   nodes.inline('', '%s.' % text,
                                                classes=classes), )
            node.append(para)

        ret = [node]  # type: List[nodes.Node]
        ret += messages
        return ret

# Do like Sphinx does for the seealso directive. 
class SeeAlso(BaseAdmonition):
    """
    An admonition mentioning things to look at as reference.
    """
    class seealso(nodes.Admonition, nodes.Element):
        """Custom "see also" admonition node."""

    node_class = seealso

class PythonCodeDirective(Directive):
    """
    A custom restructuredtext directive which can be used to display
    syntax-highlighted Python code blocks.  This directive takes no
    arguments, and the body should contain only Python code.  This
    directive can be used instead of doctest blocks when it is
    inconvenient to list prompts on each line, or when you would
    prefer that the output not contain prompts (e.g., to make
    copy/paste easier).
    """

    has_content = True
    
    def run(self) -> List[nodes.Node]:
        text = '\n'.join(self.content)
        node = nodes.doctest_block(text, text, codeblock=True)
        return [ node ]

class DocutilsAndSphinxCodeBlockAdapter(PythonCodeDirective):
    # Docutils and Sphinx code blocks have both one optional argument, 
    # so we accept it here as well but do nothing with it.
    required_arguments = 0
    optional_arguments = 1

    # Listing all options that docutils.parsers.rst.directives.body.CodeBlock provides
    # And also sphinx.directives.code.CodeBlock. We don't care about their values, 
    # we just don't want to see them in self.content.
    option_spec = {'class': directives.class_option,
                'name': directives.unchanged,
                'number-lines': directives.unchanged, # integer or None
                'force': directives.flag,
                'linenos': directives.flag,
                'dedent': directives.unchanged, # integer or None
                'lineno-start': int,
                'emphasize-lines': directives.unchanged_required,
                'caption': directives.unchanged_required,
    }

directives.register_directive('python', PythonCodeDirective)
directives.register_directive('code', DocutilsAndSphinxCodeBlockAdapter)
directives.register_directive('code-block', DocutilsAndSphinxCodeBlockAdapter)
directives.register_directive('versionadded', VersionChange)
directives.register_directive('versionchanged', VersionChange)
directives.register_directive('deprecated', VersionChange)
directives.register_directive('seealso', SeeAlso)
