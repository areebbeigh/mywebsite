from django.contrib.sitemaps import Sitemap
from coding_portfolio.models import Project


class ProjectSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.7

    def items(self):
        return Project.objects.all()

    def lastmod(self, item):
        return item.publish_data
