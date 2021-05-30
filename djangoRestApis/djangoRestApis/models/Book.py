from django.db import models


class Book (models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    read = models.BooleanField()

    def __str__(self):
        return self.title + ' by ' + self.author
