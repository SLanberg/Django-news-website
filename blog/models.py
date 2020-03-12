from django.db import models





class Category(models.Model):
	"""Category model"""
	name = models.CharField(verbose_name='Name', max_length=100)
	slug = models.SlugField(verbose_name='url', max_length=100)



	def __str__(self):
		return self.name



	class Meta:
		verbose_name_plural = 'categories'




class Tag(models.Model):
	"""Tag model"""
	name = models.CharField(verbose_name='Tag', max_length=100)
	slug = models.SlugField(verbose_name='Slug', max_length=100)


	def __str__(self):
		return self.name



class Post(models.Model):
	"""Post model"""
	title 		  = models.CharField(verbose_name='Title', max_length=100)
	mini_text 	  = models.TextField(verbose_name='Mini Text', max_length=100)
	text 		  = models.TextField(verbose_name='Text', max_length=16000)
	creation_date = models.DateTimeField(auto_now=True)
	slug          = models.SlugField(verbose_name='Slug', max_length=100)

	def __str__(self):
		return self.title




class Commentary(models.Model):
	text 		  = models.TextField(verbose_name='Text', max_length=244)
	creation_date = models.DateTimeField(auto_now=True)
	moderation    = models.BooleanField()


	def __str__(self):
		return self.text



	class Meta:
		verbose_name_plural = 'commentaries'