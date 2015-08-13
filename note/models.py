from django.db import models

# Create your models here.


class Note(models.Model):
    class Meta():
        db_table = "note"
    CATEGORY_CHOICES = (
        ('T', 'TODO'),
        ('L', 'LINK'),
        ('N', 'NOTE'),
        ('M','MEMO')

    )
    title = models.CharField(max_length=200)
    text = models.TextField()
    date = models.DateTimeField()
    category = models.CharField(max_length=1,choices= CATEGORY_CHOICES)
    isFavorite = models.BooleanField(default= False)


