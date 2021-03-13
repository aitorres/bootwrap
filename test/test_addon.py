"""
Test for bootwrap/components/image.py
"""

import pytest

from bootwrap import (
    Icon,
    Separator,
    Spinner
)

from .helper import HelperHTMLParser


@pytest.mark.addon
def test_icon():
    icon = Icon('fab fa-google').as_primary()
    actual = HelperHTMLParser.parse(str(icon))
    expected = HelperHTMLParser.parse(f'''
        <i id={icon.identifier} class="fab fa-google text-primary"></i> 
    ''')
    assert actual == expected


@pytest.mark.addon
def test_separator():
    separator = Separator()
    actual = HelperHTMLParser.parse(str(separator))
    expected = HelperHTMLParser.parse('<hr/>')
    assert actual == expected


@pytest.mark.addon
def test_spinner():
    spinner = Spinner().as_primary()
    actual = HelperHTMLParser.parse(str(spinner))
    expected = HelperHTMLParser.parse(f'''
        <span id="{spinner.identifier}"
            class="spinner text-primary">
        </span>
    ''')
    assert actual == expected