import pytest
from tien_ship import tienShip

@pytest.mark.parametrize("a, b, expected", [
    (-1, "no", "Đầu vào không hợp lệ"),
    (3, "no", 12000),
    (8, "no", 20000),
    (11, "no", "Quá quãng đường quy định"),
    (1, "normal", 0),
    (3, "normal", 7000),
    (8, "normal", 15000),
    (15,"normal","Quá quãng đường quy định"),
    (3, "freeship", 0),
    (5, "freeship", 0),
    (9, "freeship", 0),
    (20,"freeship","Quá quãng đường quy định")
])

def test_tien_ship(a, b, expected):
    assert tienShip(a, b) == expected