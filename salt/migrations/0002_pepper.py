# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-30 07:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

	dependencies = [
		('salt', '0001_initial'),
	]

	operations = [
		migrations.CreateModel(
			name='Pepper',
			fields=[
				('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
				('body', models.TextField(max_length=110)),
				('timestamp', models.DateTimeField(auto_now_add=True)),
				('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='salt.Profile')),
			],
		),
	]
