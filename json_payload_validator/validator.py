import jsonschema
import re


def handle_failure(error, schema):
    error = str(error)

    def look_for_required_property_error():
        matches = re.search("'.*' is a required property", error)
        if matches:
            return matches.group(0)

    def look_for_validation_failure():
        matches = re.search("Failed validating '.*' in schema\['.*']", error)
        if not matches:
            return None
        prop = schema
        prop_name = None
        for key in re.findall("\['\w{0,}']", matches.group(0)):
            key = key.replace("['", '').replace("']", '')
            prop_name = key
            prop = prop[key]
        print(prop.keys())
        if 'message' in prop.keys():
            return prop_name, str(prop['message'])
        return prop_name, str(prop)

    result = look_for_required_property_error()
    if result:
        return result
    result = look_for_validation_failure()
    if result:
        return "Validation of property '%s' failed: %s" % result
    # return everything if error in unknown
    return error


def validate(json_payload, schema):
    try:
        jsonschema.validate(json_payload, schema)
        return None
    except jsonschema.ValidationError as e:
        return handle_failure(e, schema)
