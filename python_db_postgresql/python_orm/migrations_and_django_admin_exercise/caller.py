import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Shoe


def add_initial_products():
    shoe1 = Shoe(
        brand="Nike",
        size=34
    )

    shoe1.save()

    shoe2 = Shoe(
        brand="Nike",
        size=31
    )

    shoe2.save()

    shoe3 = Shoe(
        brand="Adidas",
        size=45
    )

    shoe3.save()

    shoe4 = Shoe(
        brand="Adidas",
        size=42
    )

    shoe4.save()

    shoe5 = Shoe(
        brand="Puma",
        size=21
    )

    shoe5.save()

    return f"{shoe1}, {shoe2}, {shoe3}, {shoe4}, {shoe5}"


# print(add_initial_products())

















