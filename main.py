import argparse

from json_to_csv_service import JsonToCsvService

parser = argparse.ArgumentParser(description='Converts a Trello JSON to CSV.')
parser.add_argument('--i', action="store", required=True, metavar='input_file',
                    help='The input file (Trello JSON).')
parser.add_argument('--o', action="store", required=True, metavar='output_file',
                    help='The output file (CSV).')
parser.add_argument('--field_selector', action="store", default='name', metavar='regex',
                    help='A regex to select all fields of the cards which should be included in the CSV.')
parser.add_argument('--member_filter', action="store", default=None, metavar='regex',
                    help='A regex to select usernames for which cards should be included. '
                         'Optional, including cards of all users if unspecified.')
parser.add_argument('--list_filter', action="store", default=None, metavar='regex',
                    help='A regex to select listnames which for which cards should be included. '
                         'Optional, including cards of all lists if unspecified.')
args = parser.parse_args()


service = JsonToCsvService()
service.load_from_json(args.i)
cards = service.get_cards(args.list_filter, args.member_filter)
field_names = service.get_field_names(args.field_selector)
service.write_to_file(args.o, cards, field_names)
