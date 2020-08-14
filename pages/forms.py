from django import forms
from .models import Contact
CHOICES = [
    ('ui', 'UI/UX'),
    ('frontend', 'FrontEnd'),
    ('backend', 'BackEnd')
]


class ContactForms(forms.Form):
    class Meta:
        model = Contact
    username = forms.CharField(
        label="Name", min_length=20, max_length=200, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))

    email = forms.EmailField(label="Email", min_length=20, required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))
    service = forms.ChoiceField(choices=CHOICES)
    message = forms.CharField(label="Your Message", min_length=20, max_length=200,
                              required=True, widget=forms.Textarea(attrs={'class': 'form-control'}))
    comment = forms.CharField(label="Speical Comment", min_length=20, max_length=200,
                              required=True, widget=forms.Textarea(attrs={'class': 'form-control'}))
