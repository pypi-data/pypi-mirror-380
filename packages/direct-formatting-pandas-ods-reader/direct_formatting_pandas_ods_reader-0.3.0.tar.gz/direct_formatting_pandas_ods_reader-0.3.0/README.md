# direct-formatting-pandas-ods-reader

Inspired from [pandas-ods-reader](https://github.com/iuvbio/pandas_ods_reader), but with the ability to read direct formatting. pandas-ods-reader relies on [ezodf](https://pypi.org/project/ezodf/) to extract cell content, but ezodf ignores direct formatting, so we need to go at a lower level.

The direct (italic, bold, underline, subscript, superscript, and anchors) formatting is turned into markup in the resulting pandas DataFrame.

## Dependencies

* `lxml`
* `pandas`

## Usage

```python
from direct_formatting_pandas_ods_reader import read_ods

read_ods("test/test.ods")

read_ods("test/test.ods", format="markdown")

read_ods("test/test.ods", format="html", sheet=0)

```

The `format` argument can be either `html`, `markdown` or `asciidoc`, and defaults to `asciidoc`. There is also a `sheet` argument that defaults to `0`, which corresponds to the first sheet of the file.

## License

Licensed under the GNU GPL v3.0, [Yann Trividic](https://yanntrividic.fr).