from django.db import models
from django.db.models import Count


class DirectorManager(models.Manager):

    def get_directors_by_movies_count(self):
        return self.annotate(number_movies=Count('movie')).order_by('-number_movies', 'full_name')




