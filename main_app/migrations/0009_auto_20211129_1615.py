# Generated by Django 3.2.7 on 2021-11-29 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_alter_stop_food'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stop',
            name='food',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='stop',
            name='todos',
            field=models.TextField(max_length=2000),
        ),
    ]
