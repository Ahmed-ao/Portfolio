from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'message', 'service',)

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'},),
            'email': forms.TextInput(attrs={'class': 'form-control'}, ),
            'message': forms.TextInput(attrs={'class': 'form-control'},),
            # 'comment': forms.TextInput(attrs={'class': 'form-control'},)
        }
