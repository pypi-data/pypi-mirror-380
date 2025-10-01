# -*- coding: utf-8 -*-
# :Project:   python-rapidjson -- Normalizer class tests
# :Author:    Meagan Lang <langmm.astro@gmail.com>
# :License:   MIT License
# :Copyright: © 2017, 2019, 2020 Lele Gaifax
#

import pytest

import yggdrasil_rapidjson as rj


def filter_func_ex():  # pragma: no cover
    r"""Test function for normalizing filters."""
    return False


def test_invalid_schema():
    pytest.raises(rj.JSONDecodeError, rj.Normalizer, '')
    pytest.raises(rj.JSONDecodeError, rj.Normalizer, '"')


def test_invalid_json():
    normalizer = rj.Normalizer('{"type": "number"}')
    pytest.raises(rj.JSONDecodeError, normalizer, '')
    pytest.raises(rj.JSONDecodeError, normalizer, '"')
    pytest.raises(rj.JSONDecodeError, normalizer.normalize, '')
    pytest.raises(rj.JSONDecodeError, normalizer.normalize, '"')
    pytest.raises(rj.JSONDecodeError, normalizer.validate, '')
    pytest.raises(rj.JSONDecodeError, normalizer.validate, '"')


def test_notEncoded():
    normalizer = rj.Normalizer('{"type": "number"}')
    pytest.raises(rj.NormalizationError, normalizer,
                  '1', not_encoded=True)
    pytest.raises(rj.NormalizationError, normalizer.normalize,
                  '1', not_encoded=True)
    pytest.raises(rj.ValidationError, normalizer.validate,
                  '1', not_encoded=True)


@pytest.mark.parametrize('schema,json,normalized', (
    ('{ "type": "object", '
     '  "properties": { "color": { "default": "purple"} },'
     '  "required": ["color"] }', '{}', {"color": "purple"}),
    ({"type": "object",
      "properties": {"color": {"default": "purple"}},
      "required": ["color"]}, {}, {"color": "purple"}),
    ({"type": "function"},
     f"{__file__}:filter_func_ex",
     filter_func_ex),
    ({"type": "array", "items": [{"type": "string"}]},
     [b"hello"], ["hello"]),
    ({"type": "array", "items": [{"type": "scalar",
                                  "subtype": "string",
                                  "precision": 5}]},
     ["hello"], [b"hello"]),
    ({"type": "object", "required": ["a"],
      "properties": {
          "a": {"type": "boolean", "default": True}}},
     {"a": True}, {"a": True}),
    ({"type": "array", "items": [{"type": "string"}],
      "allowSingular": True},
     "hello", ["hello"]),
    ({'allowSingular': True,
      'items': [{'subtype': 'string', 'type': 'scalar'}],
      'type': 'array'},
     b"hello", [b"hello"]),
))
def test_normalize(schema, json, normalized):
    normalizer = rj.Normalizer(schema)
    assert normalizer(json) == normalized
    assert normalizer.normalize(json) == normalized
    normalizer.validate(normalized)


def test_normalize_path():
    import os
    import sys
    normalizer = rj.Normalizer({"type": "function"})
    json = f"./{os.path.basename(__file__)}:filter_func_ex"
    fname = __file__
    if sys.platform in ['win32', 'cygwin']:
        fname = fname.replace('\\', '\\\\')
    full = f"\"{fname}:test_normalizer:filter_func_ex\""
    normalized = normalizer(json, relative_path_root=os.path.dirname(__file__))
    norm = rj.dumps(normalized, yggdrasil_mode=rj.YM_READABLE)
    assert norm == full


@pytest.mark.parametrize('schema,json,details', (
    ('{ "type": ["number", "string"] }',
     '["Life", "the universe", "and everything"]',
     ('{\n'
      + '    "message": "Property has a type \'array\' that is not in the'
      + ' following list: \'[\\"string\\",\\"number\\"]\'.",\n'
      + '    "instanceRef": "#",\n'
      + '    "schemaRef": "#"\n'
      + '}', )
     ),
))
def test_invalid(schema, json, details):
    normalizer = rj.Normalizer(schema)
    with pytest.raises(ValueError) as error:
        normalizer(json)
    assert error.value.args == details
    with pytest.raises(ValueError) as error:
        normalizer.normalize(json)
    assert error.value.args == details
    with pytest.raises(ValueError) as error:
        normalizer.validate(json)
    assert error.value.args == details


@pytest.mark.parametrize('schema,json,details,expected', (
    ({"type": "object",
      "properties": {"a": {"type": "string", "default": "foo"},
                     "b": {"type": "string", "deprecated": True}},
      "required": ["a"]},
     {"b": "bar"},
     ('{\n'
      + '    "message": "Property is being deprecated.",\n'
      + '    "instanceRef": "#/b",\n'
      + '    "schemaRef": "#/properties/b"\n'
      + '}', ),
     {"a": "foo", "b": "bar"}
     ),
    ({"type": "object",
      "properties": {"a": {"type": "string", "default": "foo"},
                     "b": {"type": "string", "deprecated": True}},
      "required": ["a"]},
     {"a": "foo", "b": "bar"},
     ('{\n'
      + '    "message": "Property is being deprecated.",\n'
      + '    "instanceRef": "#/b",\n'
      + '    "schemaRef": "#/properties/b"\n'
      + '}', ),
     {"a": "foo", "b": "bar"}
     ),
))
def test_warning(schema, json, details, expected):
    normalizer = rj.Normalizer(schema)
    with pytest.warns(rj.NormalizationWarning) as record:
        assert normalizer(json) == expected
    assert len(record) == 1
    assert record[0].message.args == details
    with pytest.warns(rj.NormalizationWarning) as record:
        assert normalizer.normalize(json) == expected
    assert len(record) == 1
    assert record[0].message.args == details
    with pytest.warns(rj.NormalizationWarning) as record:
        assert rj.normalize(json, schema) == expected
    assert len(record) == 1
    assert record[0].message.args == details


@pytest.mark.parametrize('schema', (
    '{ "type": ["number", "string"] }',
    {"type": ["number", "string"]},
    '{ "type": "instance" }',
    {"type": "instance"}
))
def test_check_schema(schema):
    rj.Normalizer.check_schema(schema)


@pytest.mark.parametrize('schema,details', (
    ('{ "type": 3 }',
     ('{\n'
      '    "message": "Property did not match any of the sub-schemas'
      ' specified by \'anyOf\', refer to following errors.",\n'
      '    "instanceRef": "#/type",\n'
      '    "schemaRef": "#/properties/type",\n'
      '    "errors": [\n'
      '        {\n'
      '            "message": "Property has a value that is not one of its'
      ' allowed enumerated values: [\\"array\\",\\"boolean\\",'
      '\\"integer\\",\\"null\\",\\"number\\",\\"object\\",\\"string\\",'
      '\\"1darray\\",\\"any\\",\\"bytes\\",\\"class\\",\\"complex\\",'
      '\\"float\\",\\"function\\",\\"instance\\",\\"int\\",\\"ndarray\\",'
      '\\"obj\\",\\"ply\\",\\"scalar\\",\\"schema\\",\\"uint\\",'
      '\\"unicode\\"].",\n'
      '            "instanceRef": "#/type",\n'
      '            "schemaRef": "#/definitions/simpleTypes"\n'
      '        },\n'
      '        {\n'
      '            "message": "Property has a type \'integer\' that is not'
      ' in the following list: \'[\\"array\\"]\'.",\n'
      '            "instanceRef": "#/type",\n'
      '            "schemaRef": "#/properties/type/anyOf/1"\n'
      '        }\n'
      '    ]\n'
      '}', )),
    ({"type": 3},
     ('{\n'
      '    "message": "Property did not match any of the sub-schemas'
      ' specified by \'anyOf\', refer to following errors.",\n'
      '    "instanceRef": "#/type",\n'
      '    "schemaRef": "#/properties/type",\n'
      '    "errors": [\n'
      '        {\n'
      '            "message": "Property has a value that is not one of its'
      ' allowed enumerated values: [\\"array\\",\\"boolean\\",\\"integer\\",'
      '\\"null\\",\\"number\\",\\"object\\",\\"string\\",\\"1darray\\",'
      '\\"any\\",\\"bytes\\",\\"class\\",\\"complex\\",\\"float\\",'
      '\\"function\\",\\"instance\\",\\"int\\",\\"ndarray\\",\\"obj\\",'
      '\\"ply\\",\\"scalar\\",\\"schema\\",\\"uint\\",\\"unicode\\"].",\n'
      '            "instanceRef": "#/type",\n'
      '            "schemaRef": "#/definitions/simpleTypes"\n'
      '        },\n'
      '        {\n'
      '            "message": "Property has a type \'integer\' that is not'
      ' in the following list: \'[\\"array\\"]\'.",\n'
      '            "instanceRef": "#/type",\n'
      '            "schemaRef": "#/properties/type/anyOf/1"\n'
      '        }\n'
      '    ]\n'
      '}', )),
))
def test_check_schema_invalid(schema, details):
    with pytest.raises(ValueError) as error:
        rj.Normalizer.check_schema(schema)
    assert error.value.args == details
