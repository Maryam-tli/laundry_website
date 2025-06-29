from django.db import models

# Create your models here.
class schedule(models.Model):
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