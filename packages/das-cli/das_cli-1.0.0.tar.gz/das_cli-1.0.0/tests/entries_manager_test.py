from dotenv import load_dotenv
import unittest
import os

from das.app import Das
from das.common.config import save_api_url
from das.managers.entries_manager import EntryManager

# Load environment variables from .env file
load_dotenv()

class TestEntriesManager(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures before each test method"""        
        self.das_client = Das(base_url=os.getenv("API_URL"))
        self.das_client.authenticate(username=os.getenv("USER_NAME"), password=os.getenv("USER_PASSWORD"))
        self.entry_manager = EntryManager()

    def test_create_entry(self):
        """Test creating an entry"""
        
        entry_data = {
            "Alias": "test.entry.001",
            "Event": "64PE428-02PC",
            "Number": 1,
            "Number Alias": "001",
            "Start Depth": 576,
            "End Depth": 600,
            "Length": 24,
            "Diameter": 12,
            "Storage location":  "OCS-refrigerator4 (core-lab)",
            "Availability": "pc.b.b",
            "Comment": "This is a test entry created by unit test."
        }

        created_entry_id = self.entry_manager.create(attribute="Cores", entry=entry_data)

        self.assertIsNotNone(created_entry_id)
        # assert createrd entry id is an guid
        self.assertRegex(created_entry_id, r'^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$')

    def test_update_entry(self):
        """Test updating an entry"""
        
        updated_entry_data = {
            "Availability": "pc.b.c"
        }

        updated_entry_id = self.entry_manager.update(attribute="Cores", code="zb.b.qdc", entry=updated_entry_data)
        self.assertIsNotNone(updated_entry_id)
        self.assertRegex(updated_entry_id, r'^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$')


    def test_create_entry_with_json_file(self):
        """Test creating an entry from a JSON file"""
        file_path = os.path.join(os.path.dirname(__file__), 'test_data', 'entry_data.json')
        self.entry_manager.create_from_file(attribute="Cores", file_path=file_path)
        # If no exception is raised, the test is considered passed for this example

    def test_create_entry_with_csv_file(self):
        """Test creating an entry from a CSV file"""
        file_path = os.path.join(os.path.dirname(__file__), 'test_data', 'entry_data.csv')
        self.entry_manager.create_from_file(attribute="Cores", file_path=file_path)
        # If no exception is raised, the test is considered passed for this example

    def test_create_entry_with_excel_file(self):
        """Test creating an entry from an Excel file"""
        file_path = os.path.join(os.path.dirname(__file__), 'test_data', 'entry_data.xlsx')
        self.entry_manager.create_from_file(attribute="Cores", file_path=file_path)
        # If no exception is raised, the test is considered passed for this example