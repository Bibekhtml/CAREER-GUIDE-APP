from django.test import TestCase
from .models import DistractionBlock

class DistractionBlockModelTest(TestCase):
    def setUp(self):
        DistractionBlock.objects.create(name="Social Media", is_blocked=True)
        DistractionBlock.objects.create(name="Gaming", is_blocked=False)

    def test_distraction_block_creation(self):
        distraction = DistractionBlock.objects.get(name="Social Media")
        self.assertEqual(distraction.is_blocked, True)

    def test_distraction_block_not_blocked(self):
        distraction = DistractionBlock.objects.get(name="Gaming")
        self.assertEqual(distraction.is_blocked, False)

    def test_str_representation(self):
        distraction = DistractionBlock(name="Email")
        self.assertEqual(str(distraction), distraction.name)