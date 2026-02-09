from myproj.lib.math import add
from myproj.utils.validation import is_email


def handle_sum(body: dict) -> dict:
    a = body.get("a", 0)
    b = body.get("b", 0)
    return {"result": add(int(a), int(b))}


def handle_validate_email(body: dict) -> dict:
    email = body.get("email", "")
    return {"valid": is_email(str(email))}
