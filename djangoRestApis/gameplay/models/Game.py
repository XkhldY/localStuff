from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q


class GamesQuerySet(models.QuerySet):
    def games_for_user(self, user):
        return self.filter(Q(first_player=user) | Q(second_player=user))

    def active(self):
        return self.filter(Q(status='F') | Q(status='S'))


class Game(models.Model):
    first_player = models.ForeignKey(User, related_name='games_first_player', on_delete=models.CASCADE)
    second_player = models.ForeignKey(User, related_name='games_second_player', on_delete=models.CASCADE)
    start_time = models.DateTimeField(auto_now_add=True)
    last_active = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=1, default='F')
    objects = GamesQuerySet.as_manager()

    def __str__(self):
        return self.first_player.__str__() + ' vs ' + self.second_player.__str__()
