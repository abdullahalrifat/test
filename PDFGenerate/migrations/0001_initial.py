# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-11 23:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.EmailField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FullName', models.TextField(max_length=1000)),
                ('Company', models.TextField(max_length=1000)),
                ('Position', models.TextField(max_length=1000)),
                ('Interest1', models.TextField(max_length=1000)),
                ('Interest2', models.TextField(max_length=1000)),
                ('Interest3', models.TextField(max_length=1000)),
                ('Number', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='excel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ex', models.FileField(upload_to='')),
                ('type', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='pdf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('org', models.CharField(max_length=250)),
                ('talk', models.CharField(max_length=1000)),
                ('person_image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='verify',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.TextField(max_length=1000)),
            ],
        ),
    ]
