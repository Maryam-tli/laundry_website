from django.urls import path
from blog_app.views import *

urlpatterns = [
    path('', blog_view, name='blog'),
    path('post/<slug:slug>/', post_detail, name='post_detail'),
    path('search/', search_view, name='search'),
    path('tag/<slug:slug>/', tagged_posts, name='tagged_posts'),
    path('category/<slug:slug>/', blog_view, name='category'),
    path('author/<slug:slug>/', author_view, name='author'),
]