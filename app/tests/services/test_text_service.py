import unittest

from services.text_service import TextService


class TestTextParserResource(unittest.TestCase):

    def test_text_service_returns_correct_count(self):
        """Test that service returns correct count of words requested."""

        service = TextService()
        text = """
        Life is a journey, full of ups and downs.
        It's important to enjoy the good moments and learn from the bad ones.
        """
        count = service.agg_words_count(text)

        self.assertEqual(count[0], ("a", 1))

    def test_text_service_returns_correct_num_of_words(self):
        """Test that service returns number of words requested."""

        service = TextService()
        text = """
        Life is a journey, full of ups and downs.
        It's important to enjoy the good moments and learn from the bad ones.
        """
        num_words = service.agg_words_number(text)

        self.assertEqual(num_words, 22)

    def test_text_service_returns_correct_text_length(self):
        """Test that service returns correct text length requested."""

        service = TextService()
        text = """
        Life is a journey, full of ups and downs.
        It's important to enjoy the good moments and learn from the bad ones.
        """
        full_size, full_size_no_spaces = service.text_length(text)

        self.assertEqual(full_size, len(text))
