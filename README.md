# Bitfinex Lending Stats
A simple tool for determining statistics about the earnings made by lending cryptocurrencies on [bitfinex.com](http://bitfinex.com).

## Dependencies
- Python 3
- pandas
- argparse
- (Only for the Webapp) Flask

## Export the Earnings CSV File
Go to [bitfinex.com](http://bitfinex.com) and export the earnings CSV file. It can be exported via "Manage Account" / "Reports" / "Funding Earnings".

## Command Line Tool
To use the command line to show the earnings run

```
python print_lending_stats.py <path_to_csv_file>
```

## Webapp

To start the Webapp run

```
start_webapp.bat
```

on Windows or

```
start_webapp.sh
```

on Linux.

The Webapp should be running on [http://localhost:5000](http://localhost:5000)
