from django.db import models


# Create your models here.
class SampleModel(models.Model):
    x = models.CharField(max_length=10)


class Company(models.Model):
    companyName = models.CharField(max_length=200, default='', name='companyName')
    symbol = models.CharField(max_length=20)

    def __str__(self):
        return self.companyName


class Stock(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    date = models.DateTimeField(name='Date')
    open = models.FloatField()
    close = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    previous_close = models.FloatField(name='prev close')
    volume = models.IntegerField(name='volume')

    # def __str__(self):
    #     return self.company.name
    #
    # def __repr__(self):
    #     return self.company.name



