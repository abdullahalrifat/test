# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-29 16:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PDFGenerate', '0002_auto_20170829_1217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pdf',
            name='person_image',
            field=models.ImageField(upload_to=''),
        ),
    ]
