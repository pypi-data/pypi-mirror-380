"""
Convert L{pydoctor.epydoc} parsed markup into renderable content.
"""
from __future__ import annotations

from collections import defaultdict
import enum
import inspect
from typing import (
    TYPE_CHECKING, Any, Callable, ClassVar, DefaultDict, Dict, Generator,
    Iterator, List, Mapping, Optional, Sequence, Tuple, Union,
)
import ast
import re

import attr
from docutils import nodes

from pydoctor import model, linker
from pydoctor.astutils import is_none_literal
from pydoctor.epydoc.docutils import new_document, set_node_attributes, text_node, code
from pydoctor.epydoc.markup import (Field as EpydocField, ParseError, get_parser_by_name, 
                                    processtypes, parsed_text)
from twisted.web.template import Tag, tags
from pydoctor.epydoc.markup import ParsedDocstring, DocstringLinker, ObjClass
import pydoctor.epydoc.markup.plaintext
from pydoctor.epydoc.markup.restructuredtext import ParsedRstDocstring
from pydoctor.epydoc.markup._pyval_repr import colorize_pyval, colorize_inline_pyval

if TYPE_CHECKING:
    from twisted.web.template import Flattenable

taglink = linker.taglink
"""
Alias to L{pydoctor.linker.taglink()}.
"""

BROKEN_TEXT = 'Broken description'
BROKEN = tags.p(class_="undocumented")(BROKEN_TEXT)

def _get_docformat(obj: model.Documentable) -> str:
    """
    Returns the docformat to use to parse the docstring of this object.
    """
    # Use module's __docformat__ if specified, else use system's.
    # Except if system's docformat is plaintext, in this case, use plaintext.
    # See https://github.com/twisted/pydoctor/issues/503 for the reason
    # of this behavior.
    if obj.system.options.docformat == 'plaintext':
        return 'plaintext'
    # the docstring should be parsed using the format of the module it was inherited from
    docformat = obj.module.docformat or obj.system.options.docformat
    return docformat

@attr.s(auto_attribs=True)
class FieldDesc:
    """
    Combines informations from multiple L{Field} objects into one.

    Example::

       :param foo: description of parameter foo
       :type foo:  SomeClass

    """
    _UNDOCUMENTED: ClassVar[Tag] = tags.span(class_='undocumented')("Undocumented")

    name: Optional[str] = None
    """Field name, i.e. C{:param <name>:}"""

    type: Optional[Tag] = None
    """Formatted type"""

    body: Optional[Tag] = None

    def format(self) -> Generator[Tag, None, None]:
        """
        @return: Iterator that yields one or two C{tags.td}.
        """
        formatted = self.body or self._UNDOCUMENTED
        fieldNameTd: List[Tag] = []
        if self.name:
            # Add the stars to the params names just before generating the field stan, not before.
            if isinstance(self.name, VariableArgument):
                prefix = "*"
            elif isinstance(self.name, KeywordArgument):
                prefix = "**"
            else:
                prefix = ""

            name = tags.transparent(prefix, insert_break_points(self.name))

            stan_name = tags.span(class_="fieldArg")(name)
            if self.type:
                stan_name(":")
            fieldNameTd.append(stan_name)

        if self.type:
            fieldNameTd.append(self.type)
        if fieldNameTd:
            #  <name>: <type> | <desc>
            yield tags.td(class_="fieldArgContainer")(*fieldNameTd)
            yield tags.td(class_="fieldArgDesc")(formatted)
        else:
            #  <desc>
            yield tags.td(formatted, colspan="2")

@attr.s(auto_attribs=True)
class _SignatureDesc(FieldDesc):
    type_origin: Optional['FieldOrigin'] = None

    def is_documented(self) -> bool:
        return bool(self.body or self.type_origin is FieldOrigin.FROM_DOCSTRING)

@attr.s(auto_attribs=True)
class ReturnDesc(_SignatureDesc):...

@attr.s(auto_attribs=True)
class ParamDesc(_SignatureDesc):...

@attr.s(auto_attribs=True)
class KeywordDesc(_SignatureDesc):...

class RaisesDesc(FieldDesc):
    """Description of an exception that can be raised by function/method."""

    def format(self) -> Generator[Tag, None, None]:
        assert self.type is not None  # TODO: Why can't it be None?
        yield tags.td(tags.code(self.type), class_="fieldArgContainer")
        yield tags.td(self.body or self._UNDOCUMENTED)

def format_desc_list(label: str, descs: Sequence[FieldDesc]) -> list[Tag]:
    """
    Format list of L{FieldDesc}. Used for param, returns, raises, etc.

    Generates a 2-columns layout as follow::

        +------------------------------------+
        | <label>                            |
        | <name>: <type> |     <desc>        |
        | <name>: <type> |     <desc>        |
        +------------------------------------+

    If the fields don't have type or name information,
    generates the same output as L{format_field_list}::

        +------------------------------------+
        | <label>                            |
        | <desc ... >                        |
        +------------------------------------+

    @arg label: Section "mini heading"
    @arg descs: L{FieldDesc}s
    @returns: A list containing a single table tag or an empty list if no C{descs} are provided.
    """
    if not descs: 
        return []
    
    def rows() -> Iterator[Tag]:
        # <label>
        row = tags.tr(class_="fieldStart")
        row(tags.td(class_="fieldName", colspan="2")(label))
        # yield the first row.
        yield row
        # yield descriptions.
        for d in descs:
            row = tags.tr()
            # <name>: <type> |     <desc>
            # or
            # <desc ... >
            row(d.format())
            yield row
    
    return [tags.table(class_='fieldTable')(*rows())]

@attr.s(auto_attribs=True)
class Field:
    """Like L{pydoctor.epydoc.markup.Field}, but without the gross accessor
    methods and with a formatted body.

    Example::

        @note: some other information
    """

    tag: str
    """Field tag, i.e. C{:<tag>:} """
    arg: Optional[str]
    """Field argument, i.e. C{:param <argument>:}"""
    source: model.Documentable
    lineno: int
    body: ParsedDocstring

    @classmethod
    def from_epydoc(cls, field: EpydocField, source: model.Documentable) -> 'Field':
        return cls(
            tag=field.tag(),
            arg=field.arg(),
            source=source,
            lineno=field.lineno,
            body=field.body()
            )

    def format(self) -> Tag:
        """Present this field's body as HTML."""
        return safe_to_stan(self.body, self.source.docstring_linker, self.source,
                    # the parsed docstring maybe doesn't support to_node(), i.e. ParsedTypeDocstring,
                    # so we can only show the broken text.
                    fallback=lambda _, __, ___:BROKEN)

    def report(self, message: str) -> None:
        self.source.report(message, lineno_offset=self.lineno, section='docstring')


def format_field_list(singular: str, plural: str, fields: Sequence[Field]) -> list[Tag]:
    """
    Format list of L{Field} object. Used for notes, see also, authors, etc.

    Generates a 2-columns layout as follow::

        +------------------------------------+
        | <label>                            |
        | <desc ... >                        |
        +------------------------------------+

    @returns: A list containing a single table tag or an empty list if no C{fields} are provided.
    """
    if not fields: 
        return []
    
    def rows() -> Iterator[Tag]:
        label = singular if len(fields) == 1 else plural
        row = tags.tr(class_="fieldStart")
        row(tags.td(class_="fieldName", colspan="2")(label))
        yield row

        for field in fields:
            row = tags.tr()
            row(tags.td(colspan="2")(field.format()))
            yield row

    return [tags.table(class_='fieldTable')(*rows())]

class VariableArgument(str):
    """
    Encapsulate the name of C{vararg} parameters in L{Function.annotations} mapping keys.
    """

class KeywordArgument(str):
    """
    Encapsulate the name of C{kwarg} parameters in L{Function.annotations} mapping keys.
    """

class FieldOrigin(enum.Enum):
    FROM_AST = 0
    FROM_DOCSTRING = 1

@attr.s(auto_attribs=True)
class ParamType:
    stan: Tag
    origin: FieldOrigin

class FieldHandler:

    def __init__(self, obj: model.Documentable):
        self.obj = obj
        self._linker = self.obj.docstring_linker

        self.types: Dict[str, Optional[ParamType]] = {}

        self.parameter_descs: List[Union[ParamDesc, KeywordDesc]] = []
        self.return_desc: Optional[ReturnDesc] = None
        self.yields_desc: Optional[FieldDesc] = None
        self.raise_descs: List[RaisesDesc] = []
        self.warns_desc: List[FieldDesc] = []
        self.seealsos: List[Field] = []
        self.notes: List[Field] = []
        self.authors: List[Field] = []
        self.sinces: List[Field] = []
        self.unknowns: DefaultDict[str, List[FieldDesc]] = defaultdict(list)

    def set_param_types_from_annotations(
            self, annotations: Mapping[str, Optional[ast.expr]]
            ) -> None:
        _linker = self.obj.docstring_linker
        formatted_annotations = {
            name: None if value is None
                       else ParamType(safe_to_stan(colorize_inline_pyval(value, is_annotation=True), _linker,
                                self.obj, fallback=colorized_pyval_fallback, section='annotation', report=False),
                                # don't spam the log, invalid annotation are going to be reported when the signature gets colorized
                                origin=FieldOrigin.FROM_AST)

            for name, value in annotations.items()
            }

        ret_type = formatted_annotations.pop('return', None)
        self.types.update(formatted_annotations)
        if ret_type is not None:
            # In most cases 'None' is not an actual return type, but the absence
            # of a returned value. Not storing it is the easiest way to prevent
            # it from being presented.
            ann_ret = annotations['return']
            assert ann_ret is not None  # ret_type would be None otherwise
            if not is_none_literal(ann_ret):
                self.return_desc = ReturnDesc(type=ret_type.stan, type_origin=ret_type.origin)

    @staticmethod
    def _report_unexpected_argument(field:Field) -> None:
        if field.arg is not None:
            field.report('Unexpected argument in %s field' % (field.tag,))

    def handle_return(self, field: Field) -> None:
        self._report_unexpected_argument(field)
        if not self.return_desc:
            self.return_desc = ReturnDesc()
        self.return_desc.body = field.format()
    handle_returns = handle_return

    def handle_yield(self, field: Field) -> None:
        self._report_unexpected_argument(field)
        if not self.yields_desc:
            self.yields_desc = FieldDesc()
        self.yields_desc.body = field.format()
    handle_yields = handle_yield

    def handle_returntype(self, field: Field) -> None:
        self._report_unexpected_argument(field)
        if not self.return_desc:
            self.return_desc = ReturnDesc()
        self.return_desc.type = field.format()
        self.return_desc.type_origin = FieldOrigin.FROM_DOCSTRING
    handle_rtype = handle_returntype

    def handle_yieldtype(self, field: Field) -> None:
        self._report_unexpected_argument(field)
        if not self.yields_desc:
            self.yields_desc = FieldDesc()
        self.yields_desc.type = field.format()
    handle_ytype = handle_yieldtype

    def _handle_param_name(self, field: Field) -> Optional[str]:
        """
        Returns the Field name and trigger a few warnings for a few scenarios.
        Note that the return type could be L{VariableArgument} or L{KeywordArgument} or L{str}.
        """
        name = field.arg
        if name is None:
            field.report('Parameter name missing')
            return None

        name = name.lstrip('*')
        annotations = None
        if isinstance(field.source, model.Function):
            annotations = field.source.annotations
        elif isinstance(field.source, model.Class):
            # Constructor parameters can be documented on the class.
            annotations = field.source.constructor_params
        # This might look useless, but it's needed in order to keep the
        # right return type and then add the stars accordingly.
        if annotations is not None:
            for param_name, _ in annotations.items():
                if param_name == name:
                    name = param_name
        return name

    def _handle_param_not_found(self, name: str, field: Field) -> None:
        """Figure out if the parameter might exist despite not being found
        in this documentable's code, warn if not.
        """
        source = field.source
        if source is not self.obj:
            # Docstring is inherited, so it may not represent this exact method.
            return
        if isinstance(source, model.Class):
            if None in source.baseobjects:
                # Class has a computed base class, which could define parameters
                # we can't discover.
                # For example, this class might use
                # L{twisted.python.components.proxyForInterface()}.
                return
            if name in source.constructor_params:
                # Constructor parameters can be documented on the class.
                return
        msg = f'Documented parameter "{name}" does not exist'
        if any(isinstance(n, KeywordArgument) for n in self.types):
            msg += ', variable keywords should be documented with the '
            if _get_docformat(self.obj) in ('google', 'numpy'):
                msg += '"Keyword Arguments" section'
            else:
                msg += '"keyword" field'
        field.report(msg)

    def handle_type(self, field: Field) -> None:
        if isinstance(self.obj, model.Attribute):
            if field.arg is not None:
                field.report('Field in variable docstring should not include a name')
            self.obj.parsed_type = field.body
            return
        elif isinstance(self.obj, model.Function):
            name = self._handle_param_name(field)
            if name is not None and name not in self.types and not any(
                    # Don't warn about keywords or about parameters we already
                    # reported a warning for.
                    desc.name == name for desc in self.parameter_descs
                    ):
                self._handle_param_not_found(name, field)
        else:
            # Note: extract_fields() will issue warnings about missing field
            #       names, so we can silently ignore them here.
            # TODO: Processing the fields once in extract_fields() and again
            #       in format_docstring() adds complexity and can cause
            #       inconsistencies.
            name = field.arg
        if name is not None:
            self.types[name] = ParamType(field.format(), origin=FieldOrigin.FROM_DOCSTRING)

    def handle_param(self, field: Field) -> None:
        name = self._handle_param_name(field)
        if name is not None:
            if any(desc.name == name for desc in self.parameter_descs):
                field.report('Parameter "%s" was already documented' % (name,))
            self.parameter_descs.append(ParamDesc(name=name, body=field.format()))
            if name not in self.types:
                self._handle_param_not_found(name, field)

    handle_arg = handle_param

    def handle_keyword(self, field: Field) -> None:
        name = self._handle_param_name(field)
        if name is not None:
            # TODO: How should this be matched to the type annotation?
            self.parameter_descs.append(KeywordDesc(name=name, body=field.format()))
            if name in self.types:
                field.report('Parameter "%s" is documented as keyword' % (name,))


    def handled_elsewhere(self, field: Field) -> None:
        # Some fields are handled by extract_fields below.
        pass

    handle_ivar = handled_elsewhere
    handle_cvar = handled_elsewhere
    handle_var = handled_elsewhere

    def handle_raises(self, field: Field) -> None:
        name = field.arg
        if name is None:
            field.report('Exception type missing')
            typ_fmt = tags.span(class_='undocumented')("Unknown exception")
        else:
            typ_fmt = self._linker.link_to(name, name)
        self.raise_descs.append(RaisesDesc(type=typ_fmt, body=field.format()))
    handle_raise = handle_raises
    handle_except = handle_raises

    # Warns is just like raises but the syntax is more relax i.e. warning type not required.
    def handle_warns(self, field: Field) -> None:
        if field.arg is None:
            typ_fmt = None
        else:
            typ_fmt = self._linker.link_to(field.arg, field.arg)
        self.warns_desc.append(FieldDesc(type=typ_fmt, body=field.format()))

    handle_warn = handle_warns

    def handle_seealso(self, field: Field) -> None:
        self.seealsos.append(field)
    handle_see = handle_seealso

    def handle_note(self, field: Field) -> None:
        self.notes.append(field)

    def handle_author(self, field: Field) -> None:
        self.authors.append(field)

    def handle_since(self, field: Field) -> None:
        self.sinces.append(field)

    def handleUnknownField(self, field: Field) -> None:
        name = field.tag
        field.report(f"Unknown field '{name}'" )
        self.unknowns[name].append(FieldDesc(name=field.arg, body=field.format()))

    def handle(self, field: Field) -> None:
        m = getattr(self, 'handle_' + field.tag, self.handleUnknownField)
        m(field)

    def resolve_types(self) -> None:
        """Merge information from 'param'/'keyword' fields and AST analysis."""

        params = {param.name: param for param in self.parameter_descs}
        any_info = bool(params)

        # We create a new parameter_descs list to ensure the parameter order
        # matches the AST order.
        new_parameter_descs: List[Union[ParamDesc, KeywordDesc]] = []
        for index, (name, param_type) in enumerate(self.types.items()):
            try:
                param = params.pop(name)
            except KeyError:
                # parameter is not documented with @param.

                if index == 0:
                    # Strip 'self' or 'cls' from parameter table when it semantically makes sens.
                    if name=='self' and self.obj.kind is model.DocumentableKind.METHOD:
                        continue
                    if name=='cls' and self.obj.kind is model.DocumentableKind.CLASS_METHOD:
                        continue

                param = ParamDesc(name=name,
                    type=param_type.stan if param_type else None,
                    type_origin=param_type.origin if param_type else None,)

                any_info |= param_type is not None
            else:
                param.type = param_type.stan if param_type else None
                param.type_origin = param_type.origin if param_type else None

            new_parameter_descs.append(param)

        # Add any leftover parameters, which includes documented **kwargs keywords
        # and non-existing (but documented) parameters.
        new_parameter_descs += params.values()

        # Only update the descriptions if at least one parameter is documented
        # or annotated.
        if any_info:
            self.parameter_descs = new_parameter_descs

        # loops thought the parameters and remove eventual **kwargs 
        # entry if keywords are specifically documented.
        kwargs = None
        has_keywords = False
        for p in self.parameter_descs:
            if isinstance(p.name, KeywordArgument):
                kwargs = p
                continue
            if isinstance(p, KeywordDesc):
                has_keywords = True
        if kwargs:
            self.parameter_descs.remove(kwargs)
            if not has_keywords or kwargs.is_documented():
                # make sure **kwargs row is presented last in the parameter table
                self.parameter_descs.append(kwargs)

    def format(self) -> Tag:
        r: List[Tag] = []

        # Only include parameter or return sections if any are documented or any type are documented from @type fields.
        include_params = False
        if any(p.is_documented() for p in self.parameter_descs):
            r += format_desc_list('Parameters', self.parameter_descs)
            include_params = True

        if self.return_desc and (include_params or self.return_desc.is_documented()):
            r += format_desc_list('Returns', [self.return_desc])

        if self.yields_desc:
            r += format_desc_list('Yields', [self.yields_desc])

        r += format_desc_list("Raises", self.raise_descs)
        r += format_desc_list("Warns", self.warns_desc)
        for s_p_l in (('Author', 'Authors', self.authors),
                      ('See Also', 'See Also', self.seealsos),
                      ('Present Since', 'Present Since', self.sinces),
                      ('Note', 'Notes', self.notes)):
            r += format_field_list(*s_p_l)
        for kind, fieldlist in self.unknowns.items():
            r += format_desc_list(f"Unknown Field: {kind}", fieldlist)

        return tags.transparent(*r)

def reportWarnings(obj: model.Documentable, warns: Sequence[str], **kwargs:Any) -> None:
    for message in warns:
        obj.report(message, **kwargs)

def reportErrors(obj: model.Documentable, errs: Sequence[ParseError], section:str='docstring') -> None:
    if not errs:
        return

    errors = obj.system.parse_errors[section]

    if obj.fullName() not in errors:
        errors.add(obj.fullName())

        for err in errs:
            obj.report(
                f'bad {section}: ' + err.descr(),
                lineno_offset=(err.linenum() or 1) - 1,
                section=section
                )

def _objclass(obj: model.Documentable) -> ObjClass | None:
    # There is only 4 main kinds of objects
    if isinstance(obj, model.Module):
        return 'module'
    if isinstance(obj, model.Class):
        return 'class'
    if isinstance(obj, model.Attribute):
        return 'attribute'
    if isinstance(obj, model.Function):
        return 'function'
    return None

_docformat_skip_processtypes = ('google', 'numpy', 'plaintext')
def parse_docstring(
        obj: model.Documentable,
        doc: str,
        source: model.Documentable,
        markup: Optional[str]=None,
        section: str='docstring',
        ) -> ParsedDocstring:
    """Parse a docstring.
    @param obj: The object we're parsing the documentation for.
    @param doc: The docstring.
    @param source: The object on which the docstring is defined.
        This can differ from C{obj} if the docstring is inherited.
    @param markup: Parse the docstring with the given markup, ignoring system's options.
        Useful for creating L{ParsedDocstring}s from restructuredtext for instance.
    @param section: A custom section to use.
    """

    docformat = _get_docformat(source) if not markup else markup

    # fetch the parser function
    try:
        parser = get_parser_by_name(docformat, _objclass(obj))
    except (ImportError, AttributeError) as e:
        _err = 'Error trying to fetch %r parser:\n\n    %s: %s\n\nUsing plain text formatting only.'%(
            docformat, e.__class__.__name__, e)
        obj.system.msg('epydoc2stan', _err, thresh=-1, once=True)
        parser = pydoctor.epydoc.markup.plaintext.parse_docstring

    # type processing is always enabled for google and numpy docformat,
    # it's already part of the specification, doing it now would process types twice.
    if obj.system.options.processtypes and docformat not in _docformat_skip_processtypes:
        # This allows epytext and restructuredtext markup to use TypeDocstring as well with a CLI option: --process-types.
        # It's still technically part of the parsing process, so we use a wrapper function.
        parser = processtypes(parser)

    errs: List[ParseError] = []
    try:
        # parse docstring
        parsed_doc = parser(doc, errs)
    except ParseError:
        # this error should already by stored in the errs list
        parsed_doc = pydoctor.epydoc.markup.plaintext.parse_docstring(doc, errs)
    except Exception as e:
        errs.append(ParseError(f'{e.__class__.__name__}: {e}', 1))
        parsed_doc = pydoctor.epydoc.markup.plaintext.parse_docstring(doc, errs)
    if errs:
        reportErrors(source, errs, section=section)
    return parsed_doc

def ensure_parsed_docstring(obj: model.Documentable) -> Optional[model.Documentable]:
    """
    Currently, it's not 100% clear at what point the L{Documentable.parsed_docstring} attribute is set.
    It can be set from the ast builder or later processing step.

    This function ensures that the C{parsed_docstring} attribute of a documentable is set to it's final value.

    @returns:
        - If the C{obj.parsed_docstring} is set to a L{ParsedDocstring} instance:
          The source object of the docstring (might be different
          from C{obj} if the documentation is inherited).
        - If the object is undocumented: C{None}.
    """
    doc, source = model.get_docstring(obj)

    # Use cached or split version if possible.
    parsed_doc = obj.parsed_docstring

    if source is None and parsed_doc is not None:
        # No docstring found
        # A split field is documented by its parent: meaning the parsed_docstring
        # attribute has been set directly by extract_fields() with @ivar:, @cvar:, etc
        # Get the source of the docs
        source = obj.parent

    if parsed_doc is None and doc is not None:
        # The parsed_docstring has not been initialized yet
        assert source is not None
        parsed_doc = parse_docstring(obj, doc, source)
        obj.parsed_docstring = parsed_doc

    if obj.parsed_docstring is not None:
        return source
    else:
        return None


def _get_parsed_summary(obj: model.Documentable) -> Tuple[Optional[model.Documentable], ParsedDocstring]:
    """
    Ensures that the L{model.Documentable.parsed_summary} attribute of a documentable is set to it's final value.
    Do not generate summary twice.

    @returns: Tuple: C{source}, C{parsed docstring}
    """
    source = ensure_parsed_docstring(obj)

    if obj.parsed_summary is not None:
        return (source, obj.parsed_summary)

    if source is None:
        summary_parsed_doc = parsed_text(
            format_undocumented_summary(obj), 'undocumented')
    else:
        # Tell mypy that if we found a docstring, we also have its source.
        assert obj.parsed_docstring is not None
        summary_parsed_doc = obj.parsed_docstring.get_summary()

    obj.parsed_summary = summary_parsed_doc

    return (source, summary_parsed_doc)

def get_to_stan_error(e: Exception) -> ParseError:
    return ParseError(f"{e.__class__.__name__}: {e}", 0)

def safe_to_stan(parsed_doc: ParsedDocstring,
                 linker: 'DocstringLinker',
                 ctx: model.Documentable,
                 fallback: Callable[[List[ParseError], ParsedDocstring, model.Documentable], Tag],
                 report: bool = True,
                 section:str='docstring') -> Tag:
    """
    Wraps L{ParsedDocstring.to_stan()} to catch exception and handle them in C{fallback}.
    This is used to convert docstrings as well as other colorized AST values to stan.

    @param parsed_doc: The L{ParsedDocstring} to "stanify".
    @param linker: The L{DocstringLinker} to use to resolve links.
    @param ctx: The documentable context to use to report errors, passed to the C{fallback} function.
    @param fallback: A callable that returns a fallback stan if the convertion failed.
        It can also be used to set some state on the documentable context.
        Signature::
            (errs:List[ParseError], doc:ParsedDocstring, ctx:model.Documentable) -> Tag
    @param report: Whether to report errors.
    @param section: Used for error messages.
    """
    try:
        stan = parsed_doc.to_stan(linker)
    except Exception as e:
        errs = [get_to_stan_error(e)]
        stan = fallback(errs, parsed_doc, ctx)
        if report:
            reportErrors(ctx, errs, section=section)
    return stan

def format_docstring_fallback(errs: List[ParseError], parsed_doc:ParsedDocstring, ctx:model.Documentable) -> Tag:
    if ctx.docstring is None:
        stan = BROKEN
    else:
        parsed_doc_plain = pydoctor.epydoc.markup.plaintext.parse_docstring(ctx.docstring, errs)
        stan = parsed_doc_plain.to_stan(ctx.docstring_linker)
    return stan

def _wrap_in_paragraph(body:Sequence["Flattenable"]) -> bool:
    """
    Whether to wrap the given docstring stan body inside a paragraph. 
    """
    has_paragraph = False
    for e in body:
        if isinstance(e, Tag) and e.tagName == 'p':
            has_paragraph = True
        # only check the first element of the body
        break
    return bool(len(body)>0 and not has_paragraph)

def unwrap_docstring_stan(stan:Tag) -> "Flattenable":
    """
    Unwrap the body of the given C{Tag} instance if it has a non-empty tag name and 
    ensure there is at least one paragraph. 

    @note: This is the counterpart of what we're doing in L{HTMLTranslator.should_be_compact_paragraph()}.
        Since the L{HTMLTranslator} is generic for all parsed docstrings types, it always generates compact paragraphs.

        But for docstrings, we want to have at least one paragraph for consistency.
    """
    if stan.tagName:
        return stan
    body = stan.children
    if _wrap_in_paragraph(body):
        return tags.p(*body)
    else:
        return body

def format_docstring(obj: model.Documentable) -> Tag:
    """Generate an HTML representation of a docstring"""

    source = ensure_parsed_docstring(obj)

    ret: Tag = tags.div
    if source is None:
        ret(tags.p(class_='undocumented')("Undocumented"))
    else:
        assert obj.parsed_docstring is not None, "ensure_parsed_docstring() did not do it's job"
        stan = safe_to_stan(obj.parsed_docstring, source.docstring_linker, source, fallback=format_docstring_fallback)
        ret(unwrap_docstring_stan(stan))

    fh = FieldHandler(obj)
    if isinstance(obj, model.Function):
        fh.set_param_types_from_annotations(obj.annotations)
    if source is not None:
        assert obj.parsed_docstring is not None, "ensure_parsed_docstring() did not do it's job"
        for field in obj.parsed_docstring.fields:
            fh.handle(Field.from_epydoc(field, source))
    if isinstance(obj, model.Function):
        fh.resolve_types()
    ret(fh.format())
    return ret

def format_summary_fallback(errs: List[ParseError], parsed_doc:ParsedDocstring, ctx:model.Documentable) -> Tag:
    # override parsed_summary instance variable to remember this one is broken.
    ctx.parsed_summary = parsed_text(BROKEN_TEXT, 'undocumented')
    return BROKEN

def format_summary(obj: model.Documentable) -> Tag:
    """Generate an shortened HTML representation of a docstring."""

    source, parsed_doc = _get_parsed_summary(obj)
    if not source:
        source = obj
    
    # do not optimize url in order to make sure we're always generating full urls.
    # avoids breaking links when including the summaries on other pages.
    with source.docstring_linker.switch_context(None):
        # ParserErrors will likely be reported by the full docstring as well,
        # so don't spam the log, pass report=False.
        stan = safe_to_stan(parsed_doc, source.docstring_linker, source, report=False,
                fallback=format_summary_fallback)

    return stan


def format_undocumented_summary(obj: model.Documentable) -> str:
    """Generate a string representation for an object lacking a docstring."""

    sub_objects_with_docstring_count: DefaultDict[model.DocumentableKind, int] = defaultdict(int)
    sub_objects_total_count: DefaultDict[model.DocumentableKind, int]  = defaultdict(int)
    for sub_ob in obj.contents.values():
        kind = sub_ob.kind
        if kind is not None:
            sub_objects_total_count[kind] += 1
            if sub_ob.docstring is not None:
                sub_objects_with_docstring_count[kind] += 1

    if sub_objects_with_docstring_count:

        kind = obj.kind
        assert kind is not None # if kind is None, object is invisible
        return (
            f"No {format_kind(kind).lower()} docstring; "
            + ', '.join(
                f"{sub_objects_with_docstring_count[kind]}/{sub_objects_total_count[kind]} "
                f"{format_kind(kind, plural=sub_objects_with_docstring_count[kind]>=2).lower()}"

                for kind in sorted(sub_objects_total_count, key=(lambda x:x.value))
                )
            + " documented"
            )
    else:
        return "Undocumented"


def type2stan(obj: model.Documentable) -> Optional[Tag]:
    """
    Get the formatted type of this attribute.
    """
    # Currently only used for Attribute childs.
    parsed_type = get_parsed_type(obj)
    if parsed_type is None:
        return None
    else:
        return safe_to_stan(parsed_type, obj.docstring_linker, obj,
            fallback=colorized_pyval_fallback, section='annotation')

def get_parsed_type(obj: model.Documentable) -> Optional[ParsedDocstring]:
    """
    Get the type of this attribute as parsed docstring.
    """
    parsed_type = obj.parsed_type
    if parsed_type is not None:
        return parsed_type

    # Only Attribute instances have the 'annotation' attribute.
    annotation: Optional[ast.expr] = getattr(obj, 'annotation', None)
    if annotation is not None:
        return colorize_inline_pyval(annotation, is_annotation=True)

    return None

def format_toc(obj: model.Documentable) -> Optional[Tag]:
    # Load the parsed_docstring if it's not already done.
    ensure_parsed_docstring(obj)

    if obj.parsed_docstring:
        if obj.system.options.sidebartocdepth > 0:
            toc = obj.parsed_docstring.get_toc(depth=obj.system.options.sidebartocdepth)
            if toc:
                return safe_to_stan(toc, obj.docstring_linker, obj, report=False,
                    fallback=lambda _,__,___:BROKEN)
    return None


field_name_to_kind = {
    'ivar': model.DocumentableKind.INSTANCE_VARIABLE,
    'cvar': model.DocumentableKind.CLASS_VARIABLE,
    'var': model.DocumentableKind.VARIABLE,
    }


def extract_fields(obj: model.CanContainImportsDocumentable) -> None:
    """Populate Attributes for module/class variables using fields from
    that module/class's docstring.
    Must only be called for objects that have a docstring.
    """

    doc = obj.docstring
    assert doc is not None, obj
    parsed_doc = parse_docstring(obj, doc, obj)
    obj.parsed_docstring = parsed_doc

    for field in parsed_doc.fields:
        tag = field.tag()
        if tag in ['ivar', 'cvar', 'var', 'type']:
            arg = field.arg()
            if arg is None:
                obj.report("Missing field name in @%s" % (tag,),
                           'docstring', field.lineno)
                continue
            attrobj: Optional[model.Documentable] = obj.contents.get(arg)
            if attrobj is None:
                attrobj = obj.system.Attribute(obj.system, arg, obj)
                attrobj.kind = None
                attrobj.parentMod = obj.parentMod
                obj.system.addObject(attrobj)
            lineno = model.LineFromDocstringField(obj.docstring_lineno + field.lineno)
            attrobj.setLineNumber(lineno)
            if not attrobj.docstring_lineno:
                attrobj.docstring_lineno = lineno
            if tag == 'type':
                attrobj.parsed_type = field.body()
            else:
                attrobj.parsed_docstring = field.body()
                attrobj.kind = field_name_to_kind[tag]

def format_kind(kind: model.DocumentableKind, plural: bool = False) -> str:
    """
    Transform a `model.DocumentableKind` Enum value to string.
    """
    names = {
        model.DocumentableKind.NAMESPACE_PACKAGE : 'Namespace Package',
        model.DocumentableKind.PACKAGE         : 'Package',
        model.DocumentableKind.MODULE          : 'Module',
        model.DocumentableKind.INTERFACE       : 'Interface',
        model.DocumentableKind.CLASS           : 'Class',
        model.DocumentableKind.CLASS_METHOD    : 'Class Method',
        model.DocumentableKind.STATIC_METHOD   : 'Static Method',
        model.DocumentableKind.METHOD          : 'Method',
        model.DocumentableKind.FUNCTION        : 'Function',
        model.DocumentableKind.CLASS_VARIABLE  : 'Class Variable',
        model.DocumentableKind.ATTRIBUTE       : 'Attribute',
        model.DocumentableKind.INSTANCE_VARIABLE : 'Instance Variable',
        model.DocumentableKind.PROPERTY        : 'Property',
        model.DocumentableKind.VARIABLE        : 'Variable',
        model.DocumentableKind.SCHEMA_FIELD    : 'Attribute',
        model.DocumentableKind.CONSTANT        : 'Constant',
        model.DocumentableKind.EXCEPTION       : 'Exception',
        model.DocumentableKind.TYPE_ALIAS      : 'Type Alias',
        model.DocumentableKind.TYPE_VARIABLE   : 'Type Variable',
    }
    plurals = {
        model.DocumentableKind.CLASS           : 'Classes',
        model.DocumentableKind.PROPERTY        : 'Properties',
        model.DocumentableKind.TYPE_ALIAS      : 'Type Aliases',
    }
    if plural:
        return plurals.get(kind, names[kind] + 's')
    else:
        return names[kind]

def colorized_pyval_fallback(_: List[ParseError], doc:ParsedDocstring, __:model.Documentable) -> Tag:
    """
    This fallback function uses L{ParsedDocstring.to_node()}, so it must be used only with L{ParsedDocstring} subclasses that implements C{to_node()}.
    """
    return tags.code(doc.to_text())

def _format_constant_value(obj: model.Attribute) -> Iterator["Flattenable"]:

    # yield the table title, "Value"
    row = tags.tr(class_="fieldStart")
    row(tags.td(class_="fieldName")("Value"))
    # yield the first row.
    yield row

    doc = colorize_pyval(obj.value,
        linelen=obj.system.options.pyvalreprlinelen,
        maxlines=obj.system.options.pyvalreprmaxlines)

    value_repr = safe_to_stan(doc, obj.docstring_linker, obj,
        fallback=colorized_pyval_fallback, section='rendering of constant')

    # Report eventual warnings. It warns when a regex failed to parse.
    reportWarnings(obj, doc.warnings, section='colorize constant')

    # yield the value repr.
    row = tags.tr()
    row(tags.td(tags.pre(class_='constant-value')(value_repr)))
    yield row

def format_constant_value(obj: model.Attribute) -> "Flattenable":
    """
    Should be only called for L{Attribute} objects that have the L{Attribute.value} property set.
    """
    rows = list(_format_constant_value(obj))
    return tags.table(class_='valueTable')(*rows)

def _split_indentifier_parts_on_case(indentifier:str) -> List[str]:

    def split(text:str, sep:str) -> List[str]:
        # We use \u200b as temp token to hack a split that passes the tests.
        return text.replace(sep, '\u200b'+sep).split('\u200b')

    match = re.match('(_{1,2})?(.*?)(_{1,2})?$', indentifier)
    assert match is not None # the regex always matches
    prefix, text, suffix = match.groups(default='')
    text_parts = []

    if text.islower() or text.isupper():
        # We assume snake_case or SCREAMING_SNAKE_CASE.
        text_parts = split(text, '_')
    else:
        # We assume camelCase.  We're not using a regex because we also want it
        # to work with non-ASCII characters (and the Python re module does not
        # support checking for Unicode properties using something like \p{Lu}).
        current_part = ''
        previous_was_upper = False
        for c in text:

            if c.isupper() and not previous_was_upper:
                text_parts.append(current_part)
                current_part = ''

            current_part += c
            previous_was_upper = c.isupper()

        if current_part:
            text_parts.append(current_part)

    if not text_parts: # the name is composed only by underscores
        text_parts = ['']

    if prefix:
        text_parts[0] = prefix + text_parts[0]
    if suffix:
        text_parts[-1] = text_parts[-1] + suffix

    return text_parts

def insert_break_points(text: str) -> 'Flattenable':
    """
    Browsers aren't smart enough to recognize word breaking opportunities in
    snake_case or camelCase, so this function helps them out by inserting
    word break opportunities.

    :note: It support full dotted names and will add a wbr tag after each dot.
    """

    # We use tags.wbr instead of zero-width spaces because
    # zero-width spaces can interfer in subtle ways when copy/pasting a name.

    r: List['Flattenable'] = []
    parts = text.split('.')
    for i,t in enumerate(parts):
        _parts = _split_indentifier_parts_on_case(t)
        for i_,p in enumerate(_parts):
            r += [p]
            if i_ != len(_parts)-1:
                r += [tags.wbr()]
        if i != len(parts)-1:
            r += [tags.wbr(), '.']
    return tags.transparent(*r)

def format_constructor_short_text(constructor: model.Function, forclass: model.Class) -> str:
    """
    Returns a simplified signature of the constructor.
    C{forclass} is not always the function's parent, it can be a subclass.
    """
    args = ''
    # for signature with more than 5 parameters, 
    # we just show the elipsis after the fourth parameter
    annotations = constructor.annotations.items()
    many_param = len(annotations) > 6
    
    for index, (name, ann) in enumerate(annotations):
        if name=='return':
            continue

        if many_param and index > 4:
            args += ', ...'
            break
        
        # Special casing __new__ because it's actually a static method
        if index==0 and (constructor.name in ('__new__', '__init__') or 
                         constructor.kind is _CLASS_METHOD):
            # Omit first argument (self/cls) from simplified signature.
            continue
        star = ''
        if isinstance(name, VariableArgument):
            star='*'
        elif isinstance(name, KeywordArgument):
            star='**'
        
        if args:
            args += ', '
        
        args += f"{star}{name}"
    
    # display innner classes with their name starting at the top level class.
    _current:model.CanContainImportsDocumentable = forclass
    class_name = [] 
    while isinstance(_current, model.Class):
        class_name.append(_current.name)
        _current = _current.parent
    
    callable_name = '.'.join(reversed(class_name))

    if constructor.name not in ('__new__', '__init__'):
        # We assume that the constructor is a method accessible in the Class.

        callable_name += f'.{constructor.name}'

    return f"{callable_name}({args})"

def get_constructors_extra(cls:model.Class) -> ParsedDocstring | None:
    """
    Get an extra docstring to represent Class constructors.
    """
    from pydoctor.templatewriter import util
    constructors = cls.public_constructors
    if not constructors:
        return None
    
    document = new_document('docstring')

    elements: list[nodes.Node] = []
    plural = 's' if len(constructors)>1 else ''
    elements.append(set_node_attributes(
        nodes.Text(f'Constructor{plural}: '), 
        document=document, 
        lineno=1))

    for i, c in enumerate(sorted(constructors, 
                    key=util.alphabetical_order_func)):
        if i != 0:
            elements.append(set_node_attributes(
                nodes.Text(', '), 
                document=document, 
                lineno=1))
        short_text = format_constructor_short_text(c, cls)
        elements.append(set_node_attributes(
            nodes.title_reference('', '', refuri=c.fullName()), 
            document=document, 
            children=[set_node_attributes(
                nodes.Text(short_text), 
                document=document, 
                lineno=1
                )], 
                lineno=1))
    
    set_node_attributes(document, children=elements)
    return ParsedRstDocstring(document, ())

def get_namespace_docstring(ns: model.Package) -> str:
    """
    Get a useful description about this namespace package.
    """
    # Something like: 
    # Contains 1 known namespace packages, 3 known packages, 2 known modules
    # Empty
    if not ns.contents:
        text = 'Empty'
    else:
        sub_objects_total_count: DefaultDict[model.DocumentableKind, int]  = defaultdict(int)
        for sub_ob in ns.contents.values():
            kind = sub_ob.kind
            if kind is not None:
                sub_objects_total_count[kind] += 1
        
        text = 'Contains ' + ', '.join(
                f"{sub_objects_total_count[kind]} known "
                f"{format_kind(kind, plural=sub_objects_total_count[kind]>=2).lower()}"
                for kind in sorted(sub_objects_total_count, key=(lambda x:x.value))
                ) + '.'

    return text

_empty = inspect.Parameter.empty
_POSITIONAL_ONLY = inspect.Parameter.POSITIONAL_ONLY
_POSITIONAL_OR_KEYWORD = inspect.Parameter.POSITIONAL_OR_KEYWORD
_VAR_KEYWORD = inspect.Parameter.VAR_KEYWORD
_VAR_POSITIONAL = inspect.Parameter.VAR_POSITIONAL
_KEYWORD_ONLY = inspect.Parameter.KEYWORD_ONLY

def _colorize_signature_annotation(annotation: object) -> list[nodes.Node]:
    """
    Returns this annotation as a list of nodes
    """
    return colorize_inline_pyval(annotation, is_annotation=True).to_node().children

_METHOD = model.DocumentableKind.METHOD
_CLASS_METHOD = model.DocumentableKind.CLASS_METHOD
def _is_less_important_param(param: inspect.Parameter, ctx: model.Documentable) -> bool:
    """
    Whether this parameter is the 'self' param of methods or 'cls' param of class methods.
    
    @Note: this does not check whether the parameter is the first of the signature.  
        This should be done before calling this function!
    """
    if param.kind not in (_POSITIONAL_OR_KEYWORD, _POSITIONAL_ONLY):
        return False
    if (param.name == 'self' and ctx.kind is _METHOD) or (
        param.name == 'cls' and ctx.kind is _CLASS_METHOD):
        return param.annotation is _empty and param.default is _empty
    return False

# From inspect.Parameter.__str__() (Python 3.13)
def _colorize_signature_param(param: inspect.Parameter, 
                              ctx: model.Documentable, 
                              has_next: bool, 
                              is_first: bool, ) -> nodes.inline:
    """
    Convert a single parameter to a docutils inline element.
    """
    kind = param.kind
    result: list[nodes.Node] = []
    if kind == _VAR_POSITIONAL:
        result.append(nodes.Text(f'*{param.name}'))
    elif kind == _VAR_KEYWORD:
        result.append(nodes.Text(f'**{param.name}'))
    elif is_first and _is_less_important_param(param, ctx):
        result.append(text_node(param.name, 'undocumented'))
    else:
        result.append(nodes.Text(param.name))
    
    # Add annotation and default value
    if param.annotation is not _empty:
        result.append(nodes.Text(': '))
        result.append(set_node_attributes(code('', ''), 
                        children=_colorize_signature_annotation(param.annotation)))

    if param.default is not _empty:
        if param.annotation is not _empty:
            result.append(nodes.Text(' = '))
        else:
            result.append(nodes.Text('='))
        
        result.extend(colorize_inline_pyval(param.default).to_node())

    if has_next:
        result.append(nodes.Text(', '))
    
    # use the same css class as Sphinx, but rst- prefix will be added.
    return set_node_attributes(nodes.inline('', '', classes=['sig-param']),
                children=result)

# From inspect.Signature.format() (Python 3.13)
def _colorize_signature(sig: inspect.Signature, 
                        ctx: model.Documentable) -> ParsedDocstring:
    """
    Colorize this signature into a ParsedDocstring.
    """
    result: list[nodes.Node] = []
    render_pos_only_separator = False
    render_kw_only_separator = True
    param_number = len(sig.parameters)
    result.append(nodes.Text('('))

    for i, param in enumerate(sig.parameters.values()):
        kind = param.kind
        has_next = (i+1 < param_number)

        if kind == _POSITIONAL_ONLY:
            render_pos_only_separator = True
        elif render_pos_only_separator:
            # It's not a positional-only parameter, and the flag
            # is set to 'True' (there were pos-only params before.)
            result.append(text_node('/, ', 'sig-symbol'))
            render_pos_only_separator = False

        if kind == _VAR_POSITIONAL:
            # OK, we have an '*args'-like parameter, so we won't need
            # a '*' to separate keyword-only arguments
            render_kw_only_separator = False
        elif kind == _KEYWORD_ONLY and render_kw_only_separator:
            # We have a keyword-only parameter to render and we haven't
            # rendered an '*args'-like parameter before, so add a '*'
            # separator to the parameters list ("foo(arg1, *, arg2)" case)
            result.append(text_node('*, ', 'sig-symbol'))
            # This condition should be only triggered once, so
            # reset the flag
            render_kw_only_separator = False

        result.append(_colorize_signature_param(param, ctx, 
                        has_next=has_next or render_pos_only_separator, 
                        is_first=i==0))
    
    if render_pos_only_separator:
        # There were only positional-only parameters, hence the
        # flag was not reset to 'False'
        result.append(text_node('/', 'sig-symbol'))
     
    result.append(nodes.Text(')'))

    if sig.return_annotation is not _empty:
        result.append(nodes.Text(' -> '))
        result.append(set_node_attributes(code('', ''), 
                        children=_colorize_signature_annotation(sig.return_annotation)))

    return ParsedRstDocstring(set_node_attributes(
        new_document('code'), children=result), ())

def get_parsed_signature(func: model.Function | model.FunctionOverload) -> ParsedDocstring | None:
    if (psig:=func.parsed_signature) is not None:
        return psig
    
    if (signature:=func.signature) is None:
        return None

    ctx = func.primary if isinstance(func, model.FunctionOverload) else func
    func.parsed_signature = psig = _colorize_signature(signature, ctx)
    return psig

def function_signature_len(func: model.Function | model.FunctionOverload) -> int:
    """
    The lenght of the a function def is defnied by the lenght of it's name plus the lenght of it's signature.
    On top of that, a function or method that takes no argument (expect unannotated 'self' for methods, and 'cls' for classmethods) 
    will always have a lenght equals to the function name len plus two for 'function()'.
    """
    ctx = func.primary if isinstance(func, model.FunctionOverload) else func
    name_len = len(ctx.name)

    if (sig:=func.signature) is None or (
        psig:=get_parsed_signature(func)) is None:
        return name_len + 2 # bogus function def
    
    nargs = len(sig.parameters)
    if nargs == 0:
        # no arguments at all
        return name_len + 2
    
    param1 = next(iter(sig.parameters.values()))
    if _is_less_important_param(param1, ctx):
        nargs -= 1
    if nargs == 0:
        # method with only unannotated self/cls parameter
        return name_len + 2
    
    name_len = len(ctx.name)
    signature_len = len(psig.to_text())
    return name_len + signature_len
    
