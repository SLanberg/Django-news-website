from django.db import models





class Category(models.Model):


	# Category model
	name = models.CharField(verbose_name='Name', max_length=100)
	slug = models.SlugField(verbose_name='url', max_length=100)



	def __str__(self):
		return self.name



	class Meta:
		verbose_name_plural = 'categories'