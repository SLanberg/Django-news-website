from django.conf import settings
from django.http import Http404, HttpResponsePermanentRedirect
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_protect

from .models import page

def get_page(request, url):
	if not url.startswith('/'):
		url = '/' + url
	try:
		page_i = get_object_or_404(page, slug=url, published=True)
	except Http404:
		if not url.endswith('/') and settings.APPEND_SLASH:
			url += '/'
			page_i = get_object_or_404(page, slug=url, published=True)
			return HttpResponsePermanentRedirect('%s/' % request.path)
		else:
			raise

	return render_page(request, page_i)



@csrf_protect
def render_page(request, page):
	if page.registration_required and not request.user.is_authenthicated:
		from django.contrib.auth.views import redirect_to_login
		return redirect_to_login(request.path)
	return render(request, page.template, {'page': page})