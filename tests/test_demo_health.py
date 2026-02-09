from myproj.demo.health import ping, ready


def test_ping():
    assert ping() == "pong"


def test_ready():
    assert ready() is True
