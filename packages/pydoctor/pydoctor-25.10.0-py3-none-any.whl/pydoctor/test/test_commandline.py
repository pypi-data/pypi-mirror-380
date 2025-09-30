from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
import re
import sys

import pytest

from pydoctor.options import Options
from pydoctor import driver

from . import CapSys


def geterrtext(*options: str) -> str:
    """
    Run CLI with options and return the output triggered by system exit.
    """
    se = sys.stderr
    f = StringIO()
    print(options)
    sys.stderr = f
    try:
        try:
            driver.main(list(options))
        except SystemExit:
            pass
        else:
            assert False, "did not fail"
    finally:
        sys.stderr = se
    return f.getvalue()

def test_invalid_option() -> None:
    err = geterrtext('--no-such-option')
    assert 'unrecognized arguments: --no-such-option' in err

def test_cannot_advance_blank_system() -> None:
    err = geterrtext('--make-html')
    assert 'No source paths given' in err

def test_no_systemclasses_py3() -> None:
    err = geterrtext('--system-class')
    assert 'expected one argument' in err

def test_invalid_systemclasses() -> None:
    err = geterrtext('--system-class=notdotted')
    assert 'dotted name' in err
    err = geterrtext('--system-class=no-such-module.System')
    assert 'could not import module' in err
    err = geterrtext('--system-class=pydoctor.model.Class')
    assert 'is not a subclass' in err


def test_projectbasedir_absolute(tmp_path: Path) -> None:
    """
    The --project-base-dir option, when given an absolute path, should set that
    path as the projectbasedirectory attribute on the options object.

    Previous versions of this test tried using non-existing paths and compared
    the string representations, but that was unreliable, since the input path
    might contain a symlink that will be resolved, such as "/home" on macOS.
    Using L{Path.samefile()} is reliable, but requires an existing path.
    """
    assert tmp_path.is_absolute()
    options = Options.from_args(["--project-base-dir", str(tmp_path)])
    assert options.projectbasedirectory is not None
    assert options.projectbasedirectory.samefile(tmp_path)
    assert options.projectbasedirectory.is_absolute()


@pytest.mark.skipif("platform.python_implementation() == 'PyPy' and platform.system() == 'Windows'")
def test_projectbasedir_symlink(tmp_path: Path) -> None:
    """
    The --project-base-dir option, when given a path containing a symbolic link,
    should resolve the path to the target directory.
    """
    target = tmp_path / 'target'
    target.mkdir()
    link = tmp_path / 'link'
    link.symlink_to('target', target_is_directory=True)
    assert link.samefile(target)

    options = Options.from_args(["--project-base-dir", str(link)])
    assert options.projectbasedirectory is not None
    assert options.projectbasedirectory.samefile(target)
    assert options.projectbasedirectory.is_absolute()


def test_projectbasedir_relative() -> None:
    """
    The --project-base-dir option, when given a relative path, should convert
    that path to absolute and set it as the projectbasedirectory attribute on
    the options object.
    """
    relative = "projbasedirvalue"
    options = Options.from_args(["--project-base-dir", relative])
    assert options.projectbasedirectory is not None
    assert options.projectbasedirectory.is_absolute()
    assert options.projectbasedirectory.name == relative
    assert options.projectbasedirectory.parent == Path.cwd()


def test_help_option(capsys: CapSys) -> None:
    """
    pydoctor --help 
    """
    try:
        driver.main(args=['--help'])
    except SystemExit:
        assert '--project-name PROJECTNAME' in capsys.readouterr().out
    else:
        assert False

def test_cache_enabled_by_default() -> None:
    """
    Intersphinx object caching is enabled by default.
    """
    options = Options.defaults()
    assert options.enable_intersphinx_cache


def test_cli_warnings_on_error() -> None:
    """
    The --warnings-as-errors option is disabled by default.
    This is the test for the long form of the CLI option.
    """
    options = Options.defaults()
    assert options.warnings_as_errors == False

    options = Options.from_args(['--warnings-as-errors'])
    assert options.warnings_as_errors == True


def test_project_version_default() -> None:
    """
    When no --project-version is provided, it will default empty string.
    """
    options = Options.defaults()
    assert options.projectversion == ''


def test_project_version_string() -> None:
    """
    --project-version can be passed as a simple string.
    """
    options = Options.from_args(['--project-version', '1.2.3.rc1'])
    assert options.projectversion == '1.2.3.rc1'


def test_main_project_name_guess(capsys: CapSys) -> None:
    """
    When no project name is provided in the CLI arguments, a default name
    is used and logged.
    """
    exit_code = driver.main(args=[
        '-v', '--testing',
        'pydoctor/test/testpackages/basic/'
        ])

    assert exit_code == 0
    assert "Guessing 'basic' for project name." in capsys.readouterr().out


def test_main_project_name_option(capsys: CapSys) -> None:
    """
    When a project name is provided in the CLI arguments nothing is logged.
    """
    exit_code = driver.main(args=[
        '-v', '--testing',
        '--project-name=some-name',
        'pydoctor/test/testpackages/basic/'
        ])

    assert exit_code == 0
    assert 'Guessing ' not in capsys.readouterr().out


def test_main_return_zero_on_warnings() -> None:
    """
    By default it will return 0 as exit code even when there are warnings.
    """
    stream = StringIO()
    with redirect_stdout(stream):
        exit_code = driver.main(args=[
            '--html-writer=pydoctor.test.InMemoryWriter',
            'pydoctor/test/testpackages/report_trigger/'
            ])

    assert exit_code == 0
    assert "__init__.py:8: Unknown field 'bad_field'" in stream.getvalue()
    assert 'report_module.py:9: Cannot find link target for "BadLink"' in stream.getvalue()


def test_main_return_non_zero_on_warnings() -> None:
    """
    When `-W` is used it returns 3 as exit code when there are warnings.
    """
    stream = StringIO()
    with redirect_stdout(stream):
        exit_code = driver.main(args=[
            '-W',
            '--html-writer=pydoctor.test.InMemoryWriter',
            'pydoctor/test/testpackages/report_trigger/'
            ])

    assert exit_code == 3
    assert "__init__.py:8: Unknown field 'bad_field'" in stream.getvalue()
    assert 'report_module.py:9: Cannot find link target for "BadLink"' in stream.getvalue()


@pytest.mark.skipif("platform.python_implementation() == 'PyPy' and platform.system() == 'Windows'")
def test_main_symlinked_paths(tmp_path: Path) -> None:
    """
    The project base directory and package/module directories are normalized
    in the same way, such that System.setSourceHref() can call Path.relative_to()
    on them.
    """
    link = tmp_path / 'src'
    link.symlink_to(Path.cwd(), target_is_directory=True)

    exit_code = driver.main(args=[
        '--project-base-dir=.',
        '--html-viewsource-base=http://example.com',
        f'{link}/pydoctor/test/testpackages/basic/'
        ])
    assert exit_code == 0


def test_main_source_outside_basedir(capsys: CapSys) -> None:
    """
    If a --project-base-dir is given, all package and module paths should
    be located inside that base directory if source links wants to be generated.
    Otherwise it's OK, but no source links will be genrated
    """
    assert driver.main(args=[
        '--html-viewsource-base=notnone',
        '--project-base-dir=docs',
        'pydoctor/test/testpackages/basic/'
        ]) == 0
    re.match("No source links can be generated for module .+/pydoctor/test/testpackages/basic/: source path lies outside base directory .+/docs\n", 
        capsys.readouterr().out)

    assert driver.main(args=[
        '--project-base-dir=docs',
        'pydoctor/test/testpackages/basic/'
        ]) == 0
    assert "No source links can be generated" not in capsys.readouterr().out

    assert driver.main(args=[
        '--html-viewsource-base=notnone',
        '--project-base-dir=pydoctor/test/testpackages/',
        'pydoctor/test/testpackages/basic/'
        ]) == 0
    assert "No source links can be generated" not in capsys.readouterr().out


def test_make_intersphix(tmp_path: Path) -> None:
    """
    --make-intersphinx without --make-html will only produce the Sphinx inventory object.

    This is also an integration test for the Sphinx inventory writer.
    """
    inventory = tmp_path / 'objects.inv'
    exit_code = driver.main(args=[
        '--project-base-dir=.',
        '--make-intersphinx',
        '--project-name=acme-lib',
        '--project-version=20.12.0-dev123',
        '--html-output', str(tmp_path),
        'pydoctor/test/testpackages/basic/'
        ])

    assert exit_code == 0
    # No other files are created, other than the inventory.
    assert [p.name for p in tmp_path.iterdir()] == ['objects.inv']
    assert inventory.is_file()
    assert b'Project: acme-lib\n# Version: 20.12.0-dev123\n' in inventory.read_bytes()

def test_index_symlink(tmp_path: Path) -> None:
    """
    Test that the default behaviour is to create symlinks, at least on unix.

    For windows users, this has not been a success, so we automatically fallback to copying the file now.
    See https://github.com/twisted/pydoctor/issues/808, https://github.com/twisted/pydoctor/issues/720.
    """
    import platform
    exit_code = driver.main(args=['--html-output', str(tmp_path), 'pydoctor/test/testpackages/basic/'])
    assert exit_code == 0
    link = (tmp_path / 'basic.html')
    assert link.exists()
    if platform.system() == 'Windows':
        assert link.is_symlink() or link.is_file()
    else:
        assert link.is_symlink()

def test_index_hardlink(tmp_path: Path) -> None:
    """
    Test for option --use-hardlink wich enforce the usage of harlinks.
    """
    exit_code = driver.main(args=['--use-hardlink', '--html-output', str(tmp_path), 'pydoctor/test/testpackages/basic/'])
    assert exit_code == 0
    assert (tmp_path / 'basic.html').exists()
    assert not (tmp_path / 'basic.html').is_symlink()
    assert (tmp_path / 'basic.html').is_file()


def test_apidocs_help(tmp_path: Path) -> None:
    """
    Checks that the help page is well generated.
    """
    exit_code = driver.main(args=['--html-output', str(tmp_path), 'pydoctor/test/testpackages/basic/'])
    assert exit_code == 0
    help_page = (tmp_path / 'apidocs-help.html').read_text()
    assert '>Search</h2>' in help_page

def test_htmlbaseurl_option_all_pages(tmp_path: Path) -> None:
    """
    Check that the canonical link is included in all html pages, including summary pages.
    """
    exit_code = driver.main(args=[
        '--html-base-url=https://example.com.abcde',
        '--html-output', str(tmp_path), 'pydoctor/test/testpackages/basic/'])
    assert exit_code == 0
    for t in tmp_path.iterdir():
        if not t.name.endswith('.html'):
            continue
        filename = t.name
        if t.stem == 'basic':
            filename = 'index.html' # since we have only one module it's linked as index.html
        assert f'<link rel="canonical" href="https://example.com.abcde/{filename}"' in t.read_text(encoding='utf-8')
    
def test_html_ids_dont_look_like_python_names(tmp_path: Path) -> None:
    exit_code = driver.main(args=['--html-output', str(tmp_path), 'pydoctor/test/testpackages/basic/'])
    assert exit_code == 0
    
    for page in tmp_path.iterdir():
        if not page.is_file() or not page.name.endswith('.html'):
            continue
        # None of the html section contains an ID that looks like a python name
        text = page.read_text()
        if page.name == 'all-documents.html':
            assert re.findall(r'id="[a-z]+"', text, re.IGNORECASE) == ['id="basic"'], text
        else:
            assert re.findall(r'id="[a-z]+"', text, re.IGNORECASE) == [], text
