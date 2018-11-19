# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formula', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='formula',
            old_name='operand',
            new_name='operator',
        ),
    ]
