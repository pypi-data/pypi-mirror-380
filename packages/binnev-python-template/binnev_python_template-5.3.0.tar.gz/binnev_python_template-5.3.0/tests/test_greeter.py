import pytest

from src.core.greeter import greeting


@pytest.mark.parametrize(
    ["name", "expected_greeting"],
    [
        ("", "Hello, world!"),
        ("Johnny", "Hello, Johnny!"),
    ],
)
def test_greeting(name: str, expected_greeting: str) -> None:
    assert greeting(name) == expected_greeting
