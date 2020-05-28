from django.test import TestCase
from django.urls import reverse
from decimal import *

from .models import Stock


def create_stock(stockid, stockname, ticker, price, earnings, sharesoutstanding):
    """
    Create a question with the given `question_text` and published the
    given number of `days` offset to now (negative for questions published
    in the past, positive for questions that have yet to be published).
    """
    return Stock.objects.create(stock_id=stockid, stock_name=stockname, stock_ticker=ticker, stock_price=price,
                                stock_earnings=earnings, stock_shares_outstanding=sharesoutstanding)


# Create your tests here.
class StockIndexViewTests(TestCase):
    def test_index_not_empty(self):
        """
        If no questions exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse('investingsite:index'))
        self.assertEqual(response.status_code, 200)

    def test_price_to_earnings(self):
        """
        If no questions exist, an appropriate message is displayed.
        """
        stock = create_stock("MOWIXOSL2019", "MOWI", "MOWI", Decimal('70.9'), Decimal('12900.0'), 1000)
        print(stock.pricetoearnings())
        self.assertEqual(stock.pricetoearnings(), 100000000)