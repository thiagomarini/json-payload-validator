import jsonschema
import re


def handle_failure(error, schema):
    s = str(error)
    start = r"schema\['properties'\]\['"
    end = r"'\]:"
    result = re.search('%s(.*)%s' % (start, end), s)
    if not result:
        message = 'Validation failed'
        if 'required' in schema.keys():
            required_fields = ', '.join(schema['required'])
            message = 'All required properties must be present: %s' % required_fields
    else:
        field = result.group(1)
        rules = schema['properties'][field]
        if 'message' in schema['properties'][field].keys():
            rules = schema['properties'][field]['message']
        message = "Validation of property '%s' failed: %s" % (field, rules)
    return message


def validate(json_payload, schema):
    try:
        jsonschema.validate(json_payload, schema)
        return None
    except jsonschema.ValidationError as e:
        return handle_failure(e, schema)
