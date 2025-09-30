# tests/test_read_ods.py
import pandas as pd
import pytest
from direct_formatting_pandas_ods_reader import read_ods

# Expected data for each format
EXPECTED_DATA = {
    "asciidoc": [
        ["Column 1", "Column 2", "Column 3", "Column 4"],
        ["Some content in roman", "__Some other content in italics__", "A 1^st^ superscript and a __2__~__nd__~__ subscript__", None],
        ["**Some content in bold**", "**__Some content in bold and italics__**", "__Value__", None],
        ["A __word __and another__ w__o__rd__ in italics",
         "[.underline]#Some underlines#",
         "A link:https://pypi.org/project/direct-formatting-pandas-ods-reader/[__hyperlink with italic__].",
         None],
        [None, "Some other data that should be read", None, None],
    ],
    "markdown": [
        ["Column 1", "Column 2", "Column 3", "Column 4"],
        ["Some content in roman", "__Some other content in italics__", "A 1<sup>st</sup> superscript and a __2__<sub>__nd__</sub>__ subscript__", None],
        ["**Some content in bold**", "**__Some content in bold and italics__**", "__Value__", None],
        ["A __word __and another__ w__o__rd__ in italics",
         "<u>Some underlines</u>",
         "A [__hyperlink with italic__](https://pypi.org/project/direct-formatting-pandas-ods-reader/).",
         None],
        [None, "Some other data that should be read", None, None],
    ],
    "html": [
        ["Column 1", "Column 2", "Column 3", "Column 4"],
        ["Some content in roman", "<i>Some other content in italics</i>", "A 1<sup>st</sup> superscript and a <i>2</i><sub><i>nd</i></sub><i> subscript</i>", None],
        ["<b>Some content in bold</b>", "<b><i>Some content in bold and italics</i></b>", "<i>Value</i>", None],
        ["A <i>word </i>and another<i> w</i>o<i>rd</i> in italics",
         "<u>Some underlines</u>",
         'A <a href="https://pypi.org/project/direct-formatting-pandas-ods-reader/"><i>hyperlink with italic</i></a>.',
         None],
        [None, "Some other data that should be read", None, None],
    ],
    "mix": [
        ["Column 1", "Column 2", "Column 3", "Column 4"],
        ["Some content in roman", "Some other content in italics", "A 1<sup>st</sup> superscript and a <i>2</i><sub><i>nd</i></sub><i> subscript</i>", None],
        ["**Some content in bold**", "Some content in bold and italics", "<i>Value</i>", None],
        ["A __word __and another__ w__o__rd__ in italics",
         "Some underlines",
         'A <a href="https://pypi.org/project/direct-formatting-pandas-ods-reader/"><i>hyperlink with italic</i></a>.',
         None],
        [None, "Some other data that should be read", None, None],
    ],
    "none": [
        ["Column 1", "Column 2", "Column 3", "Column 4"],
        ["Some content in roman", "Some other content in italics", "A 1st superscript and a 2nd subscript", None],
        ["Some content in bold", "Some content in bold and italics", "Value", None],
        ["A word and another word in italics",
         "Some underlines",
         'A hyperlink with italic.',
         None],
        [None, "Some other data that should be read", None, None],
    ],
}


# List of formats to test
FORMATS = ["asciidoc", "markdown", "html", "mix", "none"]

@pytest.mark.parametrize("fmt", FORMATS)
def test_read_ods_formats(fmt):
    expected_df = pd.DataFrame(EXPECTED_DATA[fmt][1:], columns=EXPECTED_DATA[fmt][0])
    if fmt != "mix":
        df = read_ods("tests/test.ods", format=fmt)
    else: 
        # only for the mix, labels are used to specify the parsing
        # defaults to none
        mix = {
            "Column 1": "asciidoc",
            "Column 3": "html",
            "Column 4": "markdown",
        }
        df = read_ods("tests/test.ods", format=mix)

    # depending on how the DataFrame is build, columns names may vary
    # but we are really interested in column labels, not names.
    df.columns.name = None 
    expected_df.columns.name = None
    
    # Use pandas testing utility for clean comparison
    pd.testing.assert_frame_equal(df, expected_df)
