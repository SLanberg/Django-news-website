from django.conf import settings
from django.db import models

from django.contrib.sites.models import Site
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel

# Create your models here.


class menu_main(models.Model):
	name    	   = models.CharField(verbose_name='Name', max_length=100)
	status 	   	   = models.BooleanField(verbose_name='for authenticated?', default=False)
	published  	   = models.BooleanField(verbose_name='active?', default=False)

	def items(self):
		return self.menuitem_set.all()

	def __str__(self):
		return self.name

#Inherit from MPTT?

class menu_item(MPTTModel):
	name   		   = models.CharField(verbose_name='Name', max_length=100)
	title  		   = models.CharField(verbose_name='Title', max_length=100)
	parent 		   = TreeForeignKey(
		'self',
		on_delete=models.CASCADE,
		null=True,
		blank=True,
		related_name='children'
	)
	menu   		 = models.ForeignKey(
		menu_main,
		on_delete=models.CASCADE,
		null=True,
	)
	status         = models.BooleanField(verbose_name='for authenticated?', default=False)
	anchor 		   = models.CharField(verbose_name='Anchor', max_length=100, null=True, blank=True)

	url 		   = models.CharField(verbose_name='External resource url', null=True, blank=True, max_length=100)
	published 	   = models.BooleanField(verbose_name='Publish?', default=False)

	sort 		   = models.PositiveIntegerField(default=0)
	obj_id 		   = models.PositiveIntegerField(verbose_name='id', default=1, null=True)
	content_object = GenericForeignKey('content_type', 'obj_id')

	content_type = models.ForeignKey(
		ContentType,
		verbose_name='link to',
		on_delete=models.CASCADE,
		null=True,
		blank=True)

	def get_anchor(self):
		if self.anchor:
			return "{}/#{}".format(site.objects.get_current().domain, self.anchor)
		else:
			return False

	def __str__(self):
		return self.name

	content_object.short_description = 'ID'

	class MPTTMeta:
		order_insertion_by = ('sort',)