#!/usr/bin/env python
"""Makes working with XML feel like you are working with JSON"""

import sys

from xml.parsers import expat
from xml.sax.saxutils import XMLGenerator, escape
from xml.sax.xmlreader import AttributesImpl
from io import StringIO
from inspect import isgenerator
from collections.abc import Mapping
from typing import Any, overload

from .types import (
    # Type aliases for commonly used complex types
    AttrValue,
    AttrDict,
    PathType,
    
    # Type aliases for callback functions
    ItemCallback,
    Postprocessor,
    Preprocessor,
    ForceOption,
    
    # Type aliases for XML input and output
    XmlInput,
    XmlOutput,
    
    # Other type aliases
    Indent,
    Namespaces,
    MappingNamespaces,
    DictConstructor,
    OptionalAttrDict,
    OptionalAttrValue,
    OptionalStr,
    OptionalMappingNamespaces,
    OptionalAny,
    Expat,
)

class ParsingInterrupted(Exception):
    pass


class _DictSAXHandler:
    path: PathType
    stack: list[tuple[OptionalAttrDict, list[str]]]
    data: list[str]
    item: OptionalAttrDict
    item_depth: int
    xml_attribs: bool
    item_callback: ItemCallback
    attr_prefix: str
    cdata_key: str
    force_cdata: ForceOption
    cdata_separator: str
    postprocessor: Postprocessor | None
    dict_constructor: DictConstructor
    strip_whitespace: bool
    namespace_separator: str
    namespaces: Namespaces
    namespace_declarations: dict[str, str]
    force_list: ForceOption
    comment_key: str
    preserve_cdata: ForceOption
    preserve_cdata_key: str
    in_cdata_section: bool
    cdata_content: list[str]
    last_data_was_cdata: bool
    
    def __init__(
        self,
        item_depth: int = 0,
        item_callback: ItemCallback = lambda *args: True,
        xml_attribs: bool = True,
        attr_prefix: str = "@",
        cdata_key: str = "#text",
        force_cdata: ForceOption = False,
        cdata_separator: str = "",
        postprocessor: Postprocessor | None = None,
        dict_constructor: DictConstructor = dict,
        strip_whitespace: bool = True,
        namespace_separator: str = ":",
        namespaces: Namespaces = None,
        force_list: ForceOption = None,
        comment_key: str = "#comment",
        preserve_cdata: ForceOption = False,
        preserve_cdata_key: str = "#raw_cdata",
    ) -> None:
        self.path = []
        self.stack = []
        self.data = []
        self.item = None
        self.item_depth = item_depth
        self.xml_attribs = xml_attribs
        self.item_callback = item_callback
        self.attr_prefix = attr_prefix
        self.cdata_key = cdata_key
        self.force_cdata = force_cdata
        self.cdata_separator = cdata_separator
        self.postprocessor = postprocessor
        self.dict_constructor = dict_constructor
        self.strip_whitespace = strip_whitespace
        self.namespace_separator = namespace_separator
        self.namespaces = namespaces
        self.namespace_declarations = dict_constructor()
        self.force_list = force_list
        self.comment_key = comment_key
        self.preserve_cdata = preserve_cdata
        self.preserve_cdata_key = preserve_cdata_key
        # CDATA tracking
        self.in_cdata_section = False
        self.cdata_content = []
        self.last_data_was_cdata = False
        self.path = []
        self.stack = []
        self.data = []
        self.item = None
        self.item_depth = item_depth
        self.xml_attribs = xml_attribs
        self.item_callback = item_callback
        self.attr_prefix = attr_prefix
        self.cdata_key = cdata_key
        self.force_cdata = force_cdata
        self.cdata_separator = cdata_separator
        self.postprocessor = postprocessor
        self.dict_constructor = dict_constructor
        self.strip_whitespace = strip_whitespace
        self.namespace_separator = namespace_separator
        self.namespaces = namespaces
        self.namespace_declarations = dict_constructor()
        self.force_list = force_list
        self.comment_key = comment_key
        self.preserve_cdata = preserve_cdata
        self.preserve_cdata_key = preserve_cdata_key
        # CDATA tracking
        self.in_cdata_section = False
        self.cdata_content = []
        self.last_data_was_cdata = False

    def _build_name(self, full_name: str) -> str:
        if self.namespaces is None:
            return full_name
        i = full_name.rfind(self.namespace_separator)
        if i == -1:
            return full_name
        namespace, name = full_name[:i], full_name[i+1:]
        try:
            short_namespace = self.namespaces[namespace]
        except KeyError:
            short_namespace = namespace
        if not short_namespace:
            return name
        else:
            return self.namespace_separator.join((short_namespace, name))

    def _attrs_to_dict(self, attrs: dict[str, str] | list[str]) -> AttrDict:
        if isinstance(attrs, dict):
            # Convert to AttrDict by ensuring values are AttrValue
            result = {}
            for k, v in attrs.items():
                result[k] = v
            return result
        return self.dict_constructor(zip(attrs[0::2], attrs[1::2]))

    def startNamespaceDecl(self, prefix: str, uri: str) -> None:
        self.namespace_declarations[prefix or ''] = uri

    def startElement(self, full_name: str, attrs: dict[str, str] | list[str]) -> None:
        name = self._build_name(full_name)
        attrs = self._attrs_to_dict(attrs)
        if self.namespace_declarations:
            if not attrs:
                attrs = self.dict_constructor()
            # Handle xmlns assignment properly by creating a proper AttrValue
            xmlns_value: AttrValue = {}
            for k, v in self.namespace_declarations.items():
                if isinstance(xmlns_value, dict):
                    xmlns_value[k] = v
            # Only assign xmlns if attrs is a dict
            if isinstance(attrs, dict):
                # Create a new dict with all the attributes plus xmlns
                updated_attrs: AttrDict = {}
                for k, v in attrs.items():
                    updated_attrs[k] = v
                updated_attrs['xmlns'] = xmlns_value
                attrs = updated_attrs
            self.namespace_declarations = self.dict_constructor()
        # Create a proper AttrDict for the path
        path_attrs: OptionalAttrDict = None
        if attrs:
            path_attrs = {}
            for k, v in attrs.items():
                path_attrs[k] = v
        self.path.append((name, path_attrs))
        if len(self.path) >= self.item_depth:
            self.stack.append((self.item, self.data))
            # Create attribute entries with proper types, but only if xml_attribs is True
            attr_entries = []
            if self.xml_attribs and attrs:
                for key, value in attrs.items():
                    key = self.attr_prefix+self._build_name(key)
                    if self.postprocessor:
                        entry = self.postprocessor(self.path, key, value)
                    else:
                        entry = (key, value)
                    if entry:
                        attr_entries.append(entry)
            # Create a new AttrDict with the entries
            new_attrs: AttrDict = {}
            for k, v in attr_entries:
                new_attrs[k] = v
            attrs = new_attrs
        else:
            attrs = None
        self.item = attrs or None
        self.data = []

    def endElement(self, full_name: str) -> None:
        name = self._build_name(full_name)
        # If we just closed an item at the streaming depth, emit it and drop it
        # without attaching it back to its parent. This avoids accumulating all
        # streamed items in memory when using item_depth > 0.
        if len(self.path) == self.item_depth:
            item = self.item
            if item is None:
                item = (None if not self.data
                        else self.cdata_separator.join(self.data))

            should_continue = self.item_callback(self.path, item)
            if not should_continue:
                raise ParsingInterrupted
            # Reset state for the parent context without keeping a reference to
            # the emitted item.
            if self.stack:
                self.item, self.data = self.stack.pop()
            else:
                self.item = None
                self.data = []
            self.path.pop()
            return
        if self.stack:
            data = (None if not self.data
                    else self.cdata_separator.join(self.data))
            item = self.item
            self.item, self.data = self.stack.pop()
            if self.strip_whitespace and data:
                data = data.strip() or None
            if data and self._should_force_cdata(name, data) and item is None:
                item = self.dict_constructor()
            # Check if we need to preserve CDATA
            if self._should_preserve_cdata(name, data) and self.last_data_was_cdata:
                # For CDATA content, we need to create a dict with self.preserve_cdata_key
                if item is not None:
                    if data:
                        item = self.push_data(item, self.preserve_cdata_key, str(data))
                    self.item = self.push_data(self.item, name, item)
                else:
                    cdata_value = str(data) if data is not None else ""
                    self.item = self.push_data(self.item, name, {self.preserve_cdata_key: cdata_value})
                # Reset the CDATA flag
                self.last_data_was_cdata = False
            else:
                if item is not None:
                    if data:
                        item = self.push_data(item, self.cdata_key, str(data))
                    self.item = self.push_data(self.item, name, item)
                else:
                    if data:
                        self.item = self.push_data(self.item, name, str(data))
                    # If data is empty or None, we still need to create an entry for the element
                    else:
                        self.item = self.push_data(self.item, name, None)
        else:
            self.item = None
            self.data = []
        self.path.pop()

    def characters(self, data: str) -> None:
        if self.preserve_cdata and self.in_cdata_section:
            # When preserving CDATA, accumulate content in cdata_content
            self.cdata_content.append(data)
        else:
            # Normal character data handling
            if not self.data:
                self.data = [data]
            else:
                self.data.append(data)
            # Reset the CDATA flag since we're not in a CDATA section
            self.last_data_was_cdata = False

    def comments(self, data: str) -> None:
        if self.strip_whitespace:
            data = data.strip()
        if data:  # Only add non-empty comments
            self.item = self.push_data(self.item, self.comment_key, data)

    def startCdataSection(self) -> None:
        """Handle the start of a CDATA section"""
        if self.preserve_cdata:
            self.in_cdata_section = True
            self.cdata_content = []

    def endCdataSection(self) -> None:
        """Handle the end of a CDATA section"""
        if self.preserve_cdata and self.in_cdata_section:
            # Join all the CDATA content
            cdata_text = self.cdata_separator.join(self.cdata_content)
            # Add the CDATA content to our regular data
            if not self.data:
                self.data = [cdata_text]
            else:
                self.data.append(cdata_text)
            # Mark that the last data was from CDATA
            self.last_data_was_cdata = True
            # Reset CDATA tracking
            self.in_cdata_section = False
            self.cdata_content = []

    def push_data(self, item: OptionalAttrDict, key: str, data: OptionalAttrValue) -> AttrDict:
        if self.postprocessor is not None and data is not None:
            result = self.postprocessor(self.path, key, data)
            if result is None:
                return item or self.dict_constructor()
            key, data = result
        if item is None:
            item = self.dict_constructor()
        # Ensure item is not None for type checking purposes
        assert item is not None
        # If data is None, we still add the key with None value
        if data is None:
            try:
                # Check if the key already exists
                value = item[key]
                # If it exists and is a list, append None to it
                if isinstance(value, list):
                    value.append(data)  # type: ignore
                else:
                    # If it exists and is not a list, convert to list
                    item[key] = [value, data]  # type: ignore
            except KeyError:
                # If the key doesn't exist, add it with None value
                # But only if we're not forcing lists
                if self._should_force_list(key, data):
                    item[key] = [data]  # type: ignore
                else:
                    item[key] = data  # type: ignore
            return item
        try:
            value = item[key]
            if isinstance(value, list):
                value.append(data)
            else:
                item[key] = [value, data]
        except KeyError:
            if self._should_force_list(key, data):
                item[key] = [data]
            else:
                item[key] = data
        return item

    def _should_force_list(self, key: str, value: AttrValue | None) -> bool:
        if not self.force_list:
            return False
        if isinstance(self.force_list, bool):
            return self.force_list
        try:
            return key in self.force_list
        except TypeError:
            # Handle the case where force_list is a callable
            # The callable expects the path (without the current element), key, and value
            # Pass the path without the current element
            path_without_current = self.path[:-1] if len(self.path) > 1 else []
            # Convert value to string if it's not None
            str_value = str(value) if value is not None else ""
            return self.force_list(path_without_current, key, str_value)

    def _should_force_cdata(self, key: str, value: OptionalStr) -> bool:
        if not self.force_cdata:
            return False
        if isinstance(self.force_cdata, bool):
            return self.force_cdata
        try:
            return key in self.force_cdata
        except TypeError:
            # Handle the case where force_cdata is a callable
            # The callable expects the path (without the current element), key, and value
            # Pass the path without the current element
            path_without_current = self.path[:-1] if len(self.path) > 1 else []
            return self.force_cdata(path_without_current, key, value or "")

    def _should_preserve_cdata(self, key: str, value: OptionalStr) -> bool:
        if not self.preserve_cdata:
            return False
        if isinstance(self.preserve_cdata, bool):
            return self.preserve_cdata
        try:
            return key in self.preserve_cdata
        except TypeError:
            # Handle the case where preserve_cdata is a callable
            # The callable expects the path (without the current element), key, and value
            # Pass the path without the current element
            path_without_current = self.path[:-1] if len(self.path) > 1 else []
            return self.preserve_cdata(path_without_current, key, value or "")


def parse(xml_input: XmlInput,
          encoding: OptionalStr = None,
          expat: Expat = expat,
          process_namespaces: bool = False,
          namespace_separator: str = ':',
          disable_entities: bool = True,
          process_comments: bool = False,
          preserve_cdata: ForceOption = False,
          preserve_cdata_key: str = "#raw_cdata",
          *,
          item_depth: int = 0,
          item_callback: ItemCallback = lambda *args: True,
          xml_attribs: bool = True,
          attr_prefix: str = "@",
          cdata_key: str = "#text",
          force_cdata: ForceOption = False,
          cdata_separator: str = "",
          postprocessor: Postprocessor | None = None,
          dict_constructor: DictConstructor = dict,
          strip_whitespace: bool = True,
          namespaces: Namespaces = None,
          force_list: ForceOption = None,
          comment_key: str = "#comment") -> dict[str, Any]:
    """Parse the given XML input and convert it into a dictionary.

    `xml_input` can either be a `string`, a file-like object, or a generator of strings.

    If `xml_attribs` is `True`, element attributes are put in the dictionary
    among regular child elements, using `@` as a prefix to avoid collisions. If
    set to `False`, they are just ignored.

    Simple example::

        >>> import xmlkit
        >>> doc = xmlkit.parse(\"\"\"
        ... <a prop="x">
        ...   <b>1</b>
        ...   <b>2</b>
        ... </a>
        ... \"\"\")
        >>> doc['a']['@prop']
        'x'
        >>> doc['a']['b']
        ['1', '2']

    If `item_depth` is `0`, the function returns a dictionary for the root
    element (default behavior). Otherwise, it calls `item_callback` every time
    an item at the specified depth is found and returns `None` in the end
    (streaming mode).

    The callback function receives two parameters: the `path` from the document
    root to the item (name-attribs pairs), and the `item` (dict). If the
    callback's return value is false-ish, parsing will be stopped with the
    :class:`ParsingInterrupted` exception.

    Streaming example::

        >>> def handle(path, item):
        ...     print('path:%s item:%s' % (path, item))
        ...     return True
        ...
        >>> xmlkit.parse(\"\"\"
        ... <a prop="x">
        ...   <b>1</b>
        ...   <b>2</b>
        ... </a>\"\"\", item_depth=2, item_callback=handle)
        path:[('a', {'prop': 'x'}), ('b', None)] item:1
        path:[('a', {'prop': 'x'}), ('b', None)] item:2

    The optional argument `postprocessor` is a function that takes `path`,
    `key` and `value` as positional arguments and returns a new `(key, value)`
    pair where both `key` and `value` may have changed. Usage example::

        >>> def postprocessor(path, key, value):
        ...     try:
        ...         return key + ':int', int(value)
        ...     except (ValueError, TypeError):
        ...         return key, value
        >>> xmlkit.parse('<a><b>1</b><b>2</b><b>x</b></a>',
        ...                 postprocessor=postprocessor)
        {'a': {'b:int': [1, 2], 'b': 'x'}}

    You can pass an alternate version of `expat` (such as `defusedexpat`) by
    using the `expat` parameter. E.g:

        >>> import defusedexpat
        >>> xmlkit.parse('<a>hello</a>', expat=defusedexpat.pyexpat)
        {'a': 'hello'}

    You can use the force_list argument to force lists to be created even
    when there is only a single child of a given level of hierarchy. The
    force_list argument is a tuple of keys. If the key for a given level
    of hierarchy is in the force_list argument, that level of hierarchy
    will have a list as a child (even if there is only one sub-element).
    The index_keys operation takes precedence over this. This is applied
    after any user-supplied postprocessor has already run.

        For example, given this input:
        <servers>
          <server>
            <name>host1</name>
            <os>Linux</os>
            <interfaces>
              <interface>
                <name>em0</name>
                <ip_address>10.0.0.1</ip_address>
              </interface>
            </interfaces>
          </server>
        </servers>

        If called with force_list=('interface',), it will produce
        this dictionary:
        {'servers':
          {'server':
            {'name': 'host1',
             'os': 'Linux'},
             'interfaces':
              {'interface':
                [ {'name': 'em0', 'ip_address': '10.0.0.1' } ] } } }

        `force_list` can also be a callable that receives `path`, `key` and
        `value`. This is helpful in cases where the logic that decides whether
        a list should be forced is more complex.


        If `process_comments` is `True`, comments will be added using `comment_key`
        (default=`'#comment'`) to the tag that contains the comment.

            For example, given this input:
            <a>
              <b>
                <!-- b comment -->
                <c>
                    <!-- c comment -->
                    1
                </c>
                <d>2</d>
              </b>
            </a>

            If called with `process_comments=True`, it will produce
            this dictionary:
            'a': {
                'b': {
                    '#comment': 'b comment',
                    'c': {

                        '#comment': 'c comment',
                        '#text': '1',
                    },
                    'd': '2',
                },
            }
        Comment text is subject to the `strip_whitespace` flag: when it is left
        at the default `True`, comments will have leading and trailing
        whitespace removed. Disable `strip_whitespace` to keep comment
        indentation or padding intact.
    """
    handler = _DictSAXHandler(
        namespace_separator=namespace_separator,
        preserve_cdata=preserve_cdata,
        preserve_cdata_key=preserve_cdata_key,
        item_depth=item_depth,
        item_callback=item_callback,
        xml_attribs=xml_attribs,
        attr_prefix=attr_prefix,
        cdata_key=cdata_key,
        force_cdata=force_cdata,
        cdata_separator=cdata_separator,
        postprocessor=postprocessor,
        dict_constructor=dict_constructor,
        strip_whitespace=strip_whitespace,
        namespaces=namespaces,
        force_list=force_list,
        comment_key=comment_key,
    )
    if isinstance(xml_input, str):
        encoding = encoding or 'utf-8'
        xml_input = xml_input.encode(encoding)
    if not process_namespaces:
        namespace_separator = None
    parser = expat.ParserCreate(
        encoding,
        namespace_separator
    )
    parser.ordered_attributes = True
    parser.StartNamespaceDeclHandler = handler.startNamespaceDecl
    parser.StartElementHandler = handler.startElement
    parser.EndElementHandler = handler.endElement
    parser.CharacterDataHandler = handler.characters
    if process_comments:
        parser.CommentHandler = handler.comments
    # Add CDATA section handlers if preserve_cdata is enabled
    if preserve_cdata:
        parser.StartCdataSectionHandler = handler.startCdataSection
        parser.EndCdataSectionHandler = handler.endCdataSection
    parser.buffer_text = True
    if disable_entities:
        def _forbid_entities(*_args, **_kwargs):
            raise ValueError("entities are disabled")

        parser.EntityDeclHandler = _forbid_entities
    if hasattr(xml_input, 'read'):
        parser.ParseFile(xml_input)
    elif isgenerator(xml_input):
        for chunk in xml_input:
            parser.Parse(chunk, False)
        parser.Parse(b'', True)
    else:
        parser.Parse(xml_input, True)
    return handler.item


def _convert_value_to_string(value: Any) -> str:
    """Convert a value to its string representation for XML output.

    Handles boolean values consistently by converting them to lowercase.
    """
    if isinstance(value, (str, bytes)):
        return value
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


def _validate_name(value: Any, kind: str) -> None:
    """Validate an element/attribute name for XML safety.

    Raises ValueError with a specific reason when invalid.

    kind: 'element' or 'attribute' (used in error messages)
    """
    if not isinstance(value, str):
        raise ValueError(f"{kind} name must be a string")
    if value.startswith("?") or value.startswith("!"):
        raise ValueError(f'Invalid {kind} name: cannot start with "?" or "!"')
    if "<" in value or ">" in value:
        raise ValueError(f'Invalid {kind} name: "<" or ">" not allowed')
    if "/" in value:
        raise ValueError(f'Invalid {kind} name: "/" not allowed')
    if '"' in value or "'" in value:
        raise ValueError(f"Invalid {kind} name: quotes not allowed")
    if "=" in value:
        raise ValueError(f'Invalid {kind} name: "=" not allowed')
    if any(ch.isspace() for ch in value):
        raise ValueError(f"Invalid {kind} name: whitespace not allowed")


def _validate_comment(value: Any) -> str:
    if isinstance(value, bytes):
        try:
            value = value.decode("utf-8")
        except UnicodeDecodeError as exc:
            raise ValueError("Comment text must be valid UTF-8") from exc
    if not isinstance(value, str):
        raise ValueError("Comment text must be a string")
    if "--" in value:
        raise ValueError("Comment text cannot contain '--'")
    if value.endswith("-"):
        raise ValueError("Comment text cannot end with '-'")
    return value


def _process_namespace(name: Any, namespaces: Namespaces, ns_sep: str = ':', attr_prefix: str = '@') -> Any:
    if not isinstance(name, str):
        return name
    if not namespaces:
        return name
    try:
        ns, name = name.rsplit(ns_sep, 1)
    except ValueError:
        pass
    else:
        ns_res = namespaces.get(ns.strip(attr_prefix))
        name = '{}{}{}{}'.format(
            attr_prefix if ns.startswith(attr_prefix) else '',
            ns_res, ns_sep, name) if ns_res else name
    return name


def _emit(key: str, value: Any, content_handler: XMLGenerator,
          attr_prefix: str = '@',
          cdata_key: str = '#text',
          depth: int = 0,
          preprocessor: Preprocessor | None = None,
          pretty: bool = False,
          newl: str = '\n',
          indent: Indent = '\t',
          namespace_separator: str = ':',
          namespaces: Namespaces = None,
          full_document: bool = True,
          expand_iter: OptionalStr = None,
          comment_key: str = '#comment',
          preserve_cdata: bool = False,
          preserve_cdata_key: str = '#raw_cdata',
          **kwargs: Any) -> None:
    if isinstance(key, str) and key == comment_key:
        comments_list = value if isinstance(value, list) else [value]
        if isinstance(indent, int):
            indent = " " * indent
        for comment_text in comments_list:
            if comment_text is None:
                continue
            comment_text = _convert_value_to_string(comment_text)
            if not comment_text:
                continue
            if pretty:
                content_handler.ignorableWhitespace(depth * indent)
            content_handler.comment(comment_text)
            if pretty:
                content_handler.ignorableWhitespace(newl)
        return

    key = _process_namespace(key, namespaces, namespace_separator, attr_prefix)
    if preprocessor is not None:
        result = preprocessor(key, value)
        if result is None:
            return
        key, value = result
    # Minimal validation to avoid breaking out of tag context
    _validate_name(key, "element")
    if not hasattr(value, '__iter__') or isinstance(value, (str, dict)):
        value = [value]
    for index, v in enumerate(value):
        if full_document and depth == 0 and index > 0:
            raise ValueError('document with multiple roots')
        if v is None:
            v = {}
        elif not isinstance(v, (dict, str)):
            if expand_iter and hasattr(v, '__iter__'):
                v = {expand_iter: v}
            else:
                v = _convert_value_to_string(v)
        if isinstance(v, str):
            v = {cdata_key: v}
        cdata = None
        attrs = {}
        children = []
        for ik, iv in v.items():
            if ik == cdata_key:
                cdata = _convert_value_to_string(iv)
                continue
            if ik == preserve_cdata_key:
                cdata = _convert_value_to_string(iv)
                continue
            if isinstance(ik, str) and ik.startswith(attr_prefix):
                ik = _process_namespace(ik, namespaces, namespace_separator,
                                        attr_prefix)
                if ik == '@xmlns' and isinstance(iv, dict):
                    for k, v in iv.items():
                        _validate_name(k, "attribute")
                        attr = 'xmlns{}'.format(f':{k}' if k else '')
                        attrs[attr] = str(v)
                    continue
                if not isinstance(iv, str):
                    iv = str(iv)
                attr_name = ik[len(attr_prefix) :]
                _validate_name(attr_name, "attribute")
                attrs[attr_name] = iv
                continue
            if isinstance(iv, list) and not iv:
                continue # Skip empty lists to avoid creating empty child elements
            children.append((ik, iv))
        if isinstance(indent, int):
            indent = ' ' * indent
        if pretty:
            content_handler.ignorableWhitespace(depth * indent)
        content_handler.startElement(key, AttributesImpl(attrs))
        if pretty and children:
            content_handler.ignorableWhitespace(newl)
        for child_key, child_value in children:
            _emit(child_key, child_value, content_handler,
                  attr_prefix, cdata_key, depth+1, preprocessor,
                  pretty, newl, indent, namespaces=namespaces,
                  namespace_separator=namespace_separator,
                  expand_iter=expand_iter, comment_key=comment_key,
                  preserve_cdata=preserve_cdata, preserve_cdata_key=preserve_cdata_key,
                  **kwargs)
        if cdata is not None:
            # Check if we need to output CDATA section
            if preserve_cdata_key in v.keys():
                # Output as CDATA section
                content_handler.cdata(cdata)
            else:
                # Output as regular character data
                content_handler.characters(cdata)
        if pretty and children:
            content_handler.ignorableWhitespace(depth * indent)
        content_handler.endElement(key)
        if pretty and depth:
            content_handler.ignorableWhitespace(newl)


class _XMLGenerator(XMLGenerator):
    def comment(self, text: str) -> None:
        text = _validate_comment(text)
        self._write(f"<!--{escape(text)}-->")
    
    def cdata(self, text: str) -> None:
        """Output CDATA section"""
        self._write(f"<![CDATA[{text}]]>")


@overload
def unparse(input_dict: Mapping[str, Any], 
            output: XmlOutput,
            encoding: str = "utf-8", 
            full_document: bool = True,
            short_empty_elements: bool = False, 
            comment_key: str = "#comment",
            *,
            attr_prefix: str = "@",
            cdata_key: str = "#text",
            depth: int = 0,
            preprocessor: Preprocessor | None = None,
            pretty: bool = False,
            newl: str = "\n",
            indent: Indent = "\t",
            namespace_separator: str = ":",
            namespaces: MappingNamespaces = None,
            expand_iter: OptionalStr = None,
            preserve_cdata: bool = False,
            preserve_cdata_key: str = "#raw_cdata") -> None: ...


@overload
def unparse(input_dict: Mapping[str, Any], 
            output: None = None, 
            encoding: str = "utf-8", 
            full_document: bool = True,
            short_empty_elements: bool = False, 
            comment_key: str = "#comment",
            *,
            attr_prefix: str = "@",
            cdata_key: str = "#text",
            depth: int = 0,
            preprocessor: Preprocessor | None = None,
            pretty: bool = False,
            newl: str = "\n",
            indent: Indent = "\t",
            namespace_separator: str = ":",
            namespaces: OptionalMappingNamespaces = None,
            expand_iter: OptionalStr = None,
            preserve_cdata: bool = False,
            preserve_cdata_key: str = "#raw_cdata") -> str: ...


def unparse(input_dict: Mapping[str, Any],
            output: OptionalAny = None,
            encoding: str = "utf-8",
            full_document: bool = True,
            short_empty_elements: bool = False,
            comment_key: str = "#comment",
            **kwargs: Any) -> OptionalStr:
    """Emit an XML document for the given `input_dict` (reverse of `parse`).

    The resulting XML document is returned as a string, but if `output` (a
    file-like object) is specified, it is written there instead.

    Dictionary keys prefixed with `attr_prefix` (default=`'@'`) are interpreted
    as XML node attributes, whereas keys equal to `cdata_key`
    (default=`'#text'`) are treated as character data.

    Empty lists are omitted entirely: ``{"a": []}`` produces no ``<a>`` element.
    Provide a placeholder entry (for example ``{"a": [""]}``) when an explicit
    empty container element must be emitted.

    The `pretty` parameter (default=`False`) enables pretty-printing. In this
    mode, lines are terminated with `'\n'` and indented with `'\t'`, but this
    can be customized with the `newl` and `indent` parameters.
    """
    must_return = False
    if output is None:
        output = StringIO()
        must_return = True
    if short_empty_elements:
        content_handler = _XMLGenerator(output, encoding, True)
    else:
        content_handler = _XMLGenerator(output, encoding)
    if full_document:
        content_handler.startDocument()
    seen_root = False
    for key, value in input_dict.items():
        if key != comment_key and full_document and seen_root:
            raise ValueError("Document must have exactly one root.")
        _emit(key, value, content_handler, full_document=full_document, comment_key=comment_key, **kwargs)
        if key != comment_key:
            seen_root = True
    if full_document and not seen_root:
        raise ValueError("Document must have exactly one root.")
    if full_document:
        content_handler.endDocument()
    if must_return:
        value = output.getvalue()
        try:  # pragma no cover
            value = value.decode(encoding)
        except AttributeError:  # pragma no cover
            pass
        return value


def main():
    import marshal

    stdin = sys.stdin.buffer
    stdout = sys.stdout.buffer

    (item_depth,) = sys.argv[1:]
    item_depth = int(item_depth)

    def handle_item(path, item):
        marshal.dump((path, item), stdout)
        return True

    try:
        root = parse(stdin,
                     item_depth=item_depth,
                     item_callback=handle_item,
                     dict_constructor=dict)
        if item_depth == 0:
            handle_item([], root)
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":  # pragma: no cover
    sys.exit(main())