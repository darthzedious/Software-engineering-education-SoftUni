from django.db import models

# # Create your models here.
# class User(models.Model):
#     username = models.CharField(
#         max_length=100,
#         unique=True,
#     )
#
#     password = models.CharField(
#         max_length=100,
#     )
#
#     email = models.EmailField(
#         max_length=100,
#         unique=True,
#     )
#
#     last_login = models.DateTimeField(
#         null=True,
#         blank=True,
#     )
#
#     def __str__(self):
#         return self.username