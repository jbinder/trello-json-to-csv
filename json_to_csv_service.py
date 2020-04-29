import csv
import json
import re


class JsonToCsvService:
    def __init__(self):
        self.data = None

    def load_from_json(self, file_name):
        with open(file_name, encoding='utf-8') as f:
            self.data = json.load(f)

    def get_cards(self, list_filter, member_filter):
        list_ids = [x['id'] for x in self.data['lists']
                    if not x['closed'] and (list_filter is None or re.search(list_filter, x['name']))]
        member_ids = set([x['id'] for x in self.data['members']
                          if member_filter is None or re.search(member_filter, x['username'])])
        return [x for x in self.data['cards']
                if not x['closed'] and x['idList'] in list_ids and not set(x['idMembers']).isdisjoint(member_ids)]

    def get_property_names(self, property_selector):
        return [x for x in self.data['cards'][0].keys() if re.search(property_selector, x)]

    @staticmethod
    def write_to_file(file_name, cards, property_names):
        with open(file_name, 'w', newline='') as csvFile:
            writer = csv.writer(csvFile)
            for card in cards:
                data = []
                for property_name in property_names:
                    data.append(card[property_name])
                writer.writerow(data)
