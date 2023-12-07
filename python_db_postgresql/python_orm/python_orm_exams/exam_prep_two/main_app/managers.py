from django.db import models
from django.db.models import Count


class ProfileManager(models.Manager):

    def get_regular_customers(self):
        profile_orders = self.annotate(orders_count=Count('order')
                                       ).filter(orders_count__gt=2).order_by('-orders_count')

        return profile_orders
