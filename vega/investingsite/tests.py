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
        stock = create_stock("MOWIXOSL2019", "MOWI", "MOWI", Decimal('70.9'), Decimal('12900.0'), 1000)
        print(stock.pricetoearnings())
        self.assertEqual(round(stock.pricetoearnings(), 4), Decimal('5.4961'))

    def test_earnings_per_share(self):
        stock = create_stock("MOWIXOSL2019", "MOWI", "MOWI", Decimal('70.9'), Decimal('12900.0'), 1000)
        print(stock.earnings_per_share())
        self.assertEqual(round(stock.earnings_per_share(), 4), Decimal('12.9000'))

    def test_price_to_earnings_rainy(self):
        stock = create_stock("MOWIXOSL2019", "MOWI", "MOWI", Decimal('70.9'), Decimal('0'), 1000)
        print(stock.pricetoearnings())
        self.assertEqual(stock.pricetoearnings(), None)

    def test_earnings_per_share_rainy(self):
        stock = create_stock("MOWIXOSL2019", "MOWI", "MOWI", Decimal('70.9'), Decimal('12900.0'), 0)
        self.assertEqual(stock.earnings_per_share(), None)
