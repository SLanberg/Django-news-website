# Generated by Django 3.0.4 on 2020-04-26 13:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('menu', '0004_auto_20200411_1523'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu_item',
            name='active',
        ),
        migrations.RemoveField(
            model_name='menu_item',
            name='is_auth',
        ),
        migrations.AddField(
            model_name='menu_item',
            name='content_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType', verbose_name='link to'),
        ),
        migrations.AddField(
            model_name='menu_item',
            name='obj_id',
            field=models.PositiveIntegerField(default=1, null=True, verbose_name='id'),
        ),
        migrations.AddField(
            model_name='menu_item',
            name='published',
            field=models.BooleanField(default=False, verbose_name='Publish?'),
        ),
        migrations.AddField(
            model_name='menu_item',
            name='sort',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='menu_item',
            name='anchor',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Anchor'),
        ),
        migrations.AlterField(
            model_name='menu_item',
            name='menu',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='menu.menu_main'),
        ),
        migrations.AlterField(
            model_name='menu_item',
            name='status',
            field=models.BooleanField(default=False, verbose_name='for authenticated?'),
        ),
    ]