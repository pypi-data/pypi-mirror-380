
import unittest
from unittest.mock import patch
from emailverifysdk import EmailVerify, EmailVerifyAPIException, EmailVerifyClientException

class MockResponse:
    def __init__(self, json_data=None, status_code=200):
        self._json_data = json_data
        self.status_code = status_code
    def json(self):
        return self._json_data

class BaseTestCase(unittest.TestCase):
    def setUp(self):
        self.client = EmailVerify("test_api_key")

class EmailVerifyTestCase(BaseTestCase):

    @patch("emailverifysdk.emailverifysdk.requests.Session.request")
    def test_check_balance_valid(self, mock_request):
        mock_request.return_value = MockResponse({
            "api_status": "enabled",
            "remaining_credits": 1000
        }, 200)
        response = self.client.check_balance()
        self.assertEqual(response.api_status, "enabled")
        self.assertEqual(response.remaining_credits, 1000)

    @patch("emailverifysdk.emailverifysdk.requests.Session.request")
    def test_check_balance_error(self, mock_request):
        mock_request.return_value = MockResponse({
            "error": "Invalid API key"
        }, 401)
        with self.assertRaises(EmailVerifyAPIException) as cm:
            self.client.check_balance()
        self.assertIn("Invalid API key", str(cm.exception))

    @patch("emailverifysdk.emailverifysdk.requests.Session.request")
    def test_validate_valid(self, mock_request):
        mock_request.return_value = MockResponse({
            "email": "test@example.com",
            "status": "valid"
        }, 200)
        response = self.client.validate("test@example.com")
        self.assertEqual(response.email, "test@example.com")
        self.assertEqual(response.status, "valid")

    @patch("emailverifysdk.emailverifysdk.requests.Session.request")
    def test_validate_batch_valid(self, mock_request):
        mock_request.return_value = MockResponse({
            "status": "queued",
            "task_id": 123,
            "count_submitted": 2,
            "count_duplicates_removed": 0,
            "count_rejected_emails": 0,
            "count_processing": 2
        }, 200)
        emails = ["a@example.com", "b@example.com"]
        response = self.client.validate_batch(emails, title="Test Batch")
        self.assertEqual(response.status, "queued")
        self.assertEqual(response.task_id, 123)

    @patch("emailverifysdk.emailverifysdk.requests.Session.request")
    def test_validate_batch_error(self, mock_request):
        mock_request.return_value = MockResponse({
            "error": "Batch validation failed"
        }, 400)
        emails = ["a@example.com", "b@example.com"]
        with self.assertRaises(EmailVerifyAPIException) as cm:
            self.client.validate_batch(emails, title="Test Batch")
        self.assertIn("Batch validation failed", str(cm.exception))

    @patch("emailverifysdk.emailverifysdk.requests.Session.request")
    def test_get_batch_result_valid(self, mock_request):
        mock_request.return_value = MockResponse({
            "task_id": 123,
            "status": "verified",
            "count_checked": 2,
            "count_total": 2,
            "results": {
                "email_batch": [
                    {"address": "a@example.com", "status": "valid"},
                    {"address": "b@example.com", "status": "invalid"}
                ]
            }
        }, 200)
        response = self.client.get_batch_result(123)
        self.assertEqual(response.task_id, 123)
        self.assertEqual(response.status, "verified")
        self.assertEqual(response.count_checked, 2)
        self.assertEqual(response.count_total, 2)
        self.assertTrue(hasattr(response, "results"))

    @patch("emailverifysdk.emailverifysdk.requests.Session.request")
    def test_find_email_valid(self, mock_request):
        mock_request.return_value = MockResponse({
            "email": "john.doe@example.com",
            "status": "found"
        }, 200)
        response = self.client.find_email("John Doe", "example.com")
        self.assertEqual(response.email, "john.doe@example.com")
        self.assertEqual(response.status, "found")

    @patch("emailverifysdk.emailverifysdk.requests.Session.request")
    def test_find_email_not_found(self, mock_request):
        mock_request.return_value = MockResponse({
            "email": None,
            "status": "not_found"
        }, 200)
        response = self.client.find_email("Jane Doe", "example.com")
        self.assertIsNone(response.email)
        self.assertEqual(response.status, "not_found")

if __name__ == "__main__":
    unittest.main()
