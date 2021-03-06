# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-04 21:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='autor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('apaterno', models.CharField(max_length=25)),
                ('amaterno', models.CharField(max_length=25)),
                ('nacionalidad', models.CharField(max_length=25)),
                ('biografia', models.TextField()),
                ('sexo', models.CharField(blank=True, choices=[('M', 'Mujer'), ('H', 'Hombre')], max_length=16)),
                ('genero_lit', models.CharField(choices=[('D', 'Drama'), ('T', 'Terror')], max_length=16)),
                ('edad', models.CharField(max_length=25)),
                ('estado', models.CharField(choices=[('V', 'Vivo'), ('T', 'Muerto')], max_length=16)),
            ],
        ),
    ]
