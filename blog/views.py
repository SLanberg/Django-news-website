from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import View

from .models import (
	Category,
	Tag,
	Post,
	Commentary,
)







class HomeView(View):
	"""Home page"""
	def get(self, request):
		post_list = Post.objects.all()
		return render(request, 'blog/home_page.html', {'posts': post_list})




class PostView(View):
	"""Article of Category"""
	def get(self, request, slug):
		post = Post.objects.get(slug=slug)
		return render(request, 'blog/post_detail.html', {'post':post})