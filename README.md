# trello-json-to-csv

Extract data from Trello JSON exports to CSV.

Features:

* Filter cards by members and lists.
* Select which card fields to include.

## Requirements

* Python 3.6

## Usage

    usage: main.py [-h] --i input_file --o output_file [--field_selector regex]
                   [--member_filter regex] [--list_filter regex]

    Converts a Trello JSON to CSV.

    optional arguments:
      -h, --help            show this help message and exit
      --i input_file        The input file (Trello JSON).
      --o output_file       The output file (CSV).
      --field_selector regex
                            A regex to select all fields of the cards which should
                            be included in the CSV.
      --member_filter regex
                            A regex to select usernames for which cards should be
                            included. Optional, including cards of all users if
                            unspecified.
      --list_filter regex   A regex to select listnames which for which cards
                            should be included. Optional, including cards of all
                            lists if unspecified.
