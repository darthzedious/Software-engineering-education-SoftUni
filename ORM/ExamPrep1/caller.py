import os
import django
from django.db.models import Q, Count, Avg, F

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Director, Actor, Movie


# Create queries within functions


def get_directors(search_name=None, search_nationality=None):
    if search_name is None and search_nationality is None:
        return ""

    query = Q()

    if search_name is not None:
        query &= Q(full_name__icontains=search_name)
    if search_nationality is not None:
        query &= Q(nationality__icontains=search_nationality)

    directors = Director.objects.filter(
        query
    ).order_by(
        'full_name'
    )

    return "\n".join(f"Director: {d.full_name}, nationality: {d.nationality}, experience: {d.years_of_experience}"
                     for d in directors)


def get_top_director():
    director = Director.objects.get_directors_by_movies_count().first()

    if director is None:
        return ""

    return f"Top Director: {director.full_name}, movies: {director.movie_number}."


def get_top_actor():
    actor = Actor.objects.annotate(
        num_of_movies=Count('movie'),
        movies_avg_rating=Avg('movie__rating')) \
        .order_by('-num_of_movies', 'full_name') \
        .first()

    if not actor or not actor.num_of_movies:
        return ""

    movies = ", ".join(movie.title for movie in actor.movie.all() if movie)

    return f"Top Actor: {actor.full_name}, starring in movies: {movies}, " \
           f"movies average rating: {actor.movies_avg_rating:.1f}"


def get_actors_by_movies_count():
    actors = Actor.objects.prefetch_related('movie_actors').annotate(
        movie_number=Count('movie_actors')
    ).order_by('-movie_number', 'full_name')[:3]

    if not actors or not actors[0].movie_number:
        return ""

    return '\n'.join(f"{x.full_name}, participated in {x.movie_number} movies"
                     for x in actors)


def get_top_rated_awarded_movie():
    movie = Movie.objects.select_related(
        'starring_actor'
    ).prefetch_related(
        'actors'
    ).filter(
        is_awarded=True
    ).order_by(
        '-rating',
        'title'
    ).first()

    if movie is None:
        return ""

    cast = [x.full_name for x in movie.actors.all().order_by('full_name')]

    return f"Top rated awarded movie: {movie.title},"\
           f" rating: {movie.rating:.1f}."\
           f" Starring actor: {movie.starring_actor.full_name if movie.starring_actor else 'N/A'}."\
           f" Cast: {', '.join(cast)}."


def increase_rating():
    updated_movies = Movie.objects.filter(is_classic=True, rating__lt=10.0)

    if not updated_movies:
        return "No ratings increased."

    num_of_updated_movies = updated_movies.update(rating=F('rating') + 0.1)

    return f"Rating increased for {num_of_updated_movies} movies."

