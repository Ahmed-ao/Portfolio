from django.shortcuts import render
from .forms import contact

def contact(request):
    form = contact()
    render(request, "contact.html", {"form": form})