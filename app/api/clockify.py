from app.core.http_client import HttpClient


def fetch_clockify_data() -> dict:
    """
    Temporary stub for Clockify API.
    Later this function will call the real Clockify endpoints.
    """
    # пример того, как в будущем будем создавать клиента
    # client = HttpClient(base_url="https://api.clockify.me")

    # временные тестовые данные
    return {
        "source": "clockify",
        "status": "ok",
        "message": "Clockify stub response",
        "projects": ["Example project A", "Example project B"],
    }
