# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-10-09 12:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='publish',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, editable=False),
        ),
        migrations.AddField(
            model_name='post',
            name='update',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
