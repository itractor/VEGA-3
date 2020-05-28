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
    stock_price = models.DecimalField(decimal_places=3, max_digits=100, default=0)
    stock_earnings = models.DecimalField(decimal_places=3, max_digits=100, default=0)
    stock_shares_outstanding = models.BigIntegerField(default=1)

    def __str__(self):
        return self.stock_name

    def pricetoearnings(self):
        try:
            return self.stock_price / Stock.earnings_per_share(self)
        except ZeroDivisionError as err:
            print('Handling run-time error:', err)
            pass

    def earnings_per_share(self):
        try:
            return self.stock_earnings / self.stock_shares_outstanding
        except ZeroDivisionError as err:
            print('Handling run-time error:', err)
            pass
