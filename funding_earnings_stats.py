import pandas as pd
from bitfinex_csv_parser import BitfinexCSVParser


class FundingEarningsCalculator:
    """
    Helper class to determine the bitfinex funding earnings.
    """

    def __init__(self, filepath=None):
        """
        Constructor.
        :param filepath: The path to the bitfinex earnings csv file.
        """
        self.df_earnings = BitfinexCSVParser().parse(filepath)

    def get_currencies(self):
        """
        Returns the currencies contained in the data.
        :return: The currencies contained in the data.
        """
        return self.df_earnings['Currency'].unique()

    def get_currency_stats(self):
        """
        Returns a dictionary of dataframes. The key is the name of the currency. The value is a dataframe that
        contains statistical information about the currency.
        :return:  A list of dataframe. Every dataframe contains the data of one currency.
        """
        currencies = self.get_currencies()
        months = self.df_earnings['month'].unique()
        years = self.df_earnings['year'].unique()
        currency_stats_dict = {}
        for currency in currencies:
            df_currency_stats = pd.DataFrame()
            cum_amount = 'Cumulative Amount'
            min_amount = 'Min Amount'
            max_amount = 'Max Amount'
            num_pay = 'Number of Payments'
            for year in years:
                for month in months:
                    df_currency = self.df_earnings
                    df_currency = df_currency[((df_currency['Currency'] == currency) & (df_currency['year'] == year)) &
                                              (df_currency['month'] == month)]
                    stats = {
                        cum_amount: df_currency['Amount'].sum(),
                        min_amount: df_currency['Amount'].min(),
                        max_amount: df_currency['Amount'].max(),
                        num_pay: len(df_currency)
                    }
                    df_currency_stats.insert(0, str(year) + "-" + str(month), pd.Series(stats))

            alltime_stats = {
                min_amount: df_currency_stats.loc[[min_amount], :].min(axis=1)[0],
                max_amount: df_currency_stats.loc[[max_amount], :].max(axis=1)[0],
                cum_amount: df_currency_stats.loc[[cum_amount], :].sum(axis=1)[0],
                num_pay: df_currency_stats.loc[[num_pay], :].sum(axis=1)[0]
            }
            df_currency_stats.insert(0, "All Time", pd.Series(alltime_stats))
            currency_stats_dict[currency] = df_currency_stats
        return currency_stats_dict

    def get_monthly_earnings(self):
        """
        Creates a dataframe that contains the sum of the earnings per currency in every month.
        :return: The dataframe.
        """
        currencies = self.get_currencies()
        years = self.df_earnings['year'].unique()
        df_result = pd.DataFrame()
        for year in years:
            df_year = self.df_earnings[self.df_earnings['year'] == year]
            months = df_year['month'].unique()
            for month in months:
                df_month = df_year[df_year['month'] == month]
                sums = {}
                for currency in currencies:
                    sums[currency] = df_month[df_month['Currency'] == currency]['Amount'].sum()
                df_result.insert(0, str(year) + "-" + str(month), pd.Series(sums))

        df_result.insert(0, "All Time", df_result.sum(axis=1))
        return df_result
