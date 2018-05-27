# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-27 17:13
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0002_auto_20180527_1129'),
    ]

    operations = [
        migrations.CreateModel(
            name='Confirmed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('is_active', models.BooleanField(default=True, verbose_name='Esta activo')),
                ('hash_time', models.CharField(blank=True, max_length=254, null=True, verbose_name='Código')),
                ('email', models.CharField(blank=True, max_length=254, null=True, verbose_name='Email')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Recuperacion de Contraseña',
            },
        ),
    ]
