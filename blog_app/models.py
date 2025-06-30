from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from taggit.managers import TaggableManager

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to='author_photos/', blank=True, null=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    STATUS_CHOICES = (
        (True, 'Published'),
        (False, 'Draft'),
    )

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True, help_text="Leave blank to auto-generate from title.")
    content = models.TextField()
    image = models.ImageField(
        upload_to='post_images/',
        default='post_images/default.JPG',
        blank=False,
        null=False,
        help_text="Upload image with size 1500x1000"
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now=True)
    status = models.BooleanField(choices=STATUS_CHOICES, default=False)
    tags = TaggableManager()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
