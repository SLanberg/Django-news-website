# Generated by Django 3.0.4 on 2020-04-11 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='text',
            field=models.TextField(max_length=500),
        ),
    ]
