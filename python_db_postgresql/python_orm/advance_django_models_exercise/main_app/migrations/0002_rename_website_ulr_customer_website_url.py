# Generated by Django 4.2.4 on 2023-11-25 09:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='website_ulr',
            new_name='website_url',
        ),
    ]