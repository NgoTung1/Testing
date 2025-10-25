import pytest
from tien_ship import tienShip

@pytest.mark.parametrize("a, b, expected", [
    (-1, "no", "Đầu vào không hợp lệ"),
    (11, "no", "Quá quãng đường quy định"),
    (8, "no", 20000),
    (1, "no", 4000),
    (6, "normal", 15000),
    (1, "normal", 0),
    (3, "normal", 7000),
    (3, "abcd", "Đầu vào không hợp lệ"),
    (3, "freeship", 0)
])

def test_tien_ship(a, b, expected):
    assert tienShip(a, b) == expected