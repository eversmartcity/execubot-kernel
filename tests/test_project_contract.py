from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class ProjectContractTests(unittest.TestCase):
    def test_expected_skeleton_files_exist(self) -> None:
        expected = [
            "pyproject.toml",
            "alembic.ini",
            "execubot/api/main.py",
            "execubot/api/schemas.py",
            "execubot/api/routes/audit.py",
            "execubot/api/routes/memory.py",
            "execubot/api/routes/tasks.py",
            "execubot/core/config.py",
            "execubot/core/database.py",
            "execubot/core/models.py",
            "execubot/migrations/env.py",
            "execubot/migrations/versions/20260617_0001_initial_tables.py",
        ]

        missing = [path for path in expected if not (ROOT / path).exists()]

        self.assertEqual(missing, [])

    def test_initial_model_tables_are_declared(self) -> None:
        model_source = (ROOT / "execubot/core/models.py").read_text(encoding="utf-8")

        for table_name in ["audit_events", "memory_items", "tasks", "approvals"]:
            self.assertIn(f'__tablename__ = "{table_name}"', model_source)

    def test_no_deferred_integrations_added(self) -> None:
        pyproject = (ROOT / "pyproject.toml").read_text(encoding="utf-8").lower()

        for excluded in ["celery", "temporal", "redis", "discord", "telegram"]:
            self.assertNotIn(excluded, pyproject)


if __name__ == "__main__":
    unittest.main()
