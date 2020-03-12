from django.contrib import admin
from .models import Movie, Rating


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    # fields = ['title', 'description']
    list_display = ['title', 'description']
    list_filter = ['title', 'description']
    search_fields = ['title', 'description']


admin.site.register(Rating)
