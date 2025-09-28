import pytest

from citation_date import day_pattern


@pytest.mark.parametrize("count", [1, 5, "03", 30, 31])
def test_pass_day(count):
    assert day_pattern.fullmatch(str(count))


@pytest.mark.parametrize(
    "item",
    ["1-", "1/", "4.", 32, 98, "32a, 1b", "0", "3420 ", " 124 ", "31x", "21a"],
)
def test_fail_day(item):
    assert not day_pattern.fullmatch(str(item))
