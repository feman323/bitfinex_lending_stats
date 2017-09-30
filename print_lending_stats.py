import argparse
from funding_earnings_stats import FundingEarningsCalculator

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("funding_earnings_file", help="The path to the bitfinex funding earnings csv file.")
args = arg_parser.parse_args()

csv_parser = FundingEarningsCalculator(args.funding_earnings_file)
currencies = csv_parser.get_currencies()

print("Found earnings for {} currencies in file {} ".format(len(currencies), args.funding_earnings_file))
currency_stats = csv_parser.get_currency_stats()
for currency in currencies:
    print("Earnings for {}".format(currency))
    print()
    print(currency_stats[currency])
    print()
    print()
print()
print("---------------------")
print()

monthly_earnings = csv_parser.get_monthly_earnings()
print("Monthly Earnings")
print()
print(csv_parser.get_monthly_earnings())

# TODO Monthly earnings sum col, Testing with multiple months
# TODO FundingEarningsCalculator so umstrukturieren, dass parsen ausgelagert ist


