from django.shortcuts import render, redirect
from django.core.mail import send_mail
from laundry_app.forms import *
from django.contrib import messages
from blog_app.models import Author

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
    Author_list = Author.objects.all()
    return render(request, 'about.html', {'form': form, 'form_2': form_2, 'Author_list': Author_list})

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

def contact_view(request):
    form = ContactForm()
    form_2 = subscriberForm()
    form_3 = scheduleForm()
    if 'contact_submit' in request.POST:
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_message = form.save()
            messages.success(request, 'Your message has been sent successfully!')
            send_mail(
                'Thank you for contacting us',
                f"""Dear {contact_message.full_name},Thank you for reaching out to us. We have received your message with the following details:
                Subject: {contact_message.subject}
                Message:
                {contact_message.message}
                We will get back to you soon.
                Best regards,  
                The Laundry Team
                """,
                'maryamtli@zohomail.com',
                [contact_message.email],
                fail_silently=False,
            )
        else:
            messages.error(request, "There was a problem with your submission. Please correct the errors below.")


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
            return redirect('contact')

    elif 'schedule_submit' in request.POST:
        form_3 = scheduleForm(request.POST)
        if form_3.is_valid():
            pickup = form_3.save()
            send_mail(
                'Pickup Scheduled',
                f'Your pickup is scheduled on {pickup.date} at {pickup.time}.',
                'maryamtli@zohomail.com',
                [pickup.email],
                fail_silently=False,
            )
            return redirect('contact')

    return render(request, 'contact.html', {'form': form, 'form_2': form_2, 'form_3': form_3})

from django.core.management import call_command
from django.http import HttpResponse

def load_data(request):
    try:
        call_command('loaddata', 'data.json')
        return HttpResponse("✅ Data loaded successfully!")
    except Exception as e:
        return HttpResponse(f"❌ Error: {e}")
    
def privacy_policy_view(request):
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
            return redirect('privacy_policy')

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
            return redirect('privacy_policy')
    else:
        form = scheduleForm()
        form_2 = subscriberForm()
    return render(request, 'privacy-policy.html', {'form': form, 'form_2': form_2})

def custom_404(request, exception):
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
    return render(request, '404.html', {'form_2': form_2} ,status=404)