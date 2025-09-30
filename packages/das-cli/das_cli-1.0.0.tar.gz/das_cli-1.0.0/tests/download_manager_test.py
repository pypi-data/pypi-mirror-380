from dotenv import load_dotenv
import unittest
import os

from das.app import Das
from das.common.config import save_api_url
from das.managers.entries_manager import EntryManager

# Load environment variables from .env file
load_dotenv()

class TestDownloadManager(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures before each test method"""        
        self.das_client = Das(base_url=os.getenv("API_URL"))
        self.das_client.authenticate(username=os.getenv("USER_NAME"), password=os.getenv("USER_PASSWORD"))

    def test_create_download_request(self):
        """Test creating a download request"""
        from das.managers.download_manager import DownloadManager

        download_manager = DownloadManager()  

        request_data = {
            'name': 'Test Download Request',
            'zb.b.dc': ['h.b.z0pg', 'h.b.s3pg'],
            'zb.b.lu': []
        }      

        download_request_id = download_manager.create_download_request(request_data)

        self.assertIsNotNone(download_request_id)
        # assert created download request id is a guid
        self.assertRegex(download_request_id, r'^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$')