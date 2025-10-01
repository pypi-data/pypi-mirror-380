
import os
import sys
import unittest
from dotenv import load_dotenv

from das.app import Das

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

load_dotenv()

class TestEntries(unittest.TestCase):
    def setUp(self):
        self.das_client = Das(base_url="https://api.das-dev.nioz.nl")
        self.das_client.authenticate(username=os.getenv("USER_NAME"), password=os.getenv("USER_PASSWORD"))

    def test_get_entry_by_code(self):
        entry_code = "zb.b.tcc"
        entry = self.das_client.entries.get_entry(code=entry_code)
        self.assertIsNotNone(entry)
        self.assertEqual(entry.get('entry', {}).get('code'), entry_code)

    def test_search_entries(self):
        search_params = {
            "attributeId": "55",            
            "queryString": "*64*",
            "maxResultCount": 5,
            "skipCount": 0
        }
        results = self.das_client.search.search_entries(**search_params)
        self.assertIsNotNone(results)
        self.assertIn('items', results)
        self.assertGreater(len(results['items']), 0)    

if __name__ == '__main__':
    unittest.main()