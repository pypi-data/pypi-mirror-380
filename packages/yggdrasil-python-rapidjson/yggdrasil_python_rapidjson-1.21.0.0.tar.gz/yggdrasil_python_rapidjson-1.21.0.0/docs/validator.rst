.. -*- coding: utf-8 -*-
.. :Project:   python-rapidjson -- Validator class documentation
.. :Author:    Lele Gaifax <lele@metapensiero.it>
.. :License:   MIT License
.. :Copyright: © 2017, 2018, 2019, 2020, 2024 Lele Gaifax
..

=================
 Validator class
=================

.. currentmodule:: yggdrasil_rapidjson

.. testsetup::

   from yggdrasil_rapidjson import ValidationError, Validator

.. class:: Validator(json_schema)

   :param json_schema: the `JSON schema`__, specified as a ``str`` instance or an *UTF-8*
                       :class:`bytes`/:class:`bytearray` instance
   :raises JSONDecodeError: if `json_schema` is not a valid ``JSON`` value

   __ http://json-schema.org/documentation.html

   .. method:: __call__(json)

      :param json: the ``JSON`` value, specified as a ``str`` instance or an *UTF-8*
                   :class:`bytes`/:class:`bytearray` instance, that will be validated
      :raises JSONDecodeError: if `json` is not a valid ``JSON`` value

      The given `json` value will be validated accordingly to the *schema*: a
      :exc:`ValidationError` will be raised if the validation fails, and the exception
      will contain three arguments, respectively the type of the error, the position in
      the schema and the position in the ``JSON`` document where the error occurred:

      .. doctest::

         >>> validate = Validator('{"required": ["a", "b"]}')
         >>> validate('{"a": null, "b": 1}')
         >>> try:
         ...   validate('{"a": null, "c": false}')
         ... except ValidationError as error:
         ...   print(error.args)
         ...
	 ('{\n    "message": "Object is missing the following members required by the schema: \'[\\"b\\"]\'.",\n    "instanceRef": "#",\n    "schemaRef": "#"\n}',)

      .. doctest::

         >>> validate = Validator('{"type": "array",'
         ...                      ' "items": {"type": "string"},'
         ...                      ' "minItems": 1}')
         >>> validate('["foo", "bar"]')
         >>> try:
         ...   validate('[]')
         ... except ValidationError as error:
         ...   print(error.args)
         ...
	 ('{\n    "message": "Array of length \'0\' is shorter than the \'minItems\' value \'1\'.",\n    "instanceRef": "#",\n    "schemaRef": "#"\n}',)

      .. doctest::

         >>> try:
         ...   validate('[1]')
         ... except ValidationError as error:
         ...   print(error.args)
         ...
	 ('{\n    "message": "Property has a type \'integer\' that is not in the following list: \'[\\"string\\"]\'.",\n    "instanceRef": "#/0",\n    "schemaRef": "#/items"\n}',)

      When `json` is not a valid JSON document, a :exc:`JSONDecodeError` is raised instead:

      .. doctest::

         >>> validate('[x]')
         Traceback (most recent call last):
           File "<stdin>", line 1, in <module>
         yggdrasil_rapidjson.JSONDecodeError: Invalid JSON when creating a document (expectsString = 0, allowsString = 0)
