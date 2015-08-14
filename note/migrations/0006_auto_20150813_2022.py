# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0005_auto_20150813_2009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='category',
            field=models.CharField(max_length=4, choices=[('TODO', 'TODO'), ('LINK', 'LINK'), ('NOTE', 'NOTE'), ('MEMO', 'MEMO')]),
        ),
    ]
