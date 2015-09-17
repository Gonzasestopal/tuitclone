# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('first_name', models.CharField(help_text=b'The first name of the user.', max_length=200, blank=True)),
                ('last_name', models.CharField(help_text=b'The last name of the user.', max_length=200, blank=True)),
                ('identifier', models.CharField(unique=True, max_length=40)),
                ('email', models.EmailField(help_text=b'The email and identifier of the user', max_length=255, verbose_name=b'email address')),
                ('is_active', models.BooleanField(default=True, help_text=b'Determines whether the user is active or not. ', verbose_name=b'Active')),
                ('is_staff', models.BooleanField(default=False, help_text=b'Designates where the user will have acces to the admin interface', verbose_name=b'Staff Status')),
                ('is_superuser', models.BooleanField(default=False, help_text=b'CAUTION - enabling this gives the user full admin access and access to the entire database. Only for ArcCore admins.', verbose_name=b'Superuser')),
                ('follow', models.ManyToManyField(related_name='follow_rel_+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tweet', models.CharField(max_length=140)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
