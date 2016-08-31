# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-31 19:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='picture',
            field=models.ImageField(default='/static/img/no-avatar.jpg', upload_to='avatars', verbose_name='picture'),
        ),
    ]