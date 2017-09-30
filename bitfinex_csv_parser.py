import pandas as pd


class BitfinexCSVParser:
    """
    Helper class to read the data from a funding earning csv file exported from bitfinex.
    """

    def parse(self, filepath):
        """
        Parses a funding earning csv file exported from bitfinex.
        :param filepath: The path to the csv file.
        :return: The a list of dataframes. Every dataframe contains the data of one month.
        """
        df_earnings = pd.read_csv(filepath, delimiter=',')
        df_earnings['month'] = df_earnings['Date'].apply(self.__extract_month)
        df_earnings['year'] = df_earnings['Date'].apply(self.__extract_year)
        return df_earnings

    def __extract_year(self, date_string):
        """
        Extracts the year from the date string.
        :param date_string: The date string in the csv file.
        :return: The extracted year as integer.
        """
        year = date_string[0:4]
        return int(year)

    def __extract_month(self, date_string):
        """
        Extracts the month from the date string.
        :param date_string: The date string in the csv file.
        :return: The extracted month as integer.
        """
        month = date_string[5:7]
        return int(month)
