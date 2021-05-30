from django.db import models


class Stocks(models.Model):
    stock_name = models.CharField(max_length=20)
    date = models.DateTimeField()
    open = models.FloatField()
    close = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    previous_close = models.FloatField()
    volume = models.IntegerField()


class Stks(models.Model):
    stock_name = models.CharField(max_length=20)
