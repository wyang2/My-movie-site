from django.contrib import admin

# Register your models here.
from .models import Movie, themeSong

admin.site.register(Movie)
admin.site.register(themeSong)