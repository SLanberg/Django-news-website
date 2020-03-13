from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import View
from django.utils import timezone

from .models import (
	Category,
	Tag,
	Post,
	Commentary,
)



class HomeView(View):
    """All categories and all posts"""
    def get(self, request):
        category_list = Category.objects.all()
        post_list = Post.objects.filter(published=True, published_date__lte=timezone.now())
        return render(request, "blog/post_list.html", {"categories": category_list, "post_list": post_list})


class PostDetailView(View):
    """Show specific post"""
    def get(self, request, category, slug):
        category_list = Category.objects.all()
        post = Post.objects.get(slug=slug)
        return render(request, post.template, {"categories": category_list, "post": post})


class CategoryView(View):
    """Show articles by category"""
    def get(self, request, slug):
        category = Category.objects.get(slug=slug)
        return render(request, "blog/post_list.html", {"category": category})