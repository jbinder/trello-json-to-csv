import argparse

from json_to_csv_service import JsonToCsvService

parser = argparse.ArgumentParser(description='Converts a Trello JSON to CSV.')
parser.add_argument('--i', action="store", required=True,
                    help='The input file (Trello JSON).')
parser.add_argument('--o', action="store", required=True,
                    help='The output file (CSV).')
parser.add_argument('--property_selector', action="store", default='name',
                    help='A regex to select all properties of the cards which should be included in the CSV.')
parser.add_argument('--member_filter', action="store", default=None,
                    help='A regex to select usernames for which cards should be included. '
                         'Optional, including cards of all users if unspecified.')
parser.add_argument('--list_filter', action="store", default=None,
                    help='A regex to select listnames which for which cards should be included. '
                         'Optional, including cards of all lists if unspecified.')
args = parser.parse_args()


service = JsonToCsvService()
service.load_from_json(args.i)
cards = service.get_cards(args.list_filter, args.member_filter)
property_names = service.get_property_names(args.property_selector)
service.write_to_file(args.o, cards, property_names)
