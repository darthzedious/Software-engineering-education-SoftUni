import os
import django
from django.db.models import Q, Count, Avg

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Author, Article


# Create queries within functions
def get_authors(search_name=None, search_email=None):

    if search_name is None and search_email is None:
        return ""

    query = Q()
    if search_name is not None:
        query &= Q(full_name__icontains=search_name)
    if search_email is not None:
        query &= Q(email__icontains=search_email)

    authors = Author.objects.filter(
        query
    ).order_by('-full_name')

    if not authors.exists():
        return ""

    return "\n".join(
        f"Author: {a.full_name}, email: {a.email}, status: {'Banned' if a.is_banned else 'Not Banned'}"
        for a in authors
    )


def get_top_publisher():
    articles = Author.objects.get_authors_by_article_count().first()

    if articles is None or articles.number_articles == 0:
        return ""

    return f"Top Author: {articles.full_name} with {articles.number_articles} published articles."


def get_top_reviewer():
    reviews = Author.objects.annotate(
        reviews_number=Count('review')
    ).order_by(
        '-reviews_number',
        'email'
    ).first()

    if reviews is None or reviews.reviews_number == 0:
        return ""

    return f"Top Reviewer: {reviews.full_name} with {reviews.reviews_number} published reviews."


def get_latest_article():
    latest_articles = Article.objects.prefetch_related('authors', 'review_set').order_by('-published_on').first()

    if latest_articles is None:
        return ""

    authors_names = ', '.join(author.full_name for author in latest_articles.authors.all().order_by('full_name'))
    reviews_count = latest_articles.review_set.count()
    avg_rating = sum([r.rating for r in latest_articles.review_set.all()]) / reviews_count if reviews_count else 0.0

    return f"The latest article is: {latest_articles.title}. Authors: {authors_names}. Reviewed: {reviews_count} times." \
           f" Average Rating: {avg_rating:.2f}."


def get_top_rated_article():
    top_rated_article = Article.objects.annotate(avg_rating=Avg('review__rating')) \
        .order_by('-avg_rating', 'title') \
        .first()

    num_reviews = top_rated_article.review_set.count() if top_rated_article else 0
    if top_rated_article is None or num_reviews == 0:
        return ''

    avg_rating = top_rated_article.avg_rating or 0.0
    return f"The top-rated article is: {top_rated_article.title}, with an average rating of {avg_rating:.2f}, " \
           f"reviewed {num_reviews} times."


def ban_author(email=None):
    author = Author.objects.prefetch_related('review_set').filter(email__exact=email).first()
    if email is None or author is None:
        return "No authors banned."

    num_reviews_deleted = author.review_set.count()

    author.is_banned = True
    author.save()
    author.reviews.all().delete()

    return f"Author: {author.full_name} is banned! {num_reviews_deleted} reviews deleted."
