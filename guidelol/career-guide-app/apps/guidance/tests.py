from django.test import TestCase
from .models import Career, Video, Test

class CareerModelTest(TestCase):
    def setUp(self):
        self.career = Career.objects.create(name="Software Development", description="Developing software applications.")

    def test_career_creation(self):
        self.assertEqual(self.career.name, "Software Development")
        self.assertEqual(self.career.description, "Developing software applications.")

class VideoModelTest(TestCase):
    def setUp(self):
        self.video = Video.objects.create(title="Introduction to Python", url="http://example.com/python")

    def test_video_creation(self):
        self.assertEqual(self.video.title, "Introduction to Python")
        self.assertEqual(self.video.url, "http://example.com/python")

class TestModelTest(TestCase):
    def setUp(self):
        self.test = Test.objects.create(title="Python Basics", total_questions=10)

    def test_test_creation(self):
        self.assertEqual(self.test.title, "Python Basics")
        self.assertEqual(self.test.total_questions, 10)