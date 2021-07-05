from django.contrib.sitemaps import Sitemap
from women.models import Women

class WomenSitemap(Sitemap):

    def items(self):
        return Women.objects.all()
