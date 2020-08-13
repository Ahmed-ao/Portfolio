from django import forms

class ContactForms(forms.Form):
    username = forms.CharField(label="Username",min_length=20, max_length=200, required=True)
    email = forms.EmailField(label="Email", min_length=20, required=True)
    message = forms.CharField(label="Your Message", min_length=20, max_length=200, required=True, widget=forms.Textarea(attrs={"rows":4, "cols":10}))