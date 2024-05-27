import unittest
from email_sender import send_email
from config import user_email


class TestEmailSender(unittest.TestCase):

    def test_send_email(self):
        success = send_email('example@gmail.com', 'Test Subject', 'Test Content')
        self.assertTrue(success)


if __name__ == '__main__':
    unittest.main()
