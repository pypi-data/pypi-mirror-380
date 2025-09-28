import pytest
import respx
from httpx import Response

from dequest import ConsumerType
from dequest.clients._sync import _perform_request


@respx.mock
def test_perform_request_no_cache():
    expectred_number_of_calls = 4
    api_response = {
        "name": "Alice",
        "grade": 14,
        "city": "New York",
        "birthday": "2000-01-01",
    }
    api = respx.get(
        "https://api.example.com/students/1",
    ).mock(
        return_value=Response(
            json=api_response,
            status_code=200,
        ),
    )

    for _ in range(4):
        response = _perform_request(
            "https://api.example.com/students/1",
            method="GET",
            headers=None,
            json_body=None,
            params=None,
            data=None,
            timeout=30,
            enable_cache=False,
            cache_ttl=None,
            consume=ConsumerType.JSON,
        )

        assert response == api_response

    assert api.call_count == expectred_number_of_calls


@respx.mock
def test_perform_request_cache_enabled():
    expectred_number_of_calls = 1
    api_response = {
        "name": "Alice",
        "grade": 14,
        "city": "New York",
        "birthday": "2000-01-01",
    }
    api = respx.get(
        "https://api.example.com/students/1",
    ).mock(
        return_value=Response(
            json=api_response,
            status_code=200,
        ),
    )

    for _ in range(4):
        response = _perform_request(
            "https://api.example.com/students/1",
            method="GET",
            headers=None,
            json_body=None,
            params=None,
            data=None,
            timeout=30,
            enable_cache=True,
            cache_ttl=None,
            consume=ConsumerType.JSON,
        )

        assert response == api_response

    assert api.call_count == expectred_number_of_calls


@respx.mock
def test_perform_request_post_method():
    expectred_number_of_calls = 4
    api_response = {
        "name": "Alice",
        "grade": 14,
        "city": "New York",
        "birthday": "2000-01-01",
    }
    api = respx.post(
        "https://api.example.com/students/1",
    ).mock(
        return_value=Response(
            json=api_response,
            status_code=200,
        ),
    )

    for _ in range(4):
        response = _perform_request(
            "https://api.example.com/students/1",
            method="POST",
            headers=None,
            json_body=None,
            params=None,
            data=None,
            timeout=30,
            enable_cache=False,
            cache_ttl=None,
            consume=ConsumerType.JSON,
        )

        assert response == api_response

    assert api.call_count == expectred_number_of_calls


@respx.mock
@pytest.mark.parametrize("method", ["POST", "PUT", "DELETE"])
def test_perform_request_not_allowed_methods_with_cache(method):
    expectred_number_of_calls = 0
    api_response = {
        "name": "Alice",
        "grade": 14,
        "city": "New York",
        "birthday": "2000-01-01",
    }
    api = respx.post(
        "https://api.example.com/students/1",
    ).mock(
        return_value=Response(
            json=api_response,
            status_code=200,
        ),
    )

    with pytest.raises(ValueError):
        _perform_request(
            "https://api.example.com/students/1",
            method=method,
            headers=None,
            json_body=None,
            params=None,
            data=None,
            timeout=30,
            enable_cache=False,
            cache_ttl=True,
            consume=ConsumerType.JSON,
        )

    assert api.call_count == expectred_number_of_calls
