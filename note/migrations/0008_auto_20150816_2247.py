# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0007_note_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='isFavorite',
            field=models.BooleanField(default=False, verbose_name='mark as favorite'),
        ),
    ]
