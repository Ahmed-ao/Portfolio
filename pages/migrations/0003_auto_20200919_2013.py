# Generated by Django 2.2.13 on 2020-09-19 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20200919_1950'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='username',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='contact',
            name='service',
            field=models.CharField(choices=[('webapp', 'Web App'), ('api', 'Api'), ('consultancy', 'Consultancy'), ('theme', 'Theme'), ('Upgradewebapp', 'Upgrade Web App')], max_length=2000),
        ),
    ]
