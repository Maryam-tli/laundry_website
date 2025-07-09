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

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['full_name', 'email', 'phone', 'subject', 'message', 'agree']
        widgets = {
            'message': forms.Textarea(attrs={
                'rows': 4,
                'cols': 50,
                'placeholder': 'Write your message here...',
                'class': 'form-control form-control-sm'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            if not isinstance(field.widget, forms.CheckboxInput):
                existing_classes = field.widget.attrs.get('class', '')
                field.widget.attrs['class'] = f'{existing_classes} form-control form-control-sm'.strip()
        self.fields['agree'].label = "I agree to the terms & conditions and privacy policy"


    def clean_agree(self):
        agree = self.cleaned_data.get('agree')
        if not agree:
            raise forms.ValidationError("You must agree to the terms and conditions.")
        return agree
