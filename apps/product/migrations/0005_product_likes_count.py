# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_auto_20160307_2011'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='likes_count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
