# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formula', '0002_auto_20181112_0738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formula',
            name='name',
            field=models.CharField(unique=True, max_length=10),
        ),
    ]
