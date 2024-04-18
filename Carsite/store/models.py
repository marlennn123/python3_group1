from django.db import models


class Car(models.Model):
    category = models.CharField(max_length=20)
    marka = models.CharField(max_length=16)
    model = models.CharField(max_length=32)
    price = models.PositiveIntegerField(default=0)
    year = models.SmallIntegerField(max_length=16)
    mileage = models.PositiveIntegerField(max_length=32)
    city = models.CharField(max_length=15)
    country = models.CharField(max_length=20)
    with_photo = models.BooleanField()
    color = models.CharField(max_length=30)
    volume = models.DecimalField(max_digits=6, decimal_places=3)
    DESCRIPTION = models.TextField()

    def __str__(self):
        return f'{self.category} | {self.marka}'

class Bet(models.Model):
    number = models.IntegerField()
    total_number = models.IntegerField()
    buy_now = models.IntegerField()
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

    def __int__(self):
        return self.number