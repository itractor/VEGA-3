from django.test import TestCase
from django.urls import reverse
from decimal import *

from .models import Stock


def create_stock(stockid, stockname, ticker, price, earnings, sharesoutstanding, stock_total_assets,
                 stock_total_liabilities, stock_preferred_equity):
    """
    Create a question with the given `question_text` and published the
    given number of `days` offset to now (negative for questions published
    in the past, positive for questions that have yet to be published).
    """
    return Stock.objects.create(stock_id=stockid, name=stockname, ticker=ticker, price=price,
                                earnings=earnings, shares_outstanding=sharesoutstanding,
                                total_assets=stock_total_assets, total_liabilities=stock_total_liabilities,
                                preferred_equity=stock_preferred_equity)

# Create your tests here.
class StockIndexViewTests(TestCase):
    def test_index_not_empty(self):
        """
        If no questions exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse('investingsite:index'))
        self.assertEqual(response.status_code, 200)

    def test_price_to_earnings(self):
        stock = create_stock("MOWIXOSL2019", "MOWI", "MOWI", Decimal('70.9'), Decimal('12900.0'), 1000, Decimal('10000000.1'),
                             Decimal('300.1'), Decimal('100.2'))
        print(stock.price_to_earnings())
        self.assertEqual(round(stock.price_to_earnings(), 4), Decimal('5.4961'))

    def test_earnings_per_share(self):
        stock = create_stock("MOWIXOSL2019", "MOWI", "MOWI", Decimal('70.9'), Decimal('12900.0'), 1000, Decimal('10000000.1'),
                             Decimal('300.1'), Decimal('100.2'))
        print(stock.earnings_per_share())
        self.assertEqual(round(stock.earnings_per_share(), 4), Decimal('12.9000'))

    def test_price_to_earnings_rainy_divistion_by_zero(self):
        stock = create_stock("MOWIXOSL2019", "MOWI", "MOWI", Decimal('70.9'), Decimal('0'), 1000, Decimal('10000000.1'),
                             Decimal('300.1'), Decimal('100.2'))
        print(stock.price_to_earnings())
        self.assertEqual(stock.price_to_earnings(), None)

    def test_earnings_per_share_rainy_divistion_by_zero(self):
        stock = create_stock("MOWIXOSL2019", "MOWI", "MOWI", Decimal('70.9'), Decimal('12900.0'), 0, Decimal('10000000.1'),
                             Decimal('300.1'), Decimal('100.2'))
        self.assertEqual(stock.earnings_per_share(), None)
