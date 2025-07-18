from django.db import models

# Create your models here.
class schedule(models.Model):
    full_name = models.CharField(max_length=100, blank=False, null=False)
    date = models.DateField()
    time = models.TimeField()
    email = models.EmailField()
    phone_number = models.CharField(max_length=15, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.date} at {self.time}"
    
class Subscriber(models.Model):
    email = models.EmailField()
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class ContactMessage(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(help_text="Please enter a valid email address")
    phone = models.CharField(max_length=20)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    agree = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.full_name} - {self.subject}"
