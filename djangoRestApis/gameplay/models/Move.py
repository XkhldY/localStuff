from django.db import models
from .Game import Game


class Move(models.Model):
    x = models.IntegerField()
    y = models.IntegerField()
    comments = models.CharField(max_length=100)
    by_first_player = models.BooleanField()
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
