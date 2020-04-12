# Generated by Django 3.0.4 on 2020-04-11 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_menu_item_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu_item',
            name='url',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='External resource url'),
        ),
    ]
