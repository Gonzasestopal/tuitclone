# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20150915_1922'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 18, 18, 20, 47, 580732, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
