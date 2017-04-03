# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-02 11:04
from __future__ import unicode_literals

from django.db import migrations, models
import sumbangan.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PemberianSumbangan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tanggal', models.DateField(auto_now_add=True, db_index=True)),
                ('nama', models.CharField(max_length=500)),
                ('no_ktp', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=250)),
                ('no_telephone', models.CharField(max_length=50)),
                ('jumlah', models.DecimalField(decimal_places=2, max_digits=65)),
                ('bukti_transfer', models.ImageField(max_length=500, upload_to=sumbangan.models.bukti_transfer_directory_path)),
            ],
        ),
    ]