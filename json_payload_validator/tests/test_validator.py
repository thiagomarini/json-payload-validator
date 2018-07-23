from unittest import TestCase
from json_payload_validator import validate


class TestValidator(TestCase):
    """
    To run the tests use: python setup.py test
    """

    flat_schema = {
        'type': 'object',
        'properties': {
            'name': {'type': 'string'},
            'surname': {'type': 'string'},
        },
        'required': [
            'name', 'surname'
        ]
    }

    nested_schema = {
        'type': 'object',
        'required': ['name', 'age', 'club_name'],
        'properties': {
            'name': {
                'type': 'object',
                'required': ['first_name', 'last_name'],
                'properties': {
                    'first_name': {'type': 'string', 'minLength': 2, 'maxLength': 50},
                    'last_name': {'type': 'string'}
                }
            },
            'age': {'type': 'integer'},
            'club_name': {'type': 'string'}
        }
    }

    def test_required_property_validation_with_empty_payload(self):
        error = validate({}, self.flat_schema)
        expected = "'name' is a required property"
        self.assertEqual(expected, error)

    def test_required_property_validation_with_other_property_present(self):
        error = validate({'name': 'John'}, self.flat_schema)
        expected = "'surname' is a required property"
        self.assertEqual(expected, error)

    def test_required_property_validation_in_nested_object(self):
        payload = {
            'name': {
                'last_name': 'Tardelli'
            },
            'age': 27,
            'club_name': 'Clube Atletico Mineiro'
        }
        error = validate(payload, self.nested_schema)
        expected = "'first_name' is a required property"
        self.assertEqual(expected, error)

    def test_return_of_validation_rule_in_flat_object(self):
        error = validate({'name': 666, 'surname': 'Maus'}, self.flat_schema)
        expected = "Validation of property 'name' failed: {'type': 'string'}"
        self.assertEqual(expected, error)

    def test_return_of_validation_rule_in_nested_object(self):
        payload = {
            'name': {
                'first_name': 66,
                'last_name': 'Tardelli',
            },
            'age': 76,
            'club_name': 'Clube Atletico Mineiro'
        }
        error = validate(payload, self.nested_schema)
        self.assertTrue("Validation of property 'first_name' failed:" in error)
        self.assertTrue("'minLength': 2" in error)
        self.assertTrue("'type': 'string'" in error)
        self.assertTrue("'maxLength': 50" in error)

    def test_return_of_custom_error_message_in_flat_object(self):
        schema = {
            'type': 'object',
            'properties': {
                'name': {'type': 'string', 'message': 'Foo bar'},
                'surname': {'type': 'string'},
            },
            'required': [
                'name', 'surname'
            ]
        }
        error = validate({'name': 666, 'surname': 'Maus'}, schema)
        expected = "Validation of property 'name' failed: Foo bar"
        self.assertEqual(expected, error)

    def test_return_of_custom_error_message_in_nested_object(self):
        schema = {
            'type': 'object',
            'required': ['name', 'age', 'club_name'],
            'properties': {
                'name': {
                    'type': 'object',
                    'required': ['first_name', 'last_name'],
                    'properties': {
                        'first_name': {'type': 'string', 'message': 'Hello World'},
                        'last_name': {'type': 'string'}
                    }
                },
                'age': {'type': 'integer'},
                'club_name': {'type': 'string'}
            }
        }
        payload = {
            'name': {
                'first_name': 666,
                'last_name': 'Tardelli',
            },
            'age': 31,
            'club_name': 'Clube Atletico Mineiro'
        }
        error = validate(payload, schema)
        expected = "Validation of property 'first_name' failed: Hello World"
        self.assertEqual(expected, error)

    def test_flat_object_passing_validation(self):
        error = validate({'name': 'John', 'surname': 'Maus'}, self.flat_schema)
        self.assertEqual(None, error)

    def test_nested_object_passing_validation(self):
        payload = {
            'name': {
                'first_name': 'Diego',
                'last_name': 'Tardelli',
            },
            'age': 26,
            'club_name': 'Clube Atletico Mineiro'
        }
        error = validate(payload, self.nested_schema)
        self.assertEqual(None, error)
