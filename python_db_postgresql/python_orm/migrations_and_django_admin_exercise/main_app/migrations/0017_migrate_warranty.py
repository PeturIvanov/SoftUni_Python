# Generated by Django 4.2.4 on 2023-11-08 16:39

from django.db import migrations
from django.utils import timezone


def update_delivery_warranty(apps, schema_editor):
    order_model = apps.get_model('main_app', 'Order')
    orders = order_model.objects.all()

    for order in orders:
        if order.status == 'Pending':
            order.delivery = order.order_date + timezone.timedelta(days=3)

        elif order.status == 'Completed':
            order.warranty = '24 months'

        else:
            order.delete()

        order.save()


def reverse_delivery_and_warranty(apps, schema_editor):
    order_model = apps.get_model('main_app', 'Order')
    orders = order_model.objects.all()

    default_warranty = order_model._meta.get_field('warranty').default

    for order in orders:
        if order.status == 'Pending':
            order.delivery = None

        elif order.status == 'Completed':
            order.warranty = default_warranty

    order_model.objects.bulk_update(orders, ['delivery', 'warranty'])


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0016_order'),
    ]

    operations = [
        migrations.RunPython(update_delivery_warranty, reverse_code=reverse_delivery_and_warranty)
    ]
