from django.contrib import admin
from note.models import Note

# Register your models here.


class NoteAdmin(admin.ModelAdmin):
    fields = ['category']


admin.site.register(Note, NoteAdmin)