from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

"""MPTT import"""
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel




class Category(MPTTModel):
	"""Category model"""
	name 			= models.CharField(verbose_name='Name', max_length=100)
	slug 			= models.SlugField(verbose_name='url', max_length=100, unique=True)
	description 	= models.TextField(max_length=1000, default="", blank=True)
	parent 			= TreeForeignKey(
		'self',
		on_delete=models.CASCADE,
		null=True,
		blank=True,
		related_name='children'
	)
	template 		= models.CharField(max_length=500, default='blog/post_list.html')
	published		= models.BooleanField(verbose_name='Publicate?', default=True)
	paginated		= models.PositiveIntegerField(verbose_name='amount of articles on single page', default=5)
	sort			= models.PositiveIntegerField(default=0)







	def __str__(self):
		return self.name



	class Meta:
		verbose_name_plural = 'categories'




class Tag(models.Model):
	"""Tag model"""
	name 		= models.CharField(verbose_name='Tag', max_length=100)
	slug 		= models.SlugField(verbose_name='Slug', max_length=100, unique=True)
	published	= models.BooleanField(verbose_name='Show tag?', default=True)

	def __str__(self):
		return self.name



class Post(models.Model):
	"""Post model"""
	author = models.ForeignKey(
		User,
		on_delete=models.SET_NULL,
		null=True,
		blank=True,
)
	title 		  = models.CharField(verbose_name='Title', max_length=100)
	subtitle	  = models.CharField(max_length=500, blank=True, null=True)
	mini_text 	  = models.TextField(verbose_name='Mini Text', max_length=100)
	text 		  = models.TextField(verbose_name='Text', max_length=16000)
	creation_date = models.DateTimeField(auto_now=True)
	slug          = models.SlugField(max_length=100, unique=True)
	


	edit_date 	  = models.DateTimeField(
		"Edit date",
		default=timezone.now,
		blank=True,
		null=True,
	)


	published_date = models.DateTimeField(
		"Publication date",
		default=timezone.now,
		blank=True,
		null=True,
	)


	category = models.ForeignKey(
		Category,
		verbose_name="Category",
		on_delete=models.CASCADE,
		null=True,
	)

	image    	= models.ImageField('Main photo', upload_to='post/', null=True, blank=True)

	tags 	 	= models.ManyToManyField(Tag, blank=True)
	
	template 	= models.CharField(max_length=500, default='blog/post_detail.html')

	published	= models.BooleanField(verbose_name='Publicate?', default=True)

	viewed		= models.PositiveIntegerField(default=0)

	status		= models.BooleanField(verbose_name='For Registered', default=False)

	sort		= models.PositiveIntegerField(default=0)


	def get_absolute_url(self):
		return reverse('detail_post', kwargs={'category': self.category.slug, 'slug':self.slug})


	def __str__(self):
		return self.title





class Commentary(models.Model):
	"""Model of Post Commentary"""
	author = models.ForeignKey(
		User,
		on_delete=models.CASCADE,
		null=True
)

	post 		  = models.ForeignKey(Post, verbose_name="Article", on_delete=models.CASCADE, blank=True)
	text 		  = models.TextField(verbose_name='Text', max_length=244)
	creation_date = models.DateTimeField(auto_now=True)
	moderation    = models.BooleanField()


	def __str__(self):
		return self.text



	class Meta:
		verbose_name_plural = 'commentaries'