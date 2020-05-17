import datetime
import random

from django.db import models

# Create your models here.
from django.utils import timezone


class Stock(models.Model):
    random.seed(a=None, version=2)
    stock_id = models.CharField(primary_key=True, max_length=100, default='UNDEFINED')
    stock_name = models.CharField(max_length=100)
    stock_ticker = models.CharField(max_length=10)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.stock_name

