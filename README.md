## General CSV Plotter

`plot_general.py`: A general script to plot any value column over a date column from any CSV file.

### Usage

Run with command-line arguments:

```
python plot_general.py <csv_file> <date_column> <value_column> [--output <output_file>] [--title <title>] [--xlabel <xlabel>] [--ylabel <ylabel>]
```

Example for powerHistory.csv:

```
python plot_general.py powerHistory.csv Date "Yield(Wh)" --output yield_plot.png --title "Power Yield Over Time" --ylabel "Yield (Wh)"
```

### Arguments

- `csv_file`: Path to the CSV file
- `date_column`: Name of the date column (must be parseable as dates)
- `value_column`: Name of the numeric column to plot
- `--output`: Output image file (default: plot.png)
- `--title`: Plot title (default: "Value Over Time")
- `--xlabel`: X-axis label (default: "Date")
- `--ylabel`: Y-axis label (default: "Value")

## Troubleshooting

- If you get import errors, make sure `pandas` and `matplotlib` are installed.
- The script assumes the CSV has the specified columns.
- Dates should be in a format that pandas can parse (e.g., MM/DD/YY). If not, you may need to specify a date format in the code.
