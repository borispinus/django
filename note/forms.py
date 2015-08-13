from django.forms import ModelForm
from note.models import Note


class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'text', 'category', 'isFavorite']
