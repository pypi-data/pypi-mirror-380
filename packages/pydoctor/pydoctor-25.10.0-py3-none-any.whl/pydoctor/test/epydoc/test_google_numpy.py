from typing import List
from pydoctor.epydoc.markup import ParseError
from unittest import TestCase
from pydoctor.test import NotFoundLinker
from pydoctor.model import Attribute, Class, Module, System, Function
from pydoctor.stanutils import flatten
from pydoctor.epydoc2stan import _objclass

from pydoctor.epydoc.markup.google import get_parser as get_google_parser
from pydoctor.epydoc.markup.numpy import get_parser as get_numpy_parser


class TestGetParser(TestCase):

    def test_get_google_parser_attribute(self) -> None:

        obj = Attribute(system = System(), name='attr1')

        parse_docstring = get_google_parser(_objclass(obj))


        docstring = """\
numpy.ndarray: super-dooper attribute"""

        errors: List[ParseError] = []

        parsed_doc = parse_docstring(docstring, errors)

        actual = flatten(parsed_doc.fields[-1].body().to_stan(NotFoundLinker()))
        
        expected = """<code><a>numpy.ndarray</a></code>"""

        self.assertEqual(expected, actual)
        self.assertEqual(errors, [])

    def test_get_google_parser_not_attribute(self) -> None:

        obj = Function(system = System(), name='whatever')

        parse_docstring = get_google_parser(_objclass(obj))


        docstring = """\
numpy.ndarray: super-dooper attribute"""

        errors: List[ParseError] = []

        assert not parse_docstring(docstring, errors).fields

    # the numpy inline attribute parsing is the same as google-style
    # as shown in the example_numpy.py from Sphinx docs
    def test_get_numpy_parser_attribute(self) -> None:

        obj = Attribute(system = System(), name='attr1')

        parse_docstring = get_numpy_parser(_objclass(obj))


        docstring = """\
numpy.ndarray: super-dooper attribute"""

        errors: List[ParseError] = []
        
        parsed_doc = parse_docstring(docstring, errors)

        actual = flatten(parsed_doc.fields[-1].body().to_stan(NotFoundLinker()))

        expected = """<code><a>numpy.ndarray</a></code>"""

        self.assertEqual(expected, actual)
        self.assertEqual(errors, [])

    def test_get_numpy_parser_not_attribute(self) -> None:

        obj = Function(system = System(), name='whatever')

        parse_docstring = get_numpy_parser(_objclass(obj))


        docstring = """\
numpy.ndarray: super-dooper attribute"""

        errors: List[ParseError] = []

        assert not parse_docstring(docstring, errors).fields


    def test_get_parser_for_modules_does_not_generates_ivar(self) -> None:
        
        obj = Module(system = System(), name='thing')

        parse_docstring = get_google_parser(_objclass(obj))


        docstring = """\
Attributes:
  i: struff
  j: thing
  """

        errors: List[ParseError] = []
        parsed_doc = parse_docstring(docstring, errors)
        assert [f.tag() for f in parsed_doc.fields] == ['var', 'var']


    def test_get_parser_for_classes_generates_ivar(self) -> None:
        
        obj = Class(system = System(), name='thing')

        parse_docstring = get_google_parser(_objclass(obj))


        docstring = """\
Attributes:
  i: struff
  j: thing
  """

        errors: List[ParseError] = []
        parsed_doc = parse_docstring(docstring, errors)
        assert [f.tag() for f in parsed_doc.fields] == ['ivar', 'ivar']


class TestWarnings(TestCase):

    def test_warnings(self) -> None:
        
        obj = Function(system = System(), name='func')

        parse_docstring = get_numpy_parser(_objclass(obj))


        docstring = """
Description of the function. 

Some more text.

Some more text.

Some more text.

Some more text.

Args
----
my attr: 'bar or 'foo'
        super-dooper attribute
a valid typed param: List[Union[str, bytes]]
        Description.
other: {hello
        Choices.

Returns
-------
'spam' or 'baz, optional
        A string.

Note
----
Some more text.
"""

        errors: List[ParseError] = []

        parse_docstring(docstring, errors)
        
        self.assertEqual(len(errors), 3)
        
        self.assertIn("malformed string literal (missing closing quote)", errors[2].descr())
        self.assertIn("invalid value set (missing closing brace)", errors[1].descr())
        self.assertIn("malformed string literal (missing opening quote)", errors[0].descr())
        
        #FIXME: It should be 23 actually: https://github.com/twisted/pydoctor/issues/807
        self.assertEqual(errors[2].linenum(), 20) 
        self.assertEqual(errors[1].linenum(), 17)
        self.assertEqual(errors[0].linenum(), 13)

        
