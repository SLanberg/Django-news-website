from django.contrib.sitemaps import Sitemap

from .models import page


class PagesSitemap(Sitemap):
    priority = 0.9
    # protocol = 'https'
    limit = 1000

    def items(self):
        return page.objects.filter(published=True)

    def lastmod(self, obj):
        return obj.published_date