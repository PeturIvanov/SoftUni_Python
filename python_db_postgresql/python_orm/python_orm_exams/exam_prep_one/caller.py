import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Director, Actor, Movie
from django.db.models import Q, Count, Avg, Max, F


def get_directors(search_name=None, search_nationality=None):
    if search_name is None and search_nationality is None:
        return ""

    directors = Director.objects.all()

    if search_name:
        directors = directors.filter(full_name__icontains=search_name)

    if search_nationality:
        directors = directors.filter(nationality__icontains=search_nationality)

    directors = directors.order_by('full_name')

    result = [
        f"Director: {director.full_name}, nationality: {director.nationality}, experience: {director.years_of_experience}"
        for director in directors
    ]

    return "\n".join(result)


def get_top_director():
    top_director = Director.objects.get_directors_by_movies_count().first()

    return f"Top Director: {top_director.full_name}, movies: {top_director.number_movies}." if top_director else ""


def get_top_actor():
    top_actor = Actor.objects.annotate(
        staring_movies_count=Count('movie'),
        avg_rating=Avg('movie__rating')).order_by('-staring_movies_count', 'full_name').first()

    if top_actor is None or not top_actor.staring_movies_count:
        return ''

    actor_movies = ", ".join([movie.title for movie in top_actor.movie_set.all()])

    return f"Top Actor: {top_actor.full_name}," \
           f" starring in movies: {actor_movies}," \
           f" movies average rating: {top_actor.avg_rating:.1f}"


def get_actors_by_movies_count():
    actors = Actor.objects.annotate(movies_count=Count('movies')).filter(movies_count__gt=0).order_by('-movies_count',
                                                                                                      'full_name')

    if actors.count() >= 3:
        actors = actors[:3]

    result = [f"{actor.full_name}, participated in {actor.movies_count} movies" for actor in actors]

    return '\n'.join(result)


def get_top_rated_awarded_movie():
    top_movie = Movie.objects.prefetch_related('actors'
                                               ).filter(is_awarded=True
                                                        ).order_by('-rating', 'title'
                                                                   ).first()

    if top_movie is None:
        return ""

    staring_actor = top_movie.starring_actor.full_name if top_movie.starring_actor else "N/A"

    cast = ", ".join([f"{actor.full_name}" for actor in top_movie.actors.all().order_by('full_name')])

    return f"Top rated awarded movie: {top_movie.title}, rating: {top_movie.rating:.1f}. " \
           f"Starring actor: {staring_actor}. Cast: {cast}."


def increase_rating():
    updated_movies_count = Movie.objects.filter(is_classic=True, rating__lt=10).update(rating=F('rating') + 0.1)

    if updated_movies_count == 0:
        return 'No ratings increased.'

    return f"Rating increased for {updated_movies_count} movies."



















