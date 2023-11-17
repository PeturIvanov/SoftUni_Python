import os
from datetime import timedelta, date

import django
from django.db.models import Sum, Count

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Author, Book, Artist, Song, Product, Review, DrivingLicense, Driver, Owner, Car, \
    Registration


def show_all_authors_with_their_books():
    authors = Author.objects.all().order_by('id')

    result = []

    for author in authors:
        books_by_author = author.book_set.all()

        if not books_by_author:
            continue

        result.append(
            f"{author} has written - {', '.join([str(book) for book in books_by_author])}!"
        )

    return "\n".join(result)


def delete_all_authors_without_books():
    Author.objects.filter(book__isnull=True).delete()


def add_song_to_artist(artist_name: str, song_title: str):
    artist = Artist.objects.get(name=artist_name)
    song = Song.objects.get(title=song_title)

    artist.songs.add(song)


def get_songs_by_artist(artist_name: str):
    return Artist.objects.get(name=artist_name).songs.all().order_by('-id')


def remove_song_from_artist(artist_name: str, song_title: str):
    artist = Artist.objects.get(name=artist_name)
    song = Song.objects.get(title=song_title)

    artist.songs.remove(song)


remove_song_from_artist('Daniel Di Angelo', 'Loyalty')


def calculate_average_rating_for_product_by_name(product_name: str):
    product_ratings = Product.objects.annotate(total_rating=Sum('reviews__rating'),
                                               num_reviews=Count('reviews')
                                               ).get(name=product_name)

    avg_rating = product_ratings.total_rating / product_ratings.num_reviews

    return avg_rating


def get_reviews_with_high_ratings(threshold: int):
    return Review.objects.filter(rating__gte=threshold)


def get_products_with_no_reviews():
    return Product.objects.filter(reviews__isnull=True).order_by('-name')


def delete_products_without_reviews():
    Product.objects.filter(reviews__isnull=True).delete()


def calculate_licenses_expiration_dates():
    driving_licenses = DrivingLicense.objects.all().order_by('-license_number')

    result = []

    for dl in driving_licenses:
        expiration_date = dl.issue_date + timedelta(days=365)

        result.append(
            f'License with id: {dl.license_number} expires on {expiration_date}!'
        )

    return '\n'.join(result)


def get_drivers_with_expired_licenses(due_date):
    expiration_date = due_date - timedelta(days=365)

    drivers_with_expired_license = Driver.objects.filter(drivinglicense__issue_date__gt=expiration_date)

    return drivers_with_expired_license


def register_car_by_owner(owner: Owner):
    registration = Registration.objects.filter(car__isnull=True).first()
    car = Car.objects.filter(registration__isnull=True).first()

    car.owner = owner
    car.registration = registration

    car.save()

    registration.registration_date = date.today()
    registration.car = car

    registration.save()

    return f'Successfully registered {car.model}' \
           f' to {owner.name} with registration number' \
           f' {registration.registration_number}.'










