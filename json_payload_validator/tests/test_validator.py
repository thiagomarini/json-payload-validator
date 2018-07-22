from unittest import TestCase
from json_payload_validator import validate


class TestValidator(TestCase):
    """
    To run the tests use: python setup.py test
    """
    def test_required_properties_validation(self):
        schema = {
            'type': 'object',
            'properties': {
                'name': {'type': 'string'},
                'surname': {'type': 'string'},
            },
            'required': [
                'name', 'surname'
            ]
        }
        error = validate({}, schema)
        expected = "All required properties must be present: name, surname"
        self.assertEqual(expected, error)

    def test_validation_rule_being_returned(self):
        schema = {
            'type': 'object',
            'properties': {
                'name': {'type': 'string', 'minLength': 2, 'maxLength': 50},
            },
            'required': [
                'name'
            ]
        }
        error = validate({'name': 5}, schema)
        self.assertTrue("Validation of property 'name' failed:" in error)
        self.assertTrue("'minLength': 2" in error)
        self.assertTrue("'type': 'string'" in error)
        self.assertTrue("'maxLength': 50" in error)

    def test_custom_message_being_returned(self):
        schema = {
            'type': 'object',
            'properties': {
                'name': {'type': 'string', 'message': 'Name is required'},
            },
            'required': [
                'name'
            ]
        }
        error = validate({'name': 5}, schema)
        expected = "Validation of property 'name' failed: Name is required"
        self.assertEqual(expected, error)

    def test_payload_passing_validation(self):
        schema = {
            'type': 'object',
            'properties': {
                'name': {'type': 'string', 'minLength': 2, 'maxLength': 50},
            },
            'required': [
                'name'
            ]
        }
        error = validate({'name': 'John'}, schema)
        self.assertEqual(None, error)
