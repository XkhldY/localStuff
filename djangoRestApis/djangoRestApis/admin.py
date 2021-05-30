from django.contrib import admin
from gameplay.models import Game, Move
from .models import Book

admin.site.register(Game)
admin.site.register(Move)
admin.site.register(Book)
