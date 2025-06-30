from django.shortcuts import render, get_object_or_404
from blog_app.models import *

# Create your views here.
def blog_view(request):
    posts = Post.objects.filter(status=True).order_by('-published_date')
    context = {'posts': posts,}
    return render(request, 'blog.html', context)

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, status=True)
    context = {'post': post}
    return render(request, 'blog-post.html', context)