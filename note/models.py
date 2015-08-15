from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Note(models.Model):
    class Meta():
        db_table = "note"
    CATEGORY_CHOICES = (
        ('TODO', 'TODO'),
        ('LINK', 'LINK'),
        ('NOTE', 'NOTE'),
        ('MEMO','MEMO')

    )

    def to_string(self):
        return {'title':self.title, 'text': self.text, 'date': str(self.date),
                'category': self.category, 'is_favorite': self.isFavorite }

    title = models.CharField(max_length=200)
    text = models.TextField()
    date = models.DateTimeField()
    category = models.CharField(max_length=4,choices= CATEGORY_CHOICES)
    isFavorite = models.BooleanField(default= False, verbose_name='mark as favorite')
    user = models.ForeignKey(User)


