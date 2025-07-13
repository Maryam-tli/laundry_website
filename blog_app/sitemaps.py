from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from blog_app.models import Post, Category, Author
from taggit.models import Tag

class StaticViewSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.5

    def items(self):
        return ['blog']

    def location(self, item):
        return reverse(item)

class CategorySitemap(Sitemap):
    changefreq = "daily"
    priority = 0.5

    def items(self):
        return Category.objects.all()

    def location(self, obj):
        return reverse('category', kwargs={'slug': obj.slug})

class PostSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.9

    def items(self):
        return Post.objects.filter(status=True)
    
    def lastmod(self, obj):
        return obj.updated_at

    def location(self, obj):
        return reverse('post_detail', kwargs={'slug': obj.slug})

class AuthorSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return Author.objects.all()

    def location(self, obj):
        return reverse('author', kwargs={'slug': obj.slug})

class TagSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return Tag.objects.filter(taggit_taggeditem_items__isnull=False).distinct()

    def location(self, obj):
        return reverse('tagged_posts', kwargs={'slug': obj.slug})
