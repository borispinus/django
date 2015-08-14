# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0004_auto_20150812_0821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='category',
            field=models.CharField(choices=[('TODO', 'TODO'), ('LINK', 'LINK'), ('NOTE', 'NOTE'), ('MEMO', 'MEMO')], max_length=1),
        ),
    ]
