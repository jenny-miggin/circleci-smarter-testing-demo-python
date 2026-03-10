def ping() -> str:
    """Return a liveness probe string.

    Intended for use by health-check endpoints to confirm the service is
    reachable and responsive.

    Returns:
        The string ``"pong"``.
    """
    return "pong"


def ready() -> bool:
    """Return the readiness status of the service.

    Intended for use by readiness-check endpoints to signal that the service
    has finished initialising and is able to handle requests.

    Returns:
        ``True`` unconditionally, indicating the service is ready.
    """
    return True
