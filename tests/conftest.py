import pytest
from src.masks import get_mask_card_number
@pytest.fixture()
def data():
    return "11.03.2024"