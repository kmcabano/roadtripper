# Generated by Django 3.2.7 on 2021-11-29 16:53

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_stop'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stop',
            name='food',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200, verbose_name='Places to eat. Separate with commas!'), size=None),
        ),
    ]