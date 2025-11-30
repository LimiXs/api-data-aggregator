# from app.core.http_client import HttpClient
from datetime import datetime


def fetch_clockify_data() -> dict:
    """
    Temporary stub for Clockify API.
    Later this function will call the real Clockify endpoints.
    """
    # пример того, как в будущем будем создавать клиента
    # client = HttpClient(base_url="https://api.clockify.me")

    # временные тестовые данные
    return {
        "workspace_id": 123,
        "dateRangeStart": "2025-01-01T00:00:00Z",
        "dateRangeEnd": datetime.now().isoformat() + "Z",
        "entries": [
            {
                "project": "Example project A",
                "task": "Coding",
                "duration": 3600,
            },
            {
                "project": "Example project B",
                "task": "Review",
                "duration": 1800,
            },
        ],
    }
