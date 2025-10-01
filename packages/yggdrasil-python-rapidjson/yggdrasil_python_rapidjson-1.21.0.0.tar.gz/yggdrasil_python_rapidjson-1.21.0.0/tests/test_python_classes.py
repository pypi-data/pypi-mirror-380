# -*- coding: utf-8 -*-
# :Project:   python-rapidjson -- Normalizer class tests
# :Author:    Meagan Lang <langmm.astro@gmail.com>
# :License:   MIT License
# :Copyright: © 2017, 2019, 2020 Lele Gaifax
#

import pytest

import yggdrasil_rapidjson as rj
import collections


@pytest.mark.parametrize(
    'value_str', (
        'example_function',
        'example_class',
        'example_instance',
    ))
def test_python_objects(dumps, loads, value_str, request):
    value = request.getfixturevalue(value_str)
    dumped = dumps(value)
    loaded = loads(dumped)
    assert loaded == value and type(loaded) is type(value)


@pytest.mark.parametrize(
    'value_str,result', [
        ('example_function',
         '{rapidjson_test_module_path}:example_python:example_function'),
        ('example_class',
         '{rapidjson_test_module_path}:example_python:ExampleClass'),
        ('example_instance',
         {'class': '{rapidjson_test_module_path}:example_python:ExampleClass',
          'args': [1, 'b'],
          'kwargs': {'c': 2, 'd': 'd'}}),
        ('example_class_builtin',
         f'{collections.__file__}:collections:OrderedDict')
    ])
def test_python_objects_as_pure_python(dumps, loads, value_str, result,
                                       request, rapidjson_test_module_path):
    if isinstance(result, str):
        result = result.format(
            rapidjson_test_module_path=rapidjson_test_module_path)
    elif isinstance(result, dict):
        result['class'] = result['class'].format(
            rapidjson_test_module_path=rapidjson_test_module_path)
    value = request.getfixturevalue(value_str)
    dumped = dumps(value, yggdrasil_mode=rj.YM_READABLE)
    loaded = loads(dumped)
    assert loaded == result
    assert rj.as_pure_json(value) == result


@pytest.mark.parametrize('schema', (
    '{ "type": "instance", "class": "-YGG-eyJ0eXBlIjoiY2xhc3MifQ=='
    '-YGG-ZXhhbXBsZV9weXRob246RXhhbXBsZUNsYXNz-YGG-" }',
    {"type": "instance",
     "class": ("-YGG-eyJ0eXBlIjoiY2xhc3MifQ==-YGG-ZXhhbXBsZV9weXRob246RX"
               "hhbXBsZUNsYXNz-YGG-")}
))
def test_check_python_schema(schema, rapidjson_test_module_on_path):
    rj.Validator.check_schema(schema)
