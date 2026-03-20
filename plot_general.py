import pandas as pd
import matplotlib.pyplot as plt
import argparse

def main():
    parser = argparse.ArgumentParser(description='Plot a value column over date from a CSV file.')
    parser.add_argument('csv_file', help='Path to the CSV file')
    parser.add_argument('date_column', help='Name of the date column')
    parser.add_argument('value_column', help='Name of the value column to plot')
    parser.add_argument('--output', default='plot.png', help='Output image file (default: plot.png)')
    parser.add_argument('--title', default='Value Over Time', help='Plot title')
    parser.add_argument('--xlabel', default='Date', help='X-axis label')
    parser.add_argument('--ylabel', default='Value', help='Y-axis label')

    args = parser.parse_args()

    # Read the CSV file and parse dates
    df = pd.read_csv(args.csv_file, parse_dates=[args.date_column], date_format=lambda s: pd.to_datetime(s, format='%m/%d/%y'))

    # Sort by date in ascending order so that the plot is chronological
    df = df.sort_values(by=args.date_column)

    # Plot the CSV data
    plt.figure(figsize=(10, 6))
    plt.plot(df[args.date_column], df[args.value_column], marker='o', linestyle='-')
    plt.xlabel(args.xlabel)
    plt.ylabel(args.ylabel)
    plt.title(args.title)
    plt.grid(True)
    plt.gcf().autofmt_xdate(rotation=45)
    plt.tight_layout()


    #save the plot to a PNG file with a customized name
    plt.savefig(args.output)

if __name__ == '__main__':
    main()