from django.test import TestCase
from .models import Playlist, Teacher

class PlaylistModelTest(TestCase):

    def setUp(self):
        self.teacher = Teacher.objects.create(name="John Doe", bio="Expert in Python")
        self.playlist = Playlist.objects.create(title="Python Basics", teacher=self.teacher)

    def test_playlist_creation(self):
        self.assertEqual(self.playlist.title, "Python Basics")
        self.assertEqual(self.playlist.teacher.name, "John Doe")

    def test_playlist_str(self):
        self.assertEqual(str(self.playlist), "Python Basics")

class TeacherModelTest(TestCase):

    def setUp(self):
        self.teacher = Teacher.objects.create(name="Jane Smith", bio="Expert in JavaScript")

    def test_teacher_creation(self):
        self.assertEqual(self.teacher.name, "Jane Smith")
        self.assertEqual(self.teacher.bio, "Expert in JavaScript")

    def test_teacher_str(self):
        self.assertEqual(str(self.teacher), "Jane Smith")