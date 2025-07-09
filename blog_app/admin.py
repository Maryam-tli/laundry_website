from django.contrib import admin
from blog_app.models import *
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
admin.site.register(Category, CategoryAdmin)

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'bio')
    search_fields = ('name',)
    fields = ('name', 'slug', 'bio', 'photo')
admin.site.register(Author, AuthorAdmin)

class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'category', 'author', 'created_date', 'published_date', 'status')
    search_fields = ('title', 'content')
    list_filter = ('category', 'author', 'status')
    fields = ('title', 'content', 'slug','image', 'category', 'author', 'status', 'tags')
    summernote_fields = ('content',)
admin.site.register(Post, PostAdmin)