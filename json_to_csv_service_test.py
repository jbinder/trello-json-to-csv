import os
import unittest

from json_to_csv_service import JsonToCsvService


class JsonToCsvServiceTest(unittest.TestCase):
    def test_load_should_not_throw_exception(self):
        service = self._get_loaded_service()
        self.assertEqual(len(service.get_cards(None, None)), 1)

    def test_get_cards_valid_list_filter_should_return_cards(self):
        service = self._get_loaded_service()
        cards = service.get_cards("l*", None)
        self.assertEqual(len(cards), 1)

    def test_get_cards_invalid_list_filter_should_not_return_cards(self):
        service = self._get_loaded_service()
        cards = service.get_cards("k1", None)
        self.assertEqual(len(cards), 0)

    def test_get_cards_valid_member_filter_should_return_cards(self):
        service = self._get_loaded_service()
        cards = service.get_cards(None, "u*")
        self.assertEqual(len(cards), 1)

    def test_get_cards_invalid_member_filter_should_not_return_cards(self):
        service = self._get_loaded_service()
        cards = service.get_cards(None, "u2")
        self.assertEqual(len(cards), 0)

    def test_get_cards_valid_list_and_member_filter_should_return_cards(self):
        service = self._get_loaded_service()
        cards = service.get_cards("l*", "u*")
        self.assertEqual(len(cards), 1)

    def test_get_property_names_valid_filter_should_return_names(self):
        service = self._get_loaded_service()
        properties = service.get_property_names("name")
        self.assertEqual(len(properties), 1)

    def test_get_property_names_invalid_filter_should_not_return_names(self):
        service = self._get_loaded_service()
        properties = service.get_property_names("doesntexist")
        self.assertEqual(len(properties), 0)

    def test_save_should_write_nonempty_csv(self):
        service = self._get_loaded_service()
        cards = service.get_cards(None, None)
        keys = service.get_property_names("name")
        file_name = "test.csv"
        service.write_to_file(file_name, cards, keys)
        self.assertTrue(os.stat(file_name).st_size > 0)
        os.remove(file_name)

    @staticmethod
    def _get_loaded_service():
        service = JsonToCsvService()
        service.load_from_json("test.json")
        return service

