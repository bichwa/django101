# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='author',
            field=models.CharField(max_length=200, default=datetime.datetime(2015, 8, 15, 17, 30, 44, 199943, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
