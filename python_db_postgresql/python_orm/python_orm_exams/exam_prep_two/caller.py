import os
import django
from django.db.models import Q, Count

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Profile, Order, Product


def get_profiles(search_string=None):
    if search_string is None:
        return ""

    query = Q(full_name__icontains=search_string
              ) | Q(phone_number__icontains=search_string
                    ) | Q(email__icontains=search_string)

    profiles = Profile.objects.filter(query).annotate(orders_count=Count('order')).order_by('full_name')

    result = [
        f"Profile: {p.full_name}, email: {p.email}, phone number: {p.phone_number}, orders: {p.orders_count}"
        for p in profiles
    ]

    return "\n".join(result)


def get_loyal_profiles():
    profiles = Profile.objects.get_regular_customers()

    if not profiles:
        return ""

    result = [
        f"Profile: {p.full_name}, orders: {p.orders_count}"
        for p in profiles
    ]

    return "\n".join(result)


def get_last_sold_products():
    latest_order = Order.objects.all().order_by('-creation_date').first()

    if not latest_order:
        return ""

    products = ", ".join(product.name for product in latest_order.products.all())

    return f"Last sold products: {products}"


























