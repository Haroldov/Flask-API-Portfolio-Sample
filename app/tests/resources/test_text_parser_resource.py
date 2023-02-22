import unittest

from resources.text_parser_resource import TextResource

class TestTextParserResource(unittest.TestCase):

    def test_simple_paragraph_is_well_parsed(self):
        """Test that a simple paragraph is well parsed."""

        text = """
        Life is a journey, full of ups and downs.
        It's important to enjoy the good moments and learn from the bad ones.
        """
        expected_parse = [
            "life","is", "a", "journey", "full", "of", "ups", "and", "downs",
            "it's", "important", "to", "enjoy", "the", "good", "moments", "and",
            "learn", "from", "the", "bad", "ones"
        ]

        r = TextResource(text)
        self.assertEqual(r.text, expected_parse)


    def test_simple_paragraph_count_is_correct(self):
        """Test that a simple paragraph is well parsed and count is correct."""

        text = """
        1 Life is a journey, full of ups and downs.
        It's important to enjoy the good moments and learn from the bad ones. 1
        """
        r = TextResource(text)
        self.assertEqual(r.compute_count_and_sort()[0], ("1", 2))


    def test_non_english_words_filtered(self):
        """Test that a simple paragraph is well parsed and count is correct."""

        text = """
        Life is a journey, full of ups and downs.
        It's HALLO important to enjoy the good moments and learn from the bad ones.
        """
        expected_parse = [
            "life","is", "a", "journey", "full", "of", "ups", "and", "downs",
            "it's", "important", "to", "enjoy", "the", "good", "moments", "and",
            "learn", "from", "the", "bad", "ones"
        ]

        r = TextResource(text)
        self.assertEqual(r.text, expected_parse)
