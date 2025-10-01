# xmlKit

| &nbsp; | &nbsp; |
| :--- | ---: |
| `xmlKit` is a fork of `xmltodict` to add new features. It is a Python module that makes working with XML feel like you are working with [JSON](http://docs.python.org/library/json.html), as in this ["spec"](http://www.xml.com/pub/a/2006/05/31/converting-between-xml-and-json.html): | <a href="https://k-tec.uk/?utm_source=gitlab&utm_medium=readme&utm_campaign=xmlKit" title="K-TEC Systems Ltd"> <picture> <img src="https://k-tec.uk/wp-content/uploads/2022/04/logo-colour-cropped-max.svg" alt="K-TEC Systems Ltd" width="200"> </picture> </a> <br /> <strong>Brought to you by <br /> <a href="https://k-tec.uk/?utm_source=gitlab&utm_medium=readme&utm_campaign=xmlKit">K-TEC Systems Ltd</a></strong> |

```python
>>> print(json.dumps(xmlkit.parse("""
...  <mydocument has="an attribute">
...    <and>
...      <many>elements</many>
...      <many>more elements</many>
...    </and>
...    <plus a="complex">
...      element as well
...    </plus>
...  </mydocument>
...  """), indent=4))
{
    "mydocument": {
        "@has": "an attribute",
        "and": {
            "many": [
                "elements",
                "more elements"
            ]
        },
        "plus": {
            "@a": "complex",
            "#text": "element as well"
        }
    }
}
```

## Namespace support

By default, `xmlKit` does no XML namespace processing (it just treats namespace declarations as regular node attributes), but passing `process_namespaces=True` will make it expand namespaces for you:

```python
>>> xml = """
... <root xmlns="http://defaultns.com/"
...       xmlns:a="http://a.com/"
...       xmlns:b="http://b.com/">
...   <x>1</x>
...   <a:y>2</a:y>
...   <b:z>3</b:z>
... </root>
... """
>>> xmlkit.parse(xml, process_namespaces=True) == {
...     'http://defaultns.com/:root': {
...         'http://defaultns.com/:x': '1',
...         'http://a.com/:y': '2',
...         'http://b.com/:z': '3',
...     }
... }
True
```

It also lets you collapse certain namespaces to shorthand prefixes, or skip them altogether:

```python
>>> namespaces = {
...     'http://defaultns.com/': None, # skip this namespace
...     'http://a.com/': 'ns_a', # collapse "http://a.com/" -> "ns_a"
... }
>>> xmlkit.parse(xml, process_namespaces=True, namespaces=namespaces) == {
...     'root': {
...         'x': '1',
...         'ns_a:y': '2',
...         'http://b.com/:z': '3',
...     },
... }
True
```

## Streaming mode

`xmlKit` is very fast ([Expat](http://docs.python.org/library/pyexpat.html)-based) and has a streaming mode with a small memory footprint, suitable for big XML dumps like [Discogs](http://discogs.com/data/) or [Wikipedia](http://dumps.wikimedia.org/):

```python
>>> def handle_artist(_, artist):
...     print(artist['name'])
...     return True
>>>
>>> xmlkit.parse(GzipFile('discogs_artists.xml.gz'),
...     item_depth=2, item_callback=handle_artist)
A Perfect Circle
Fantômas
King Crimson
Chris Potter
...
```

It can also be used from the command line to pipe objects to a script like this:

```python
import sys, marshal
while True:
    _, article = marshal.load(sys.stdin)
    print(article['title'])
```

```sh
$ bunzip2 enwiki-pages-articles.xml.bz2 | xmlkit.py 2 | myscript.py
AccessibleComputing
Anarchism
AfghanistanHistory
AfghanistanGeography
AfghanistanPeople
AfghanistanCommunications
Autism
...
```

Or just cache the dicts so you don't have to parse that big XML file again. You do this only once:

```sh
$ bunzip2 enwiki-pages-articles.xml.bz2 | xmlkit.py 2 | gzip > enwiki.dicts.gz
```

And you reuse the dicts with every script that needs them:

```sh
$ gunzip enwiki.dicts.gz | script1.py
$ gunzip enwiki.dicts.gz | script2.py
...
```

## Roundtripping

You can also convert in the other direction, using the `unparse()` method:

```python
>>> mydict = {
...     'response': {
...             'status': 'good',
...             'last_updated': '2014-02-16T23:10:12Z',
...     }
... }
>>> print(unparse(mydict, pretty=True))
<?xml version="1.0" encoding="utf-8"?>
<response>
	<status>good</status>
	<last_updated>2014-02-16T23:10:12Z</last_updated>
</response>
```

Text values for nodes can be specified with the `cdata_key` key in the python dict, while node properties can be specified with the `attr_prefix` prefixed to the key name in the python dict. The default value for `attr_prefix` is `@` and the default value for `cdata_key` is `#text`.

```python
>>> import xmlkit
>>>
>>> mydict = {
...     'text': {
...         '@color':'red',
...         '@stroke':'2',
...         '#text':'This is a test'
...     }
... }
>>> print(xmlkit.unparse(mydict, pretty=True))
<?xml version="1.0" encoding="utf-8"?>
<text stroke="2" color="red">This is a test</text>
```

Lists that are specified under a key in a dictionary use the key as a tag for each item. But if a list does have a parent key, for example if a list exists inside another list, it does not have a tag to use and the items are converted to a string as shown in the example below.  To give tags to nested lists, use the `expand_iter` keyword argument to provide a tag as demonstrated below. Note that using `expand_iter` will break roundtripping.

```python
>>> mydict = {
...     "line": {
...         "points": [
...             [1, 5],
...             [2, 6],
...         ]
...     }
... }
>>> print(xmlkit.unparse(mydict, pretty=True))
<?xml version="1.0" encoding="utf-8"?>
<line>
        <points>[1, 5]</points>
        <points>[2, 6]</points>
</line>
>>> print(xmlkit.unparse(mydict, pretty=True, expand_iter="coord"))
<?xml version="1.0" encoding="utf-8"?>
<line>
        <points>
                <coord>1</coord>
                <coord>5</coord>
        </points>
        <points>
                <coord>2</coord>
                <coord>6</coord>
        </points>
</line>
```

## API Reference

### xmlkit.parse()

Parse XML input into a Python dictionary.

- `xml_input`: XML input as a string, file-like object, or generator of strings.
- `encoding=None`: Character encoding for the input XML.
- `expat=expat`: XML parser module to use.
- `process_namespaces=False`: Expand XML namespaces if True.
- `namespace_separator=':'`: Separator between namespace URI and local name.
- `disable_entities=True`: Disable entity parsing for security.
- `process_comments=False`: Include XML comments if True. Comments can be preserved when enabled, but by default they are ignored. Multiple top-level comments may not be preserved in exact order.
- `xml_attribs=True`: Include attributes in output dict (with `attr_prefix`).
- `attr_prefix='@'`: Prefix for XML attributes in the dict.
- `cdata_key='#text'`: Key for text content in the dict.
- `force_cdata=False`: Force text content to be wrapped as CDATA for specific elements. This artificially wraps text content with the `cdata_key` (default '#text') regardless of whether the original XML contained CDATA sections. Can be a boolean (True/False), a tuple of element names to force CDATA for, or a callable function that receives (path, key, value) and returns True/False.
- `preserve_cdata=False`: Preserve actual CDATA sections from the XML input. When enabled, CDATA sections are preserved with the `preserve_cdata_key` (default '#raw_cdata') instead of being merged with regular text content. This feature only affects XML that already contains CDATA sections. Can be a boolean (True/False), a tuple of element names to preserve CDATA for, or a callable function that receives (path, key, value) and returns True/False.
- `preserve_cdata_key='#raw_cdata'`: Key used for preserved CDATA content in the dictionary. Default is '#raw_cdata'.
- `cdata_separator=''`: Separator string to join multiple text nodes. This joins adjacent text nodes. For example, set to a space to avoid concatenation.
- `postprocessor=None`: Function to modify parsed items.
- `dict_constructor=dict`: Constructor for dictionaries (e.g., dict).
- `strip_whitespace=True`: Remove leading/trailing whitespace in text nodes. Default is True; this trims whitespace in text nodes. Set to False to preserve whitespace exactly. When `process_comments=True`, this same flag also trims comment text; disable `strip_whitespace` if you need to preserve comment indentation or padding.
- `namespaces=None`: Mapping of namespaces to prefixes, or None to keep full URIs.
- `force_list=None`: Force list values for specific elements. Can be a boolean (True/False), a tuple of element names to force lists for, or a callable function that receives (path, key, value) and returns True/False. Useful for elements that may appear once or multiple times to ensure consistent list output.
- `item_depth=0`: Depth at which to call `item_callback`.
- `item_callback=lambda *args: True`: Function called on items at `item_depth`.
- `comment_key='#comment'`: Key used for XML comments when `process_comments=True`. Only used when `process_comments=True`. Comments can be preserved but multiple top-level comments may not retain order.

### xmlkit.unparse()

Convert a Python dictionary back into XML.

- `input_dict`: Dictionary to convert to XML.
- `output=None`: File-like object to write XML to; returns string if None.
- `encoding='utf-8'`: Encoding of the output XML.
- `full_document=True`: Include XML declaration if True.
- `short_empty_elements=False`: Use short tags for empty elements (`<tag/>`).
- `attr_prefix='@'`: Prefix for dictionary keys representing attributes.
- `cdata_key='#text'`: Key for text content in the dictionary.
- `preserve_cdata=False`: When enabled, dictionary entries with the `preserve_cdata_key` will be output as CDATA sections in the resulting XML.
- `preserve_cdata_key='#raw_cdata'`: Key used for preserved CDATA content in the input dictionary. Default is '#raw_cdata'.
- `pretty=False`: Pretty-print the XML output.
- `indent='\t'`: Indentation string for pretty printing.
- `newl='\n'`: Newline character for pretty printing.
- `expand_iter=None`: Tag name to use for items in nested lists (breaks roundtripping).

> **Note:** When building XML from dictionaries, keys whose values are empty
> lists are skipped. For example, `{'a': []}` produces no `<a>` element. Add a
> placeholder child (for example, `{'a': ['']}`) if an explicit empty container
> element is required in the output.

Note: xmlKit aims to cover the common 90% of cases. It does not preserve every XML nuance (attribute order, mixed content ordering, multiple top-level comments). For exact fidelity, use a full XML library such as lxml.

## Examples

### Selective force_cdata

The `force_cdata` parameter can be used to selectively force CDATA wrapping for specific elements:

```python
>>> xml = '<a><b>data1</b><c>data2</c><d>data3</d></a>'
>>> # Force CDATA only for 'b' and 'd' elements
>>> xmlkit.parse(xml, force_cdata=('b', 'd'))
{'a': {'b': {'#text': 'data1'}, 'c': 'data2', 'd': {'#text': 'data3'}}}

>>> # Force CDATA for all elements (original behavior)
>>> xmlkit.parse(xml, force_cdata=True)
{'a': {'b': {'#text': 'data1'}, 'c': {'#text': 'data2'}, 'd': {'#text': 'data3'}}}

>>> # Use a callable for complex logic
>>> def should_force_cdata(path, key, value):
...     return key in ['b', 'd'] and len(value) > 4
>>> xmlkit.parse(xml, force_cdata=should_force_cdata)
{'a': {'b': {'#text': 'data1'}, 'c': 'data2', 'd': {'#text': 'data3'}}}
```

### CDATA Handling: preserve_cdata vs force_cdata

#### Preserving actual CDATA sections

The `preserve_cdata` parameter preserves CDATA sections from the original XML. When enabled, CDATA content is stored using the `#raw_cdata` key (by default):

```python
>>> xml = '<root><![CDATA[content with <special> characters]]></root>'
>>> xmlkit.parse(xml, preserve_cdata=True)
{'root': {'#raw_cdata': 'content with <special> characters'}}
```

You can also specify specific elements to preserve CDATA for:

```python
>>> xml = '<root><a><![CDATA[data1]]></a><b><![CDATA[data2]]></b><c><![CDATA[data3]]></c></root>'
>>> # Preserve CDATA only for 'a' and 'c' elements
>>> xmlkit.parse(xml, preserve_cdata=('a', 'c'))
{'root': {'a': {'#raw_cdata': 'data1'}, 'b': 'data2', 'c': {'#raw_cdata': 'data3'}}}
```

#### Forcing CDATA wrapping

The `force_cdata` parameter artificially wraps text content as CDATA regardless of the original XML:

```python
>>> xml = '<a><b>data1</b><c>data2</c></a>'
>>> # Force CDATA wrapping for all text content
>>> xmlkit.parse(xml, force_cdata=True)
{'a': {'b': {'#text': 'data1'}, 'c': {'#text': 'data2'}}}
```

#### Differences

- `preserve_cdata=True`: Preserves actual CDATA sections from the original XML input, using the `#raw_cdata` key by default
- `force_cdata=True`: Forces ALL text content to be wrapped as CDATA, using the `#text` key by default

```python
>>> # Example showing the difference
>>> xml_with_cdata = '<root><![CDATA[original CDATA content]]></root>'
>>> 
>>> # Using preserve_cdata - preserves the actual CDATA from XML
>>> xmlkit.parse(xml_with_cdata, preserve_cdata=True)
{'root': {'#raw_cdata': 'original CDATA content'}}
>>> 
>>> # Using force_cdata - does not preserve original CDATA, but forces all text to be wrapped
>>> xmlkit.parse(xml_with_cdata, force_cdata=True)
{'root': {'#text': 'original CDATA content'}}
>>> 
>>> # The features can also be used together
>>> xmlkit.parse(xml_with_cdata, preserve_cdata=True, force_cdata=True)
{'root': {'#raw_cdata': 'original CDATA content'}}
```

#### Using custom CDATA keys

You can customize the dictionary keys used for CDATA content:

```python
>>> # Custom key for preserved CDATA
>>> xml = '<root><![CDATA[content]]></root>'
>>> xmlkit.parse(xml, preserve_cdata=True, preserve_cdata_key='_CDATA_')
{'root': {'_CDATA_': 'content'}}

>>> # Custom key for forced CDATA
>>> xml = '<root>text</root>'
>>> xmlkit.parse(xml, force_cdata=True, cdata_key='_FORCED_')
{'root': {'_FORCED_': 'text'}}
```

#### When to use each feature

- Use `preserve_cdata=True` when you need to maintain CDATA sections that already exist in your XML document, especially when the content contains special XML characters that need to be preserved without escaping.

- Use `force_cdata=True` when you want to ensure that certain text values are treated as CDATA sections in the resulting XML, regardless of their content.

### Selective force_list

The `force_list` parameter can be used to selectively force list values for specific elements:

```python
>>> xml = '<a><b>data1</b><b>data2</b><c>data3</c></a>'
>>> # Force lists only for 'b' elements
>>> xmlkit.parse(xml, force_list=('b',))
{'a': {'b': ['data1', 'data2'], 'c': 'data3'}}

>>> # Force lists for all elements (original behavior)
>>> xmlkit.parse(xml, force_list=True)
{'a': [{'b': ['data1', 'data2'], 'c': ['data3']}]}

>>> # Use a callable for complex logic
>>> def should_force_list(path, key, value):
...     return key in ['b'] and isinstance(value, str)
>>> xmlkit.parse(xml, force_list=should_force_list)
{'a': {'b': ['data1', 'data2'], 'c': 'data3'}}
```

## Ok, how do I get it?

### Using pypi

You just need to

```sh
$ pip install xmlkit
```

### Using uv

```sh
uv add xmlkit
```

## Security Notes

A CVE (CVE-2025-9375) was filed against `xmltodict` but is [disputed](https://github.com/martinblech/xmltodict/issues/377#issuecomment-3255691923). The root issue lies in Python’s `xml.sax.saxutils.XMLGenerator` API, which does not validate XML element names and provides no built-in way to do so. Since `xmltodict` is a thin wrapper that passes keys directly to `XMLGenerator`, the same issue exists in the standard library itself.

It has been suggested that `xml.sax.saxutils.escape()` represents a secure usage path. This is incorrect: `escape()` is intended only for character data and attribute values, and can produce invalid XML when misapplied to element names. There is currently no secure, documented way in Python’s standard library to validate XML element names.

Despite this, Fluid Attacks chose to assign a CVE to `xmltodict` while leaving the identical behavior in Python’s own standard library unaddressed. Their disclosure process also gave only 10 days from first contact to publication—well short of the 90-day industry norm—leaving no real opportunity for maintainer response. These actions reflect an inconsistency of standards and priorities that raise concerns about motivations, as they do not primarily serve the security of the broader community.

The maintainer considers this CVE invalid and will formally dispute it with MITRE.
