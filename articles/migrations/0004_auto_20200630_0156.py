# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2020-06-29 20:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_article_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='body',
            new_name='story',
        ),
    ]
