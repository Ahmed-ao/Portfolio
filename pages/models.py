from django.db import models

# Create your models here.


class Contact(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    message = models.CharField( max_length=50)
    service = models.CharField(max_length=50)
    comment = models.CharField(max_length=50)
