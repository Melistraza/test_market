# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250)),
                ('slug', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('price', models.DecimalField(max_digits=5, decimal_places=2)),
                ('created_at', models.DateTimeField()),
                ('modified_at', models.DateTimeField()),
            ],
        ),
    ]
