from django import forms
from .models import Note, Bulletin

class NoteForm(forms.ModelForm):
    """Form for creating and editing notes."""
    class Meta:
        model = Note
        fields = ['title', 'content']

class BulletinForm(forms.ModelForm):
    """Form for creating and editing bulletins."""
    class Meta:
        model = Bulletin
        fields = ['title', 'content']
