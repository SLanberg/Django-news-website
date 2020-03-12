# Generated by Django 3.0.4 on 2020-03-12 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200312_0512'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commentary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=244, verbose_name='Text')),
                ('creation_date', models.DateTimeField(auto_now=True)),
                ('moderation', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('mini_text', models.TextField(max_length=100, verbose_name='Mini Text')),
                ('text', models.TextField(max_length=16000, verbose_name='Text')),
                ('creation_date', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(max_length=100, verbose_name='Slug')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Tag')),
                ('slug', models.SlugField(max_length=100, verbose_name='Slug')),
            ],
        ),
    ]
