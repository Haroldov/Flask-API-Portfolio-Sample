import unittest
import pytest


@pytest.mark.usefixtures("client")
class TestTextParserRouter(unittest.TestCase):

    def test_text_router_words_count(self):
        """Test that words counter respond "ok"."""

        rv = self.client.post(
            "/word-count", json={"text": "HELLO WORLD"},
        )

        self.assertEqual(rv.status_code, 200)


    def test_text_router_words_count_400(self):
        """Test that words counter respond bad request."""

        rv = self.client.post(
            "/word-count", json={"texts": "HELLO WORLD"},
        )

        self.assertEqual(rv.status_code, 400)

    def test_text_router_words_number(self):
        """Test that words number respond "ok"."""

        rv = self.client.post(
            "/word-quantity", json={"text": "HELLO WORLD"},
        )

        self.assertEqual(rv.status_code, 200)

    def test_text_router_text_length(self):
        """Test that text_length respond "ok"."""

        rv = self.client.post(
            "/full-text-length", json={"text": "HELLO WORLD"},
        )

        self.assertEqual(rv.status_code, 200)
