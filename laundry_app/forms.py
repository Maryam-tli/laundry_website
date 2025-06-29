from django import forms
from laundry_app.models import *

class scheduleForm(forms.ModelForm):
    class Meta:
        model = schedule
        fields = '__all__'

class subscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = '__all__'