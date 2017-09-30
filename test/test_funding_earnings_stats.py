import unittest
from funding_earnings_stats import FundingEarningsCalculator

class FundingEarningsCalculatorTest(unittest.TestCase):

    def setUp(self):
        self.calcuator = FundingEarningsCalculator(filepath='earnings_test_file.csv')


    def test_get_currencies(self):
        currencies = self.calcuator.get_currencies()
        assert (len(currencies) == 2)
        assert ('BTC' in currencies)
        assert ('LTC' in currencies)

    def test_monthly_earnings(self):
        earnings = self.calcuator.get_monthly_earnings()
        assert (earnings['All Time']['LTC'] == earnings['2017-8']['LTC'] + earnings['2017-9']['LTC'])
        assert (earnings['2017-9']['BTC'] == 0.072395352 + 0.07395352)
        assert (earnings['2017-8']['BTC'] == 0.0395352)

    def test_get_currency_stats(self):
        stats = self.calcuator.get_currency_stats()
        assert (len(stats) == len(self.calcuator.get_currencies()))
        assert (stats['LTC']['All Time']['Min Amount'] == 0.01329358)
        assert (stats['BTC']['All Time']['Min Amount'] == 0.0395352)
        assert (stats['BTC']['2017-8']['Cumulative Amount'] == 0.0395352)
        assert (stats['BTC']['All Time']['Max Amount'] == 0.07395352)
        assert (stats['BTC']['All Time']['Cumulative Amount'] == 0.18588407199999998)
        assert (stats['BTC']['2017-9']['Number of Payments'] == 2)


if __name__ == '__main__':
    unittest.main()