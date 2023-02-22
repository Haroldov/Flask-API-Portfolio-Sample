import unittest

from services.text_service import TextService

class TestTextParserResource(unittest.TestCase):

    def test_text_service_returns_correct_method(self):
        """Test that service returns correct method requested."""

        service = TextService()
        text = """
        Life is a journey, full of ups and downs.
        It's important to enjoy the good moments and learn from the bad ones.
        """
        count = service.parse_text(text, method="count")
        num_words = service.parse_text(text, method="length")
        full_size = service.parse_text(text, method="full_length")

        self.assertEqual(count[0], ("a", 1))
        self.assertEqual(num_words, 22)
        self.assertEqual(full_size, len(text))

