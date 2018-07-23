Json Payload Validator
======================

|CircleCI| |PyPI version shields.io| |PyPI license| |PyPI pyversions|

.. |CircleCI| image:: https://circleci.com/gh/thiagomarini/json-payload-validator.svg?style=svg
    :target: https://circleci.com/gh/thiagomarini/json-payload-validator

.. |PyPI version shields.io| image:: https://img.shields.io/pypi/v/json_payload_validator.svg
   :target: https://pypi.python.org/pypi/json_payload_validator/

.. |PyPI license| image:: https://img.shields.io/pypi/l/json_payload_validator.svg
   :target: https://pypi.python.org/pypi/json_payload_validator/

.. |PyPI pyversions| image:: https://img.shields.io/pypi/pyversions/json_payload_validator.svg
   :target: https://pypi.python.org/pypi/json_payload_validator/

Little Python package that formats validation error messages from `jsonschema
<https://pypi.python.org/pypi/jsonschema>`_.
You should use this package if you want a stand alone json validator decoupled from any framework.

Reason of being
---------------

jsonschema is really cool but its validation error messages suck as they're meant for developers, not end users.
So if you have an API that uses jsonschema to validate json payloads and want to return nicer error messages to your
end users you can use this package :)

How it works
------------

3 simple rules:

- If you don't send a required property in the payload you'll get the message ``'foo' is a required property``.
- If validation fails the validation rule will be returned ``Validation of property 'foo' failed: {'minLength': 2, 'type': 'string', 'maxLength': 50}``.
- If you add ``message`` property in a validation rule its value will be returned instead of the rule ``Validation of property 'foo' failed: Custom error message``.

Usage
-----

**Successful validation example**

.. code-block:: python

    from json_payload_validator import validate

    schema = {
        'type': 'object',
        'properties': {
            'name': {'type': 'string', 'minLength': 2, 'maxLength': 50},
        },
        'required': [
            'name'
        ]
    }

    payload = {'name': 'John Maus'}

    error = validate(payload, schema)
    print(error) # None

**Validation failure example**

.. code-block:: python

    from json_payload_validator import validate

    schema = {
        'type': 'object',
        'properties': {
            'name': {'type': 'string', {'minLength': 2, 'type': 'string', 'maxLength': 50}},
        },
        'required': [
            'name'
        ]
    }

    payload = {'name': 555}

    error = validate(payload, schema)
    print(error) # Validation of property 'name' failed: {'minLength': 2, 'type': 'string', 'maxLength': 50}

**Custom error message example**

.. code-block:: python

    from json_payload_validator import validate

    schema = {
        'type': 'object',
        'properties': {
            'name': {'type': 'string', 'message': 'Name must be a string'},
        },
        'required': [
            'name'
        ]
    }

    # example of validation
    payload = {'name': 555}

    error = validate(payload, schema)
    print(error) # Validation of property 'name' failed: Name must be a string
