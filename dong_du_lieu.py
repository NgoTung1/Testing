import pytest
from tien_ship import tienShip

@pytest.mark.parametrize("a, b, expected", [
    # Test case của Biến a
    (-1,"normal", "Đầu vào không hợp lệ" ),
    (12,"no","Quá quãng đường quy định"),
    (11, "no","Quá quãng đường quy định"),
    (5,"anca","Đầu vào không hợp lệ"),
    (3, "no",12000),
    (7,"no",20000),
    (1,"normal",0),
    (8,"normal",15000),
    (3,"no",12000),
    (7,"normal",15000),
    (4,"normal",11000),
    # Test case của biến b
    (8.5,"no",20000),
    (2,"freeship",0),
    (9,"normal",15000),
    (8,"monad","Đầu vào không hợp lệ"),
    (9.9,"freeship",0),
    (5,"abcd","Đầu vào không hợp lệ"),
    # Test case của biến c
    (7.5,"no",20000),
    (2.5,"no",10000)
])
def test_tien_ship(a, b, expected):
    assert tienShip(a, b) == expected

