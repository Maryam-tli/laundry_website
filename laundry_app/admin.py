from django.contrib import admin
from laundry_app.models import *

# Register your models here.
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('date', 'time', 'created_at', 'email', 'phone_number')
    search_fields = ('date', 'time')
    fields = ('date', 'time', 'email', 'phone_number')
admin.site.register(schedule, ScheduleAdmin)

class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'subscribed_at')
    search_fields = ('email',)
    fields = ('email',)
admin.site.register(Subscriber, SubscriberAdmin)

class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone', 'subject', 'created_at', 'agree')
    search_fields = ('full_name', 'agree', 'subject')
    fields = ('full_name', 'email', 'phone', 'subject', 'message', 'agree')
admin.site.register(ContactMessage, ContactMessageAdmin)