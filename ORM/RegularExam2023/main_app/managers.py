from django.db import models
from django.db.models import Count


class AuthorManager(models.Manager):

    def get_authors_by_article_count(self):
        return self.annotate(
            number_articles=Count('article')
        ).order_by(
            '-number_articles',
            'email'
        )
