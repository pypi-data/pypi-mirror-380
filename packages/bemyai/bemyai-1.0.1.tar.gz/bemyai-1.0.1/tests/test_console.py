import pytest
from bemyai.__main__ import a_main
from bemyai import BeMyAI


@pytest.mark.parametrize(
    "c_args",
    [
        "bm --help",
        "bm login --help",
        "bm login test@example.com testpassword" "bm signup --help",
        "bm signup Vasya Petrov new@example.com newpassword" "bm recognize --help",
    ],
)
@pytest.mark.asyncio
async def test_main(c_args, monkeypatch):
    async def login(self, email, password):
        assert email == "test@example.com"
        assert password == "testpassword"

    monkeypatch.setattr(BeMyAI, "login", login)

    async def signup(self, first_name, last_name, email, password):
        assert first_name == "Vasya"
        assert last_name == "Petrov"
        assert email == "new@example.com"
        assert password == "newpassword"

    monkeypatch.setattr(BeMyAI, "signup", signup)
    await a_main(args=c_args)
