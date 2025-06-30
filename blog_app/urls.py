from django.urls import path
from blog_app.views import *

urlpatterns = [
    path('', blog_view, name='blog'),
    path('post/<slug:slug>/', post_detail, name='post_detail'),
]