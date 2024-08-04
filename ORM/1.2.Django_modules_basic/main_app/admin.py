from django.contrib import admin
from main_app.models import Book
# Register your models here.
# superuser angel password angel


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass
