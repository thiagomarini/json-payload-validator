# Json Payload Validator

Little package that formats validation error messages from [jsonschema](https://pypi.python.org/pypi/jsonschema).
You should use this package if you want a stand alone json validator decoupled from any framework.

### Reason of being

jsonschema is really cool but its validation error messages suck as they're meant for developers, not end users.
So if you have an API that uses jsonschema to validate json payloads and want to return nicer error messages to your
end users you can use this package :)

### How it works

3 simple rules:

* If you don't send a required property in the payload you'll get the message `All required properties must be present: foo, bar, baz`.
* If validation fails the validation rule will be returned `Validation of property 'name' failed: {'minLength': 2, 'type': 'string', 'maxLength': 50}`.
* If you add `message` property in your validation rule its value will be returned instead of the rule `Validation of property 'foo' failed: Custom message will go in here`.

### Usage

To use, simply do:

```python
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

# example of validation
payload = {'name': 'John Maus'}

error = validate(payload, schema)

if error is None:
    print 'Validation passed :-)'
else:
    print error 
    # Validation of property 'name' failed: {'minLength': 2, 'type': 'string', 'maxLength': 50}
```
