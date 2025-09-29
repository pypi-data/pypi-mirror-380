import pytest
from bemyai import BeMyAI


@pytest.fixture
def signup_response_success():
    return {
        "email_verification_required": True,
        "password_change_required": False,
        "token": "e100b146aa5451cef0e52dc7304eef018bdaf97ec68b27ff203ff75722c18703",
        "user": {
            "auth_type": "email",
            "country": "RU",
            "created_at": "2024-02-03T07:35:30.473790Z",
            "email": "test@example.com",
            "extra": {},
            "first_name": "Vasya",
            "has_accepted_latest_terms": True,
            "has_accepted_marketing": None,
            "has_hidden_email": False,
            "has_usable_password": True,
            "id": 8128031,
            "is_pending_deletion": False,
            "last_name": "Petrov",
            "primary_language": "",
            "secondary_languages": [],
            "timezone": "Asia/Shanghai",
            "uid": "c344f1db-cedd-4e93-af26-69f10dac676f",
            "user_type": "bvi",
        },
    }


@pytest.fixture
def bm_without_account():
    return BeMyAI()


@pytest.mark.asyncio
async def test_signup(bm_without_account, signup_response_success, monkeypatch):
    async def mock_request_signup_success(*args, **kwargs):
        assert "+08:00" in kwargs["json"]["terms_accepted_at"]
        assert kwargs["json"]["timezone"] == "Asia/Shanghai"
        assert kwargs["json"]["user_type"] == "bvi"
        return signup_response_success

    monkeypatch.setattr(BeMyAI, "request", mock_request_signup_success)
    result = await bm_without_account.signup(
        "Vasya", "Petrov", "test@example.com", "testpassword"
    )
    assert result.user.first_name == "Vasya"
    assert len(result.token) > 5
