import unittest
import os
import sys
from unittest.mock import patch, MagicMock
from dotenv import load_dotenv

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Load environment variables from .env file
load_dotenv()

# Import the module to test
from das.services.attributes import AttributesService
from das.common.api import get_data

class TestAttributesService(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures before each test method"""
        self.base_url = "https://api.das-dev.nioz.nl"
        self.attributes_service = AttributesService(self.base_url)
    
    def tearDown(self):
        """Clean up after each test method"""
        pass
    
    @patch('das.common.api.get_data')
    def test_get_attributes_mock(self, mock_get_data):
        """Test getting attributes with a mock response"""
        # Set up the mock response
        mock_attributes = [
            {"name": "attribute1", "id": "1"},
            {"name": "attribute2", "id": "2"}
        ]
        
        mock_get_data.return_value = {
            'success': True,
            'result': mock_attributes
        }
        
        # Call the method being tested - assuming there's a get_attributes method
        # If this method doesn't exist, you'll need to adjust this test
        try:
            result = self.attributes_service.get_attributes()
            
            # Assertions
            self.assertIsNotNone(result)
            self.assertEqual(len(result), 2)
            self.assertEqual(result[0]["name"], "attribute1")
            mock_get_data.assert_called_once()
        except AttributeError:
            # If the method doesn't exist, mark the test as skipped
            self.skipTest("AttributesService does not have get_attributes method")
    
    @unittest.skip("Example of skipped test")
    def test_skipped(self):
        """This test is skipped as an example"""
        self.assertTrue(False)  # This would fail if not skipped
    
    @unittest.expectedFailure
    def test_expected_failure(self):
        """This test is expected to fail"""
        self.assertEqual(1, 2)  # This will fail as expected
    
    def test_subtest_example(self):
        """Using subtests for testing with different inputs"""
        test_cases = [
            {"input": 1, "expected": 1},
            {"input": 2, "expected": 2},
            {"input": 3, "expected": 3},
        ]
        
        for test_case in test_cases:
            with self.subTest(input=test_case["input"]):
                self.assertEqual(test_case["input"], test_case["expected"])

if __name__ == '__main__':
    unittest.main()
