from pathlib import Path
import tempfile
import unittest

from execubot.core.config import load_settings


class ConfigTests(unittest.TestCase):
    def test_loads_defaults_without_env_file(self) -> None:
        settings = load_settings(env_file="does-not-exist.env")

        self.assertEqual(settings.app_name, "ExecuBot Kernel")
        self.assertEqual(settings.service_name, "execubot-api")
        self.assertEqual(settings.environment, "development")
        self.assertIn("postgresql+psycopg://", settings.database_url)

    def test_loads_values_from_env_file(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            env_file = Path(tmp) / ".env"
            env_file.write_text(
                "\n".join(
                    [
                        "EXECUBOT_APP_NAME=Local Bot",
                        "EXECUBOT_SERVICE_NAME=execubot-test",
                        "EXECUBOT_ENV=test",
                        "DATABASE_URL=postgresql+psycopg://user:pass@db:5432/test",
                    ]
                ),
                encoding="utf-8",
            )

            settings = load_settings(env_file=env_file)

        self.assertEqual(settings.app_name, "Local Bot")
        self.assertEqual(settings.service_name, "execubot-test")
        self.assertEqual(settings.environment, "test")
        self.assertEqual(settings.database_url, "postgresql+psycopg://user:pass@db:5432/test")


if __name__ == "__main__":
    unittest.main()
