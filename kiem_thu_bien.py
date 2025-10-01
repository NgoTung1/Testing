import pytest
from tien_ship import tienShip

@pytest.mark.parametrize("a, b, expected", [
    (0.1,"normal", 0),
    (0.2,"normal",0),
    (3, "normal",7000),
    (4.8,"normal",14200),
    (4.9, "normal",14600),
    (5,"normal",15000),
    (5.1,"normal",15000),
    (8,"normal",15000),
    (9,"normal",15000),
    (10,"normal",15000)
])
def test_tien_ship_bien(a, b, expected):
    assert tienShip(a, b) == expected

