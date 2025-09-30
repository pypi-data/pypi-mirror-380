"""
Test module for file_utils.py
"""
import unittest
import os
import json
import csv
import tempfile
from pathlib import Path
from das.common.file_utils import (
    load_json_file,
    load_csv_file,
    load_excel_file,
    parse_data_string,
    load_file_based_on_extension
)

class TestFileUtils(unittest.TestCase):
    """Test case for file_utils module."""
    
    def setUp(self):
        """Set up test environment."""
        self.temp_dir = tempfile.TemporaryDirectory()
        
    def tearDown(self):
        """Tear down test environment."""
        self.temp_dir.cleanup()
        
    def test_load_json_file(self):
        """Test loading JSON file."""
        # Create a temporary JSON file
        test_data = {"Name": "Test Entry", "Description": "Test Description", "Grant Public Access": True}
        json_path = Path(self.temp_dir.name) / "test.json"
        
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(test_data, f)
        
        # Test loading the file
        result = load_json_file(str(json_path))
        self.assertEqual(result, test_data)
        
    def test_load_csv_file(self):
        """Test loading CSV file."""
        # Create a temporary CSV file
        csv_path = Path(self.temp_dir.name) / "test.csv"
        
        with open(csv_path, 'w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["Name", "Description", "Grant Public Access"])
            writer.writerow(["Test Entry", "Test Description", "Yes"])
            
        # Test loading the file
        result = load_csv_file(str(csv_path))
        self.assertEqual(result["Name"], "Test Entry")
        self.assertEqual(result["Description"], "Test Description")
        self.assertEqual(result["Grant Public Access"], "Yes")
        
    def test_load_excel_file(self):
        """Test loading Excel file."""
        try:
            import pandas as pd
            
            # Create a temporary Excel file
            excel_path = Path(self.temp_dir.name) / "test.xlsx"
            
            # Create a pandas DataFrame and save as Excel
            df = pd.DataFrame({
                "Name": ["Test Entry"],
                "Description": ["Test Description"],
                "Grant Public Access": ["Yes"]
            })
            
            df.to_excel(excel_path, index=False)
            
            # Test loading the file
            result = load_excel_file(str(excel_path))
            self.assertEqual(result["Name"], "Test Entry")
            self.assertEqual(result["Description"], "Test Description")
            self.assertEqual(result["Grant Public Access"], "Yes")
        except ImportError:
            self.skipTest("pandas not installed, skipping Excel test")
        
    def test_parse_data_string(self):
        """Test parsing data string."""
        # Test with different formats
        data_string = "{ 'Name': 'Test Entry', 'Description': 'Test Description', 'Grant Public Access': Yes }"
        result = parse_data_string(data_string)
        
        self.assertEqual(result["Name"], "Test Entry")
        self.assertEqual(result["Description"], "Test Description")
        self.assertEqual(result["Grant Public Access"], True)
        
    def test_load_file_based_on_extension(self):
        """Test loading files based on extension."""
        # Create a temporary JSON file
        test_data = {"Name": "Test Entry", "Description": "Test Description", "Grant Public Access": True}
        json_path = Path(self.temp_dir.name) / "test.json"
        
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(test_data, f)
        
        # Test loading the JSON file
        result = load_file_based_on_extension(str(json_path))
        self.assertEqual(result, test_data)
        
        # Test with unsupported file type
        unsupported_path = Path(self.temp_dir.name) / "test.txt"
        with open(unsupported_path, 'w', encoding='utf-8') as f:
            f.write("Test data")
            
        with self.assertRaises(ValueError):
            load_file_based_on_extension(str(unsupported_path))

if __name__ == '__main__':
    unittest.main()