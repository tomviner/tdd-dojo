import pytest

from roman import to_roman

TEST_PAIRS = (
    (1, 'I'),
    (5, 'V'),
    # (10, 'X'),
    # (50, 'L'),
    # (100, 'C'),

    # (2, 'II'),
    # (3, 'III'),

    # (4, 'IV'),
    # (24, 'XXIV'),
    # (93, 'XCIII'),
    # (173, 'CLXXIII'),
)


@pytest.mark.parametrize('num,roman', TEST_PAIRS)
def test_roman(num, roman):
    assert to_roman(num) == roman
