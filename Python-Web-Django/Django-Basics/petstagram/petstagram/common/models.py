from django.db import models

# Create your models here.
from petstagram.photos.models import Photos


class Comment(models.Model):
    text = models.TextField(
        max_length=300,
    )

    date_time_of_publication = models.DateTimeField(
        auto_now_add=True,
    )

    to_photo = models.ForeignKey(
        to=Photos,
        on_delete=models.CASCADE,
    )


class Like(models.Model):
    to_photo = models.ForeignKey(
        to=Photos,
        on_delete=models.CASCADE,
    )