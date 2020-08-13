from django.shortcuts import render
<<<<<<< HEAD

# Create your views here.
=======
from .forms import contact

def contact(request):
    form = contact()
    render(request, "contact.html", {"form": form})
>>>>>>> accounts
