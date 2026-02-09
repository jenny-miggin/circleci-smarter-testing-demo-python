# Optional fixtures / config for tests (e.g. shared setup).
# Previously used TEST_DEMO_SLOWDOWN for a long-running demo; now using 200+ tests instead.

import os

import pytest


@pytest.fixture(autouse=True)
def _junit_classname_as_file_path(request, record_xml_attribute):
    """
    Set JUnit classname to the test file path (e.g. tests/test_math.py) so CircleCI
    Smarter Testing can match timing data to our test atoms (discover returns file paths).
    """
    try:
        path = request.node.fspath
        # Prefer path relative to repo root (match discover: find ./tests -type f -name 'test*.py')
        try:
            rel = os.path.relpath(path, request.config.rootpath)
            rel = rel.replace("\\", "/")
            if not rel.startswith("./"):
                rel = "./" + rel
        except Exception:
            rel = str(path).replace("\\", "/")
        record_xml_attribute("classname", rel)
    except Exception:
        pass
