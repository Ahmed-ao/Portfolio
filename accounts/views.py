from django.shortcuts import render
from .forms import ContactForms

from django.views.generic import TemplateView

class Contact(TemplateView):
    form: ContactForms();
    template_name = 'Contact.html'
