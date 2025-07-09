from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from blog_app.models import *
from laundry_app.forms import *
from taggit.models import Tag
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def blog_view(request, slug=None):
    posts_list = Post.objects.filter(status=True).order_by('-published_date')
    if slug:
        posts_list = posts_list.filter(category__slug=slug)

    paginator = Paginator(posts_list, 4)

    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    categories = Category.objects.all()
    tags = Tag.objects.filter(taggit_taggeditem_items__isnull=False).distinct()
    latest_posts = Post.objects.filter(status=True).order_by('-published_date')[:3]
    if 'schedule_submit' in request.POST:
        form = scheduleForm(request.POST)
        if form.is_valid():
            pickup = form.save()
            send_mail(
                'Pickup Scheduled',
                f'Your pickup is scheduled on {pickup.date} at {pickup.time}.',
                'maryamtli@zohomail.com',
                [pickup.email],
                fail_silently=False,
            )
            return redirect('home')

    elif 'subscribe_submit' in request.POST:
        form_2 = subscriberForm(request.POST)
        if form_2.is_valid():
            subscriber = form_2.save()
            send_mail(
                'Welcome to Our Newsletter – You’re Subscribed!',
                f'Dear User,Thank you for subscribing to our newsletter! We will keep you updated with our latest news and offers.{subscriber.subscribed_at}',
                'maryamtli@zohomail.com',
                [subscriber.email],
                fail_silently=False,
            )
            return redirect('home')
    else:
        form = scheduleForm()
        form_2 = subscriberForm()

    context = {
        'posts': posts,
        'categories': categories,
        'tags': tags,
        'latest_posts': latest_posts,
        'form': form,
        'form_2': form_2,
    }
    return render(request, 'blog.html', context)


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, status=True)
    categories = Category.objects.all()
    tags = Tag.objects.filter(taggit_taggeditem_items__isnull=False).distinct()
    latest_posts = Post.objects.filter(status=True).order_by('-published_date')[:3]
    if 'schedule_submit' in request.POST:
        form = scheduleForm(request.POST)
        if form.is_valid():
            pickup = form.save()
            send_mail(
                'Pickup Scheduled',
                f'Your pickup is scheduled on {pickup.date} at {pickup.time}.',
                'maryamtli@zohomail.com',
                [pickup.email],
                fail_silently=False,
            )
            return redirect('home')

    elif 'subscribe_submit' in request.POST:
        form_2 = subscriberForm(request.POST)
        if form_2.is_valid():
            subscriber = form_2.save()
            send_mail(
                'Welcome to Our Newsletter – You’re Subscribed!',
                f'Dear User,Thank you for subscribing to our newsletter! We will keep you updated with our latest news and offers.{subscriber.subscribed_at}',
                'maryamtli@zohomail.com',
                [subscriber.email],
                fail_silently=False,
            )
            return redirect('home')
    else:
        form = scheduleForm()
        form_2 = subscriberForm()

    context = {
        'post': post,
        'categories': categories,
        'tags': tags,
        'latest_posts': latest_posts,
        'form': form,
        'form_2': form_2,
    }
    return render(request, 'blog-post.html', context)

def search_view(request):
    posts = Post.objects.filter(status=True)
    query = request.GET.get('s')
    if query:
        posts = posts.filter(title__icontains=query)
    paginator = Paginator(posts, 4)

    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    categories = Category.objects.all()
    tags = Tag.objects.filter(taggit_taggeditem_items__isnull=False).distinct()
    latest_posts = Post.objects.filter(status=True).order_by('-published_date')[:3]
    if 'schedule_submit' in request.POST:
        form = scheduleForm(request.POST)
        if form.is_valid():
            pickup = form.save()
            send_mail(
                'Pickup Scheduled',
                f'Your pickup is scheduled on {pickup.date} at {pickup.time}.',
                'maryamtli@zohomail.com',
                [pickup.email],
                fail_silently=False,
            )
            return redirect('home')

    elif 'subscribe_submit' in request.POST:
        form_2 = subscriberForm(request.POST)
        if form_2.is_valid():
            subscriber = form_2.save()
            send_mail(
                'Welcome to Our Newsletter – You’re Subscribed!',
                f'Dear User,Thank you for subscribing to our newsletter! We will keep you updated with our latest news and offers.{subscriber.subscribed_at}',
                'maryamtli@zohomail.com',
                [subscriber.email],
                fail_silently=False,
            )
            return redirect('home')
    else:
        form = scheduleForm()
        form_2 = subscriberForm()

    context = {'posts': posts,
        'categories': categories,
        'tags': tags,
        'latest_posts': latest_posts,
        'form': form,
        'form_2': form_2,}
    return render(request, 'blog.html', context)

def tagged_posts(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    posts = Post.objects.filter(tags__slug=slug, status=True).distinct()
    paginator = Paginator(posts, 4)

    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    categories = Category.objects.all()
    tags = Tag.objects.filter(taggit_taggeditem_items__isnull=False).distinct()
    latest_posts = Post.objects.filter(status=True).order_by('-published_date')[:3]
    if 'schedule_submit' in request.POST:
        form = scheduleForm(request.POST)
        if form.is_valid():
            pickup = form.save()
            send_mail(
                'Pickup Scheduled',
                f'Your pickup is scheduled on {pickup.date} at {pickup.time}.',
                'maryamtli@zohomail.com',
                [pickup.email],
                fail_silently=False,
            )
            return redirect('home')

    elif 'subscribe_submit' in request.POST:
        form_2 = subscriberForm(request.POST)
        if form_2.is_valid():
            subscriber = form_2.save()
            send_mail(
                'Welcome to Our Newsletter – You’re Subscribed!',
                f'Dear User,Thank you for subscribing to our newsletter! We will keep you updated with our latest news and offers.{subscriber.subscribed_at}',
                'maryamtli@zohomail.com',
                [subscriber.email],
                fail_silently=False,
            )
            return redirect('home')
    else:
        form = scheduleForm()
        form_2 = subscriberForm()

    return render(request, 'blog.html', {
        'tag': tag,
        'posts': posts,
        'categories': categories,
        'tags': tags,
        'latest_posts': latest_posts,
        'form': form,
        'form_2': form_2,
    })

def author_view(request, slug):
    author = get_object_or_404(Author, slug=slug)
    posts = Post.objects.filter(author=author, status=True).order_by('-published_date')
    categories = Category.objects.all()
    tags = Tag.objects.filter(taggit_taggeditem_items__isnull=False).distinct()
    latest_posts = Post.objects.filter(status=True).order_by('-published_date')[:3]

    context = {
        'author': author,
        'posts': posts,
        'categories': categories,
        'tags': tags,
        'latest_posts': latest_posts,
    }
    return render(request, 'author.html', context)