from django.test import TestCase
from .models import TestModel  # Replace with actual model names

class TestModelTests(TestCase):

    def setUp(self):
        # Set up any initial data for the tests
        self.test_instance = TestModel.objects.create(field1='value1', field2='value2')

    def test_model_creation(self):
        """Test that the model instance is created correctly."""
        self.assertEqual(self.test_instance.field1, 'value1')
        self.assertEqual(self.test_instance.field2, 'value2')

    def test_model_str(self):
        """Test the string representation of the model."""
        self.assertEqual(str(self.test_instance), 'Expected String Representation')

    def tearDown(self):
        # Clean up after tests
        self.test_instance.delete()