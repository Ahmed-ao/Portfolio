from django.db import models

CHOICES = [
    ('theme', 'Theme'),
    ('api', 'Api'),
    ('webapp', 'Web App'),
    ('consultancy', 'Consultancy'),
    ('Upgradewebapp', 'Upgrade Web App'),
]


class Contact(models.Model):
    name = models.CharField(max_length=50,)
    email = models.EmailField(max_length=254)
    message = models.CharField(
        max_length=50, )
    service = models.CharField(
        max_length=2000, choices=CHOICES)
    comment = models.CharField(max_length=50, )

    def __str__(self):
        return self.email
