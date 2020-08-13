from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import ContactForms


# class Home(TemplateView):
#     form = ContactForms()
#     template_name = 'index.html'


def home(request):
    form = ContactForms()
    return render(request, "index.html", {"form": form})
