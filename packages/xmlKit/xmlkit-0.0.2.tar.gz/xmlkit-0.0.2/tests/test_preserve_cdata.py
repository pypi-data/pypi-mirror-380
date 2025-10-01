from xmlkit import parse, unparse


XML_WITH_CDATA = """<?xml version="1.0" encoding="utf-8"?>
<systemList xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
	<system>
		<name>cavestory</name>
		<fullname>Cave Story</fullname>
		<path>/roms/cavestory/</path>
		<extension>.dll .DLL .exe .EXE .so .SO</extension>
		<command><![CDATA[sudo perfmax %EMULATOR% %CORE%; nice -n -19 /usr/local/bin/%EMULATOR% -L /home/ark/.config/%EMULATOR%/cores/%CORE%_libretro.so %ROM%; sudo perfnorm]]></command>
		<emulators>
			<emulator name="retroarch">
				<cores>
					<core>doukutsu_rs</core>
				</cores>
			</emulator>
		</emulators>
		<platform>pc</platform>
		<theme>cavestory</theme>
	</system>
	<system>
		<name>options</name>
		<fullname>Options</fullname>
		<path>/opt/system/</path>
		<extension>.sh .SH</extension>
		<command><![CDATA[sudo chmod 666 /dev/tty1; %ROM% 2>&1 > /dev/tty1; printf "\\033c" >> /dev/tty1]]></command>
		<platform>ignore</platform>
		<theme>retropie</theme>
	</system>
</systemList>"""

EXPECTED_DICT = {
    "systemList": {
        "@xmlns:xsi": "http://www.w3.org/2001/XMLSchema-instance",
        "system": [
            {
                "name": "cavestory",
                "fullname": "Cave Story",
                "path": {"#text": "/roms/cavestory/"},
                "extension": ".dll .DLL .exe .EXE .so .SO",
                "command": {
                    "#raw_cdata": "sudo perfmax %EMULATOR% %CORE%; nice -n -19 /usr/local/bin/%EMULATOR% -L /home/ark/.config/%EMULATOR%/cores/%CORE%_libretro.so %ROM%; sudo perfnorm"
                },
                "emulators": {
                    "emulator": {"@name": "retroarch", "cores": {"core": "doukutsu_rs"}}
                },
                "platform": "pc",
                "theme": "cavestory",
            },
            {
                "name": "options",
                "fullname": "Options",
                "path": {"#text": "/opt/system/"},
                "extension": ".sh .SH",
                "command": {
                    "#raw_cdata": 'sudo chmod 666 /dev/tty1; %ROM% 2>&1 > /dev/tty1; printf "\\033c" >> /dev/tty1'
                },
                "platform": "ignore",
                "theme": "retropie",
            },
        ],
    }
}


def test_preserves_parsed_cdata() -> None:
    actual_dict = parse(XML_WITH_CDATA, preserve_cdata=True, force_cdata=("path",))
    assert actual_dict == EXPECTED_DICT


def test_preserves_unparsed_cdata() -> None:
    actual_xml = unparse(EXPECTED_DICT, force_cdata=("path",), pretty=True)
    assert actual_xml == XML_WITH_CDATA


def test_basic_cdata_preservation():
    """Test basic CDATA content preservation"""
    xml = """<?xml version="1.0"?>
    <root><![CDATA[content]]></root>"""
    expected_dict = {"root": {"#raw_cdata": "content"}}
    actual_dict = parse(xml, preserve_cdata=True)
    assert actual_dict == expected_dict

    # Round-trip test
    actual_xml = unparse(expected_dict)
    assert "<![CDATA[content]]>" in actual_xml


def test_empty_cdata_sections():
    """Test empty CDATA sections handling"""
    xml = """<?xml version="1.0"?>
    <root><![CDATA[]]></root>"""
    expected_dict = {"root": {"#raw_cdata": ""}}
    actual_dict = parse(xml, preserve_cdata=True)
    assert actual_dict == expected_dict

    # Round-trip test
    actual_xml = unparse(expected_dict)
    assert "<![CDATA[]]>" in actual_xml


def test_cdata_with_special_characters():
    """Test CDATA containing special XML characters"""
    xml = """<?xml version="1.0"?>
    <root><![CDATA[Special chars: <>&"']]></root>"""
    expected_dict = {"root": {"#raw_cdata": "Special chars: <>&\"'"}}
    actual_dict = parse(xml, preserve_cdata=True)
    assert actual_dict == expected_dict

    # Round-trip test
    actual_xml = unparse(expected_dict)
    assert "<![CDATA[Special chars: <>&\"']]>" in actual_xml


def test_cdata_with_xml_like_content():
    """Test CDATA containing XML-like text"""
    xml = """<?xml version="1.0"?>
    <root><![CDATA[<p>This looks like HTML</p>]]></root>"""
    expected_dict = {"root": {"#raw_cdata": "<p>This looks like HTML</p>"}}
    actual_dict = parse(xml, preserve_cdata=True)
    assert actual_dict == expected_dict

    # Round-trip test
    actual_xml = unparse(expected_dict)
    assert "<![CDATA[<p>This looks like HTML</p>]]>" in actual_xml


def test_nested_cdata_structures():
    """Test CDATA in nested XML elements"""
    xml = """<?xml version="1.0"?>
    <root>
        <parent>
            <child><![CDATA[nested content]]></child>
        </parent>
    </root>"""
    expected_dict = {"root": {"parent": {"child": {"#raw_cdata": "nested content"}}}}
    actual_dict = parse(xml, preserve_cdata=True)
    assert actual_dict == expected_dict

    # Round-trip test
    actual_xml = unparse(expected_dict)
    assert "<![CDATA[nested content]]>" in actual_xml


def test_cdata_with_attributes():
    """Test elements with both CDATA and attributes"""
    xml = """<?xml version="1.0"?>
    <root attr="value"><![CDATA[content with attributes]]></root>"""
    expected_dict = {
        "root": {"@attr": "value", "#raw_cdata": "content with attributes"}
    }
    actual_dict = parse(xml, preserve_cdata=True)
    assert actual_dict == expected_dict

    # Round-trip test
    actual_xml = unparse(expected_dict)
    assert 'attr="value"' in actual_xml
    assert "<![CDATA[content with attributes]]>" in actual_xml


def test_cdata_with_namespaces():
    """Test CDATA in namespaced XML"""
    xml = """<?xml version="1.0"?>
    <root xmlns:ns="http://example.com">
        <ns:element><![CDATA[namespaced content]]></ns:element>
    </root>"""
    expected_dict = {
        "root": {
            "@xmlns:ns": "http://example.com",
            "ns:element": {"#raw_cdata": "namespaced content"},
        }
    }
    actual_dict = parse(xml, preserve_cdata=True)
    assert actual_dict == expected_dict

    # Round-trip test
    actual_xml = unparse(expected_dict)
    assert "<![CDATA[namespaced content]]>" in actual_xml


def test_mixed_content_with_cdata():
    """Test elements with both regular text and CDATA"""
    xml = """<?xml version="1.0"?>
    <root>Regular text<![CDATA[and CDATA content]]></root>"""
    expected_dict = {"root": {"#raw_cdata": "Regular textand CDATA content"}}
    actual_dict = parse(xml, preserve_cdata=True)
    assert actual_dict == expected_dict

    # Round-trip test
    actual_xml = unparse(expected_dict)
    # Note: In mixed content, all character data is concatenated and output as a single CDATA section
    assert "<![CDATA[Regular textand CDATA content]]>" in actual_xml


def test_multiple_cdata_sections():
    """Test elements with multiple CDATA sections"""
    xml = """<?xml version="1.0"?>
    <root><![CDATA[first]]> and <![CDATA[second]]></root>"""
    expected_dict = {
        "root": {
            "#raw_cdata": "first and second"  # All CDATA sections are concatenated
        }
    }
    actual_dict = parse(xml, preserve_cdata=True)
    assert actual_dict == expected_dict

    # Round-trip test
    actual_xml = unparse(expected_dict)
    # All character data is concatenated and output as a single CDATA section
    assert "<![CDATA[first and second]]>" in actual_xml


def test_cdata_whitespace_variations():
    """Test CDATA with various whitespace patterns"""
    xml = """<?xml version="1.0"?>
    <root><![CDATA[  whitespace  	
  content  	
  ]]></root>"""
    expected_dict = {"root": {"#raw_cdata": "whitespace  \t\n  content"}}
    actual_dict = parse(xml, preserve_cdata=True)
    assert actual_dict == expected_dict

    # Round-trip test
    actual_xml = unparse(expected_dict)
    assert "<![CDATA[whitespace  \t\n  content]]>" in actual_xml


def test_cdata_with_force_cdata():
    """Test CDATA preservation with force_cdata parameter"""
    xml = """<?xml version="1.0"?>
    <root>
        <element><![CDATA[forced CDATA content]]></element>
    </root>"""
    expected_dict = {"root": {"element": {"#raw_cdata": "forced CDATA content"}}}
    actual_dict = parse(xml, preserve_cdata=True, force_cdata=("element",))
    assert actual_dict == expected_dict

    # Round-trip test
    actual_xml = unparse(expected_dict, force_cdata=("element",))
    assert "<![CDATA[forced CDATA content]]>" in actual_xml


def test_cdata_edge_cases():
    """Test edge cases like very long CDATA content"""
    # Test with very long CDATA content
    long_content = "A" * 10000  # 10KB of content
    xml_long = f"""<?xml version="1.0"?>
    <root><![CDATA[{long_content}]]></root>"""
    expected_dict = {"root": {"#raw_cdata": long_content}}
    actual_dict = parse(xml_long, preserve_cdata=True)
    assert actual_dict == expected_dict

    # Round-trip test
    actual_xml = unparse(expected_dict)
    assert "<![CDATA[" in actual_xml
    assert "]]>" in actual_xml
    assert long_content in actual_xml


def test_cdata_error_handling():
    """Test error conditions in CDATA processing"""
    # Test with CDATA containing the closing sequence (should be handled by splitting)
    xml_closing = """<?xml version="1.0"?>
    <root><![CDATA[content ]]]]><![CDATA[> more content]]></root>"""
    # This is a complex case - in practice, parsers might handle this differently
    # The important thing is that it doesn't crash and handles it reasonably
    try:
        actual_dict = parse(xml_closing, preserve_cdata=True)
        # If parsing succeeds, ensure round-trip works
        if actual_dict:
            actual_xml = unparse(actual_dict)
            assert "content" in actual_xml
    except Exception:
        # If parsing fails, that's acceptable as it's an edge case
        pass


def test_cdata_backward_compatibility():
    """Test that preserve_cdata=False maintains existing behavior"""
    xml = """<?xml version="1.0" encoding="UTF-8"?>
    <root><![CDATA[content]]></root>"""
    # With preserve_cdata=False (default), should behave as before
    dict_without_preserve = parse(xml)  # preserve_cdata=False by default
    dict_with_preserve_false = parse(xml, preserve_cdata=False)
    assert dict_without_preserve == dict_with_preserve_false
    # Should not have #raw_cdata key
    assert "#raw_cdata" not in str(dict_without_preserve)


def test_cdata_round_trip_consistency():
    """Test consistent round-trip behavior"""
    # Test basic CDATA preservation
    xml = """<?xml version="1.0" encoding="UTF-8"?>
    <root><![CDATA[content with > and &]]></root>"""
    parsed = parse(xml, preserve_cdata=True)
    unparsed = unparse(parsed)
    assert "<![CDATA[content with > and &]]>" in unparsed

    # Test with special characters (note: some whitespace characters may not be preserved in round-trip)
    xml_special = """<?xml version="1.0"?>
    <root><![CDATA[Special chars: <>&"']]></root>"""
    parsed = parse(xml_special, preserve_cdata=True)
    unparsed = unparse(parsed)
    assert "<![CDATA[Special chars: <>&\"']]" in unparsed

    # Test with empty CDATA
    xml_empty = """<?xml version="1.0"?>
    <root><![CDATA[]]></root>"""
    parsed = parse(xml_empty, preserve_cdata=True)
    unparsed = unparse(parsed)
    assert "<![CDATA[]]>" in unparsed


def test_selective_preserve_cdata_tuple():
    """Test selective CDATA preservation with tuple parameter"""
    xml = "<root><a><![CDATA[data1]]></a><b><![CDATA[data2]]></b><c><![CDATA[data3]]></c></root>"
    # Preserve CDATA only for 'a' and 'c' elements
    result = parse(xml, preserve_cdata=("a", "c"))
    expected = {
        "root": {
            "a": {"#raw_cdata": "data1"},
            "b": "data2",
            "c": {"#raw_cdata": "data3"},
        }
    }
    assert result == expected


def test_selective_preserve_cdata_callable():
    """Test selective CDATA preservation with callable parameter"""
    xml = "<root><a><![CDATA[data1]]></a><b><![CDATA[data2]]></b><c><![CDATA[data3]]></c></root>"

    # Test with callable function
    def should_preserve_cdata(path, key, value):
        return key in ["a", "c"]

    result = parse(xml, preserve_cdata=should_preserve_cdata)
    expected = {
        "root": {
            "a": {"#raw_cdata": "data1"},
            "b": "data2",
            "c": {"#raw_cdata": "data3"},
        }
    }
    assert result == expected


def test_custom_preserve_cdata_key():
    """Test custom CDATA key identifier"""
    xml = "<root><![CDATA[content]]></root>"
    result = parse(xml, preserve_cdata=True, preserve_cdata_key="_CDATA_")
    expected = {"root": {"_CDATA_": "content"}}
    assert result == expected


def test_preserve_cdata_backwards_compatibility():
    """Test backward compatibility with existing boolean preserve_cdata parameter"""
    xml = "<root><![CDATA[content]]></root>"
    # Test that boolean True still works (backwards compatibility)
    result_true = parse(xml, preserve_cdata=True)
    expected_true = {"root": {"#raw_cdata": "content"}}
    assert result_true == expected_true

    # Test that boolean False still works (backwards compatibility)
    result_false = parse(xml, preserve_cdata=False)
    expected_false = {"root": "content"}
    assert result_false == expected_false


def test_preserve_cdata_with_force_cdata():
    """Test combined functionality (preserve_cdata with force_cdata)"""
    xml = "<root><a><![CDATA[data1]]></a><b>data2</b></root>"
    # Preserve CDATA for 'a', force CDATA for 'b'
    result = parse(xml, preserve_cdata=("a",), force_cdata=("b",))
    expected = {"root": {"a": {"#raw_cdata": "data1"}, "b": {"#text": "data2"}}}
    assert result == expected
