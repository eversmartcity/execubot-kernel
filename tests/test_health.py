import importlib.util
import unittest


class HealthEndpointTests(unittest.TestCase):
    @unittest.skipIf(importlib.util.find_spec("fastapi") is None, "FastAPI is not installed in this environment")
    def test_health_endpoint(self) -> None:
        from fastapi.testclient import TestClient

        from execubot.api.main import create_app

        client = TestClient(create_app())
        response = client.get("/health")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["status"], "ok")
        self.assertEqual(response.json()["service"], "execubot-api")


if __name__ == "__main__":
    unittest.main()
