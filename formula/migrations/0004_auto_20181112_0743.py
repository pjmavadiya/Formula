# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formula', '0003_auto_20181112_0741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formula',
            name='operandB',
            field=models.CharField(max_length=10, blank=True),
        ),
        migrations.AlterField(
            model_name='formula',
            name='operator',
            field=models.CharField(blank=True, max_length=20, choices=[(b'ADDITION', b'+'), (b'SUBSTRACTION', b'-'), (b'DIVISION', b'/'), (b'MULTIPLICATION', b'*')]),
        ),
    ]
