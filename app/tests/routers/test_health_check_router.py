import unittest
import pytest

@pytest.mark.usefixtures("client")
class TestHealthCheckRouter(unittest.TestCase):

    def test_health_status(self):
        """Test that health check respond "ok"."""

        rv = self.client.get("/health")

        self.assertEqual(rv.status_code, 200)
        self.assertEqual(rv.json, {"status": "ok"})
