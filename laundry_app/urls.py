from django.urls import path
from laundry_app.views import *

urlpatterns = [
    path('', home_view, name='home'),
    path('about/', about_view, name='about'),
    path('services/', services_view, name='services'),
    path('contact/', contact_view, name='contact'),
]