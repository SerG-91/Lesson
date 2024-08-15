from typing import Any

import pytest

from src.generators import card_number_generator


@pytest.mark.parametrize(
    "start, stop, end",
    [
        ("95", "96", "0000 0000 0000 0095"),
        ("0", "1", "0000 0000 0000 0000"),
        ("9999999999999999", "9999999999999999", "9999 9999 9999 9999"),
    ],
)
def test_card_number_generator(start: str, stop: str, end: str) -> Any:
    """Тест функции маскировки счета"""
    numer = card_number_generator(int(start), int(stop))
    assert next(numer) == end
