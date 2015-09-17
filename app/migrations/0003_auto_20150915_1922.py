# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20150915_1854'),
    ]

    operations = [
        migrations.RenameField(
            model_name='myuser',
            old_name='hola',
            new_name='usuario',
        ),
        migrations.AlterField(
            model_name='myuser',
            name='is_staff',
            field=models.BooleanField(default=True, help_text=b'Designates where the user will have acces to the admin interface', verbose_name=b'Staff Status'),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='is_superuser',
            field=models.BooleanField(default=True, help_text=b'CAUTION - enabling this gives the user full admin access and access to the entire database. Only for ArcCore admins.', verbose_name=b'Superuser'),
        ),
    ]
