from django import forms


class ContactForms(forms.Form):
    username = forms.CharField(
        label="Name", min_length=20, max_length=200, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="Email", min_length=20, required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))
    message = forms.CharField(label="Your Message", min_length=20, max_length=200,
                              required=True, widget=forms.Textarea(attrs={'class': 'form-control'}))
