from django.shortcuts import render, redirect
from django.core.mail import send_mail
from laundry_app.forms import *

# Create your views here.
def home_view(request):
    return render(request, 'home.html')

def about_view(request):
    return render(request, 'about.html')

def services_view(request):
    form = scheduleForm()
    return render(request, 'services.html', {'form': form})

def schedule_view(request):
    if request.method == 'POST':
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
    else:
        form = scheduleForm()

    return render(request, 'services.html', {'form': form})