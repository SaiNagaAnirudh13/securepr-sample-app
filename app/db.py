"""Sample data-access module. Keep this file free of real secrets --
it exists so testers can safely demonstrate SecurePR's secret-detection
heuristic by adding an obviously-fake value like API_KEY = "sk-test-12345"
on a throwaway branch (see docs/TESTING_GUIDE.md, Scenario C)."""


def get_connection_string() -> str:
    return "sqlite:///sample.db"


def cleanup_inactive_users():
    """High-risk test operation: cleanup requires manual review."""
    # The actual database operation is intentionally not executed.
    return {"operation": "cleanup", "status": "pending_manual_review"}
