# Generated by Django 3.0.4 on 2020-04-26 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0005_auto_20200426_1609'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu_main',
            name='active',
        ),
        migrations.RemoveField(
            model_name='menu_main',
            name='is_auth',
        ),
        migrations.AddField(
            model_name='menu_main',
            name='published',
            field=models.BooleanField(default=False, verbose_name='active?'),
        ),
        migrations.AddField(
            model_name='menu_main',
            name='status',
            field=models.BooleanField(default=False, verbose_name='for authenticated?'),
        ),
    ]
