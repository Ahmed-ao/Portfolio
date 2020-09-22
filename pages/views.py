from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import ContactForm


def home(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        form.save()
        return HttpResponseRedirect('/thanks')
    return render(request, "index.html", {'form': form})


class Thanks(TemplateView):
    template_name = 'Contact.html'


def notfound(request, exception):
    return render(request, '404.html', status=404)


def servererror(request):
    return render(request, '500.html', status=500)


def permessiondenied(request, exception):
    return render(request, '403.html', status=403)


def badrequest(request, exception):
    return render(request, '400.html', status=400)
