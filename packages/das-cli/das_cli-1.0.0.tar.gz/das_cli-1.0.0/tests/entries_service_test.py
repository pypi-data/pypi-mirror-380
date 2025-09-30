import unittest
import os
from unittest.mock import patch, MagicMock
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Import the module to test
from das.services.entries import EntriesService

class TestEntriesService(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures before each test method"""
        self.base_url = "https://api.das-dev.nioz.nl"
        self.entries_service = EntriesService(self.base_url)
    
    def tearDown(self):
        """Clean up after each test method"""
        pass
    
    @patch('das.services.entries.get_data')
    def test_get_entry_mock(self, mock_get_data):
        """Test getting an entry with a mock response"""
        # Set up the mock response
        entry_code = "zb.b.tcc"
        mock_result = {
            'entry': {
                'code': entry_code,
                'name': 'Test Entry'
            }
        }
        mock_get_data.return_value = {
            'success': True,
            'result': mock_result
        }
        
        # Call the method being tested
        result = self.entries_service.get_entry(code=entry_code)
        
        # Assertions
        self.assertIsNotNone(result)
        self.assertEqual(result['entry']['code'], entry_code)
        mock_get_data.assert_called_once()
    
    @unittest.skipIf(not os.getenv("USER_NAME") or not os.getenv("USER_PASSWORD"), 
                    "Skipping integration test because credentials are not set")
    def test_real_api_connection(self):
        """Integration test with real API (requires credentials)"""
        # This test will be skipped if USER_NAME or USER_PASSWORD environment variables are not set
        from das.app import Das
        
        das_client = Das(base_url=self.base_url)
        das_client.authenticate(username=os.getenv("USER_NAME"), password=os.getenv("USER_PASSWORD"))
        
        # Test the real API
        entry_code = "zb.b.tcc"
        entry = das_client.entries.get_entry(code=entry_code)
        self.assertIsNotNone(entry)
        self.assertEqual(entry.get('entry', {}).get('code'), entry_code)
    
    def test_sample_assertion_methods(self):
        """Demonstrate various assertion methods in unittest"""
        # Basic assertions
        self.assertEqual(1+1, 2)
        self.assertNotEqual(1+1, 3)
        self.assertTrue(True)
        self.assertFalse(False)
        self.assertIs(True, True)
        self.assertIsNot(True, False)
        
        # Type checks
        self.assertIsInstance(1, int)
        self.assertIsInstance("test", str)
        
        # Container checks
        self.assertIn("a", ["a", "b", "c"])
        self.assertNotIn("d", ["a", "b", "c"])
        
        # Exception checks
        with self.assertRaises(ValueError):
            int("not a number")


if __name__ == '__main__':
    unittest.main()
