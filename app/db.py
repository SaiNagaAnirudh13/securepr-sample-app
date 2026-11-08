"""Sample data-access module. Keep this file free of real secrets --
it exists so testers can safely demonstrate SecurePR's secret-detection
heuristic by adding an obviously-fake value like API_KEY = "sk-test-12345"
on a throwaway branch (see docs/TESTING_GUIDE.md, Scenario C)."""


def get_connection_string() -> str:
    return "sqlite:///sample.db"


def get_user_status(user_id: int) -> dict:
    """Return the status information for a user.

    This is a sample implementation used to demonstrate how application
    code can be affected by a database schema change.
    """
    return {
        "user_id": user_id,
        "status": "active",
    }
