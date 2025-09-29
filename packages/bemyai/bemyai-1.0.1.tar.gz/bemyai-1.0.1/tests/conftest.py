import pytest


@pytest.fixture(autouse=True)
def no_requests(monkeypatch):
    """Disable real aiohttp requests  for all tests."""
    monkeypatch.delattr("aiohttp.client.ClientSession")


@pytest.fixture(autouse=True)
def no_dirs(monkeypatch):
    monkeypatch.setattr("os.path.isdir", lambda x: True)
    monkeypatch.setattr("os.mkdir", lambda x: True)
