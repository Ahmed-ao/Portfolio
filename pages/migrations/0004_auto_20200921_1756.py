# Generated by Django 2.2.13 on 2020-09-21 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20200919_2013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='service',
            field=models.CharField(choices=[('theme', 'Theme'), ('api', 'Api'), ('webapp', 'Web App'), ('consultancy', 'Consultancy'), ('Upgradewebapp', 'Upgrade Web App')], max_length=2000),
        ),
    ]
