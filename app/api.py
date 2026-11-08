"""A tiny Flask-style sample API used to demonstrate SecurePR's impact simulator."""


from app.db import get_user_status


def get_status():
    return {
        "status": "ok",
        "service": "securepr-sample-app",
        "version": "1.0",
    }


def get_service_info():
    """Return basic service information for API consumers."""
    return {
        "name": "SecurePR Sample App",
        "environment": "test",
        "healthy": True,
    }


"""A tiny Flask-style sample API used to demonstrate SecurePR's impact simulator."""


def get_status():
    return {"status": "ok"}


def get_account_status(user_id: int):
    """Return account status information for an API consumer."""
    return get_user_status(user_id)
