# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0003_auto_20150812_0813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='category',
            field=models.CharField(max_length=1, choices=[('T', 'TODO'), ('L', 'LINK'), ('N', 'NOTE'), ('M', 'MEMO')]),
        ),
    ]
