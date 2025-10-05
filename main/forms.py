from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_class = 'contact-form'
        
        # Field styling
        self.fields['name'].widget.attrs.update({
            'class': 'form-control form-control-lg',
            'placeholder': 'Your Full Name'
        })
        
        self.fields['email'].widget.attrs.update({
            'class': 'form-control form-control-lg',
            'placeholder': 'your.email@example.com'
        })
        
        self.fields['subject'].widget.attrs.update({
            'class': 'form-control form-control-lg',
            'placeholder': 'Subject of your message'
        })
        
        self.fields['message'].widget.attrs.update({
            'class': 'form-control form-control-lg',
            'placeholder': 'Your message...',
            'rows': 5
        })
