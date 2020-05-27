import datetime
import random
from operator import __floordiv__

from django.db import models

# Create your models here.
from django.db.models import F
from django.utils import timezone


class Stock(models.Model):
    random.seed(a=None, version=2)
    stock_id = models.CharField(primary_key=True, max_length=20, default='UNDEFINED')
    stock_name = models.CharField(max_length=100)
    stock_ticker = models.CharField(max_length=10)
    stock_price = models.DecimalField(decimal_places=3, max_digits=10, default=0)
    stock_earnings = models.DecimalField(decimal_places=3, max_digits=10, default=0)

    def __str__(self):
        return self.stock_name

    def pricetoearnings(self):

        return self.stock_price / self.stock_earnings
