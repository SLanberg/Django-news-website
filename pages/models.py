from django.db import models

# Create your models here.


class page(models.Model):
	title			=	models.CharField(verbose_name='Title', max_length=100)
	text			=	models.TextField(max_length=500)
	active			=	models.TextField(verbose_name='Text Field')
	template		=	models.CharField(max_length=500, default='page/index.html')
	slug			=	models.SlugField(verbose_name="url", max_length=100, unique=True)


models.CharField(max_length=500, default='blog/post_detail.html')