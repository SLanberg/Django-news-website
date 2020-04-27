from django.db import models
from django.urls import get_script_prefix
from django.utils.encoding import iri_to_uri

# Create your models here.


class page(models.Model):
	title				  =	models.CharField(verbose_name='Title', max_length=100)
	sub_title			  = models.CharField(verbose_name='Sub title', max_length=500, blank=True, null=True)
	text				  =	models.TextField(max_length=500, blank=True, null=True)
	edit_date			  =	models.DateTimeField(verbose_name='Date of edit', auto_now=True, blank=True, null=True)
	published_date		  =	models.DateTimeField(blank=True, null=True)
	published			  =	models.BooleanField(verbose_name="Publish?", default=True)
	template			  = models.CharField(max_length=500, default='blog/post_detail.html')
	registration_required = models.BooleanField(
							help_text='If you check this checkbox, only authenticated users can see page',
							default=False,
							)

	slug 				  = models.CharField('url', max_length=100, unique=True)

	def __str__(self):
		return self.title

	def save(self, *args, **kwargs):
		if self.slug is None:
			self.slug = "/"
		if not f"{self.slug}".startswith('/'):
			self.slug = "/" + self.slug
		if not self.slug.endswith("/"):
			self.slug += "/"
		super().save(*args, **kwargs)

	def get_absolute_url(self):
		return iri_to_uri(get_script_prefix().rstrip('/') + self.slug)

	class Meta:
		unique_together = ('slug', )


