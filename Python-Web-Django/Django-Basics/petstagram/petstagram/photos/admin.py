# Register your models here.
from django.contrib import admin
from petstagram.photos.models import Photo


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'date_of_publication', 'description', 'get_added_pets')

    @staticmethod
    def get_added_pets(obj):
        return ', '.join(str(pet) for pet in obj.tagged_pets.all())
