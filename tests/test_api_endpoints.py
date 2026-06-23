from __future__ import annotations

import importlib.util
import unittest


FASTAPI_AVAILABLE = importlib.util.find_spec("fastapi") is not None
SQLALCHEMY_AVAILABLE = importlib.util.find_spec("sqlalchemy") is not None


@unittest.skipUnless(FASTAPI_AVAILABLE and SQLALCHEMY_AVAILABLE, "FastAPI and SQLAlchemy are required for API endpoint tests")
class ApiEndpointTests(unittest.TestCase):
    def setUp(self) -> None:
        from sqlalchemy import create_engine
        from sqlalchemy.orm import sessionmaker
        from sqlalchemy.pool import StaticPool

        from execubot.api.main import create_app
        from execubot.core.database import Base, get_session

        self.engine = create_engine(
            "sqlite+pysqlite:///:memory:",
            connect_args={"check_same_thread": False},
            poolclass=StaticPool,
        )
        self.SessionTesting = sessionmaker(bind=self.engine, autoflush=False, autocommit=False)
        Base.metadata.create_all(bind=self.engine)

        def override_get_session():
            session = self.SessionTesting()
            try:
                yield session
            finally:
                session.close()

        app = create_app()
        app.dependency_overrides[get_session] = override_get_session

        from fastapi.testclient import TestClient

        self.client = TestClient(app)

    def tearDown(self) -> None:
        from execubot.core.database import Base

        Base.metadata.drop_all(bind=self.engine)

    def test_create_and_get_task(self) -> None:
        create_response = self.client.post(
            "/tasks",
            json={
                "source": "api-test",
                "goal": "Create the first task",
                "assigned_agent": "execubot",
                "correlation_id": "test-task-1",
            },
        )

        self.assertEqual(create_response.status_code, 201)
        created = create_response.json()
        self.assertEqual(created["status"], "created")
        self.assertEqual(created["goal"], "Create the first task")

        get_response = self.client.get(f"/tasks/{created['id']}")

        self.assertEqual(get_response.status_code, 200)
        self.assertEqual(get_response.json()["id"], created["id"])

    def test_get_missing_task_returns_404(self) -> None:
        response = self.client.get("/tasks/00000000-0000-0000-0000-000000000000")

        self.assertEqual(response.status_code, 404)

    def test_create_and_list_audit_events(self) -> None:
        response = self.client.post(
            "/audit/events",
            json={
                "event_type": "task.created",
                "actor": "api-test",
                "payload": {"task": "example"},
            },
        )

        self.assertEqual(response.status_code, 201)
        created = response.json()
        self.assertEqual(created["event_type"], "task.created")
        self.assertEqual(created["payload"], {"task": "example"})

        list_response = self.client.get("/audit/events")

        self.assertEqual(list_response.status_code, 200)
        events = list_response.json()
        self.assertEqual(len(events), 1)
        self.assertEqual(events[0]["id"], created["id"])

    def test_create_and_list_memory_items(self) -> None:
        response = self.client.post(
            "/memory/items",
            json={
                "scope": "project",
                "key": "architecture",
                "content": "ExecuBot uses FastAPI and PostgreSQL.",
                "metadata": {"source": "test"},
            },
        )

        self.assertEqual(response.status_code, 201)
        created = response.json()
        self.assertEqual(created["scope"], "project")
        self.assertEqual(created["metadata"], {"source": "test"})

        list_response = self.client.get("/memory/items?scope=project")

        self.assertEqual(list_response.status_code, 200)
        items = list_response.json()
        self.assertEqual(len(items), 1)
        self.assertEqual(items[0]["id"], created["id"])


if __name__ == "__main__":
    unittest.main()
