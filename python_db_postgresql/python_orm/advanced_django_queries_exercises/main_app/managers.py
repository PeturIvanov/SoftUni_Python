from django.db import models
from django.db.models import QuerySet, Count, Max, Min, Avg
from decimal import Decimal


class RealEstateListingManager(models.Manager):
    def by_property_type(self, property_type: str) -> QuerySet:
        return self.filter(property_type=property_type)

    def in_price_range(self, min_price: Decimal, max_price: Decimal) -> QuerySet:
        return self.filter(price__gte=min_price, price__lte=max_price)

    def with_bedrooms(self, bedrooms_count: int) -> QuerySet:
        return self.filter(bedrooms=bedrooms_count)

    def popular_locations(self):
        return self.values('location').annotate(
            locations_count=Count('location')).order_by('-locations_count', 'id')[:2]


class VideoGameManager(models.Manager):
    def games_by_genre(self, genre: str) -> QuerySet:
        return self.filter(genre=genre)

    def recently_released_games(self, year: int) -> QuerySet:
        return self.filter(release_year__gte=year)

    def highest_rated_game(self):
        rating = self.aggregate(highest_rating=Max('rating'))['highest_rating']
        return self.get(rating=rating)

    def lowest_rated_game(self):
        return self.annotate(min_rating=Min('rating')).order_by('rating').first()

    def average_rating(self):
        average_rating = self.aggregate(avg_rating=Avg('rating'))['avg_rating']

        return f"{average_rating:.1f}"
















