import importlib.util
import unittest
from pathlib import Path

from fastapi.testclient import TestClient

source = Path(__file__).parents[1] / "src" / "main.py"
spec = importlib.util.spec_from_file_location("deliverypulse", source)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class ReleaseContractTests(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(module.app)

    def test_health_endpoint_identifies_a_healthy_release(self):
        response = self.client.get("/healthz")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["status"], "ok")
        self.assertIn("version", response.json())

    def test_release_card_is_presented_to_reviewers(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("DeliveryPulse", response.text)


if __name__ == "__main__":
    unittest.main()
