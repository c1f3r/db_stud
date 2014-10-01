# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time', models.DateTimeField(auto_now=True, verbose_name=b'Date/Time')),
                ('action', models.CharField(max_length=20, verbose_name=b'Action')),
                ('model', models.CharField(max_length=50, verbose_name=b'Model')),
            ],
            options={
                'ordering': ['-time'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=20, verbose_name='Group title')),
            ],
            options={
                'ordering': ['title'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('full_name', models.CharField(max_length=50, verbose_name="Student's full name")),
                ('id_number', models.CharField(unique=True, max_length=20, verbose_name="Number of student's ID", blank=True)),
                ('birth_date', models.DateField(verbose_name="Student's date of birth", blank=True)),
                ('group', models.ForeignKey(related_name=b'students', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='db.Group', null=True)),
            ],
            options={
                'ordering': ['full_name'],
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='group',
            name='monitor',
            field=models.ForeignKey(related_name=b'monitor', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='db.Student', null=True),
            preserve_default=True,
        ),
    ]
