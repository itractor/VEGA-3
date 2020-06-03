import random

from django.db import models


class Stock(models.Model):
    random.seed(a=None, version=2)
    stock_id = models.CharField(primary_key=True, max_length=20, default='UNDEFINED')
    name = models.CharField(max_length=100)
    ticker = models.CharField(max_length=10)
    price = models.DecimalField(decimal_places=3, max_digits=100, default=0)
    earnings = models.DecimalField(decimal_places=3, max_digits=100, default=0)
    shares_outstanding = models.BigIntegerField(default=1)
    total_assets = models.DecimalField(decimal_places=3, max_digits=100, default=0)
    total_liabilities = models.DecimalField(decimal_places=3, max_digits=100, default=0)
    preferred_equity = models.DecimalField(decimal_places=3, max_digits=100, default=0)
    currency = models.DecimalField(decimal_places=3, max_digits=100, default=0)

    def __str__(self):
        return self.name

    def price_to_earnings(self):
        try:
            return self.price / Stock.earnings_per_share(self)
        except ZeroDivisionError as err:
            print('Handling run-time error:', err)
            pass

    def earnings_per_share(self):
        try:
            return self.earnings / self.shares_outstanding
        except ZeroDivisionError as err:
            print('Handling run-time error:', err)
            pass

    def price_to_book(self):
        try:
            return self.price / Stock.book_value_per_share(self)
        except ZeroDivisionError as err:
            print('Handling run-time error:', err)
            pass

    def book_value_per_share(self):
        try:
            return Stock.book_value(self) / self.total_liabilities
        except ZeroDivisionError as err:
            print('Handling run-time error:', err)
            pass

    def book_value(self):
        try:
            return self.total_assets - self.total_liabilities - self.preferred_equity
        except ZeroDivisionError as err:
            print('Handling run-time error:', err)
            pass
