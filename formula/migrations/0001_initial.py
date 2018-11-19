# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Formula',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=10)),
                ('operandA', models.CharField(max_length=10)),
                ('operand', models.CharField(max_length=20, choices=[(b'ADDITION', b'+'), (b'SUBSTRACTION', b'-'), (b'DIVISION', b'/'), (b'MULTIPLICATION', b'*')])),
                ('operandB', models.CharField(max_length=10)),
            ],
        ),
    ]
