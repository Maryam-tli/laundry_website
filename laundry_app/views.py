from django.shortcuts import render, redirect
from django.core.mail import send_mail
from laundry_app.forms import *

# Create your views here.
def home_view(request):
    if 'subscribe_submit' in request.POST:
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
        form_2 = subscriberForm()
    return render(request, 'home.html', {'form_2': form_2})

def about_view(request):
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
            return redirect('about')

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
            return redirect('about')
    else:
        form = scheduleForm()
        form_2 = subscriberForm()
    return render(request, 'about.html', {'form': form, 'form_2': form_2})

def services_view(request):
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
            return redirect('services')

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
            return redirect('services')
    else:
        form = scheduleForm()
        form_2 = subscriberForm()
    
    return render(request, 'services.html', {'form': form, 'form_2': form_2})
