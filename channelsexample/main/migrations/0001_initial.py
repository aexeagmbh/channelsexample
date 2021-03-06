# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-09 13:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import main.mixins
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.TextField()),
            ],
            options={
                'abstract': False,
            },
            bases=(main.mixins.PushNotificationOnChangeModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.TextField()),
            ],
            options={
                'abstract': False,
            },
            bases=(main.mixins.PushNotificationOnChangeModelMixin, models.Model),
        ),
        migrations.AddField(
            model_name='asset',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Project'),
        ),
    ]
