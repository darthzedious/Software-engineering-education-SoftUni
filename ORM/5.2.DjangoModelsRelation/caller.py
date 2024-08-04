import os
from datetime import timedelta, date

import django
from django.db.models import Avg

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Author, Book, Artist, Song, Product, Review, Driver, DrivingLicense, Owner, Car, Registration


# Create queries within functions


def show_all_authors_with_their_books():
    authors_with_books = []

    authors = Author.objects.all().order_by("id")

    for author in authors:
        books = Book.objects.filter(author=author)
        #books = author.book_set.all()

        if not books:
            continue

        titles = ", ".join(b.title for b in books)

        authors_with_books.append(f"{author.name} has written - {titles}!")

    return "\n".join(authors_with_books)


def delete_all_authors_without_books():
    Author.objects.filter(book__isnull=True).delete()


def add_song_to_artist(artist_name: str, song_title: str):
    artist = Artist.objects.get(name=artist_name)
    song = Song.objects.get(title=song_title)

    artist.songs.add(song)
    #Artist.objects.get(name=artist_name).songs.add(Song.objects.get(title=song_title))


def get_songs_by_artist(artist_name: str):
    return Artist.objects.get(name=artist_name).songs.all().order_by("-id")



def remove_song_from_artist(artist_name: str, song_title: str):
    Artist.objects.get(name=artist_name).songs.remove(Song.objects.get(title=song_title))


def calculate_average_rating_for_product_by_name(product_name: str):
    # product = Product.objects.get(name=product_name)
    # reviews = product.reviews.all()
    #
    # total_rating = sum(r.rating for r in reviews)  # 5 + 1 => 6
    # average_rating = total_rating / len(reviews)  # 6 / 2 => 3
    #
    # return average_rating

    product = Product.objects.annotate(average_rating=Avg('reviews__rating'),).get(name=product_name)

    return product.average_rating


def get_reviews_with_high_ratings(threshold: int):
    return Review.objects.filter(rating__gte=threshold)


def get_products_with_no_reviews():
    return Product.objects.filter(reviews__isnull=True).order_by('-name')


def delete_products_without_reviews():
    Product.objects.filter(reviews__isnull=True).delete()
    #get_products_with_no_reviews().delete()


def calculate_licenses_expiration_dates() -> str:
    licenses = DrivingLicense.objects.order_by('-license_number')

    return "\n".join(str(l) for l in licenses)


def get_drivers_with_expired_licenses(due_date: date) -> str:
    expiration_cutoff_date = due_date - timedelta(days=365)

    drivers_with_expired_licenses = Driver.objects.filter(
        license__issue_date__gt=expiration_cutoff_date,
    )

    return drivers_with_expired_licenses


def register_car_by_owner(owner: Owner) -> str:
    registration = Registration.objects.filter(car__isnull=True).first()
    car = Car.objects.filter(registration__isnull=True).first()

    car.owner = owner

    car.save()

    registration.registration_date = date.today()
    registration.car = car

    registration.save()

    return f"Successfully registered {car.model} to {owner.name} with registration number {registration.registration_number}."
