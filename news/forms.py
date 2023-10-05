from django import forms
from news.models import ContactModel

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = ('first_name', 'last_name', 'email', 'message')

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control'}),
        }