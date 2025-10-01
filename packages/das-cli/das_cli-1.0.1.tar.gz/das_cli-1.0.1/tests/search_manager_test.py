
import os
import sys
import unittest
from dotenv import load_dotenv
from das.app import Das
from das.managers.search_manager import SearchManager
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
load_dotenv()

class TestSearchManager(unittest.TestCase):
    def setUp(self):
        self.das_client = Das(base_url="https://api.das-dev.nioz.nl")
        self.das_client.authenticate(username=os.getenv("USER_NAME"), password=os.getenv("USER_PASSWORD"))

    def test_search_manager(self):
        search_manager = SearchManager()
        results = search_manager.search_entries(attribute="Cores", query="name(*64*)", max_results=5, page=1, sort_by="Name", sort_order="asc")
        self.assertIsInstance(results, dict)
        self.assertIn('items', results)
        self.assertGreater(len(results['items']), 0)

if __name__ == '__main__':
    unittest.main()
