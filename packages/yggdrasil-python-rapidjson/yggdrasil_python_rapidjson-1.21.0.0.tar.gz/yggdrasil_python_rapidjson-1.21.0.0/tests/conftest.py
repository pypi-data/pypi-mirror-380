# -*- coding: utf-8 -*-
# :Project:   python-rapidjson -- Tests configuration
# :Author:    Lele Gaifax <lele@metapensiero.it>
# :License:   MIT License
# :Copyright: © 2016, 2017, 2018 Lele Gaifax
#

import pytest
import io
import sys
import os
import yggdrasil_rapidjson as rj


@pytest.fixture(autouse=True)
def add_np(doctest_namespace):
    doctest_namespace["rj"] = rj
    doctest_namespace["io"] = io
    # for k in ["Decoder", "Encoder", "Validator", "RawJSON", "loads",
    #           "load", "dumps", "dump", "ValidationError", "NM_NAN",
    #           "NM_NATIVE"]:
    for k in dir(rj):
        doctest_namespace[k] = getattr(rj, k)


def binary_streaming_dumps(o, **opts):
    stream = io.BytesIO()
    rj.dump(o, stream, **opts)
    return stream.getvalue().decode('utf-8')


def text_streaming_dumps(o, **opts):
    stream = io.StringIO()
    rj.dump(o, stream, **opts)
    return stream.getvalue()


def binary_streaming_encoder(o, **opts):
    stream = io.BytesIO()
    rj.Encoder(**opts)(o, stream=stream)
    return stream.getvalue().decode('utf-8')


def text_streaming_encoder(o, **opts):
    stream = io.StringIO()
    rj.Encoder(**opts)(o, stream=stream)
    return stream.getvalue()


def pytest_generate_tests(metafunc):
    if 'dumps' in metafunc.fixturenames and 'loads' in metafunc.fixturenames:
        metafunc.parametrize('dumps,loads', (
            ((rj.dumps, rj.loads),
             (lambda o, **opts: rj.Encoder(**opts)(o),
              lambda j, **opts: rj.Decoder(**opts)(j)))
        ), ids=('func[string]',
                'class[string]'))
    elif 'dumps' in metafunc.fixturenames:
        metafunc.parametrize('dumps', (
            rj.dumps,
            binary_streaming_dumps,
            text_streaming_dumps,
            lambda o, **opts: rj.Encoder(**opts)(o),
            binary_streaming_encoder,
            text_streaming_encoder,
        ), ids=('func[string]',
                'func[bytestream]',
                'func[textstream]',
                'class[string]',
                'class[binarystream]',
                'class[textstream]'))
    elif 'loads' in metafunc.fixturenames:
        metafunc.parametrize('loads', (
            rj.loads,
            lambda j, **opts: rj.load(
                io.BytesIO(j.encode('utf-8')
                           if isinstance(j, str) else j), **opts),
            lambda j, **opts: rj.load(io.StringIO(j), **opts),
            lambda j, **opts: rj.Decoder(**opts)(j),
            lambda j, **opts: rj.Decoder(**opts)(
                io.BytesIO(j.encode('utf-8')
                           if isinstance(j, str) else j)),
            lambda j, **opts: rj.Decoder(**opts)(io.StringIO(j)),
        ), ids=('func[string]',
                'func[bytestream]',
                'func[textstream]',
                'class[string]',
                'class[bytestream]',
                'class[textstream]'))


@pytest.fixture(scope="session", autouse=True)
def rapidjson_test_module_path():
    return os.path.abspath(os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        'rapidjson', 'test', 'example_python.py'))


@pytest.fixture(scope="session", autouse=True)
def rapidjson_test_module_on_path(rapidjson_test_module_path):
    sys.path.insert(0, os.path.dirname(rapidjson_test_module_path))
    yield
    sys.path.pop(0)


@pytest.fixture(scope="session")
def rapidjson_test_module(rapidjson_test_module_on_path):
    import example_python
    return example_python


@pytest.fixture
def example_class(rapidjson_test_module):
    return rapidjson_test_module.ExampleClass


@pytest.fixture
def example_function(rapidjson_test_module):
    return rapidjson_test_module.example_function


@pytest.fixture
def example_instance(example_class):
    return example_class(1, 'b', c=2, d='d')


@pytest.fixture
def example_class_builtin(rapidjson_test_module):
    import collections
    return collections.OrderedDict
