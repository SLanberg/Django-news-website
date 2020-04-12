from django import template
from ..models import Category

register = template.Library()

def get_categories(context, order, count):
	categories = Category.objects.filter(published=True).order_by(order)
	if count is not None:
		categories = categories[:count]
	return categories


#https://docs.djangoproject.com/en/2.2/ref/templates/builtins/#for

#CATEGORIES WITH TEMPLATE USAGE
@register.inclusion_tag('/base/tags/base_tag.html', takes_context=True)
def category_list(context, order='-name', count=None, template='base/blog/categories.html'):
	categories = get_categories(context, order, count)
	return {'template': template, "category_list":categories}


#CATEGORIES WITHOUT TEMPLATE USAGE
@register.simple_tag(takes_context=True)
def for_category_list(context, count=None, order='-name'):
	return get_categories(context, order, count)
