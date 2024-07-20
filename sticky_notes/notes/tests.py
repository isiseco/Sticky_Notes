from django.test import TestCase
from .models import Note, Bulletin

class NoteModelTest(TestCase):
    """Test suite for the Note model."""

    def setUp(self):
        """Set up test data."""
        Note.objects.create(title="Test Note", content="This is a test note.")

    def test_note_content(self):
        """Test the content of a note."""
        note = Note.objects.get(id=1)
        expected_object_name = f'{note.title}'
        self.assertEqual(expected_object_name, 'Test Note')

class BulletinModelTest(TestCase):
    """Test suite for the Bulletin model."""

    def setUp(self):
        """Set up test data."""
        Bulletin.objects.create(title="Test Bulletin", content="This is a test bulletin.")

    def test_bulletin_content(self):
        """Test the content of a bulletin."""
        bulletin = Bulletin.objects.get(id=1)
        expected_object_name = f'{bulletin.title}'
        self.assertEqual(expected_object_name, 'Test Bulletin')
