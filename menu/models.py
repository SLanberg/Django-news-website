from django.db import models
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel

# Create your models here.


class menu_main(models.Model):
	name    	= models.CharField(verbose_name='Name', max_length=100)
	is_auth 	= models.BooleanField(verbose_name='for authenticated?', default=False)
	active  	= models.BooleanField(verbose_name='active?', default=False)

	def __str__(self):
		return self.name

#Inherit from MPTT?

class menu_item(MPTTModel):
	name   		= models.CharField(verbose_name='Name', max_length=100)
	title  		= models.CharField(verbose_name='Title', max_length=100)
	parent 		= TreeForeignKey(
		'self',
		on_delete=models.CASCADE,
		null=True,
		blank=True,
		related_name='children'
	)
	menu   		= models.ForeignKey(
		menu_main,
		verbose_name="menu",
		on_delete=models.CASCADE,
		null=True,
	)
	status      = models.BooleanField(verbose_name='status?', default=False)
	is_auth 	= models.BooleanField(verbose_name='for authenticated?', default=False)
	anchor 		= models.CharField(verbose_name='Anchor', max_length=100)
	url 		= models.CharField(verbose_name='External resource url', null=True, blank=True, max_length=100)
	active 		= models.BooleanField(verbose_name='active?', default=False)

	def __str__(self):
		return self.name