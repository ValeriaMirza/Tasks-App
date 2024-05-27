import unittest
from config import SENDGRID_API_KEY, AAI_SETTINGS_API_KEY, server, user_email

class TestConfig(unittest.TestCase):
    def test_sendgrid_api_key(self):
        self.assertIsNotNone(SENDGRID_API_KEY)

    def test_aai_settings_api_key(self):
        self.assertIsNotNone(AAI_SETTINGS_API_KEY)

    def test_server(self):
        self.assertIsNotNone(server)

    def test_user_email(self):
        self.assertIsNotNone(user_email)

if __name__ == '__main__':
    unittest.main()
