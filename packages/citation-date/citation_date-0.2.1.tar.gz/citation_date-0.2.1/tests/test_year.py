import pytest

from citation_date import year_pattern


@pytest.mark.parametrize(
    "year",
    [1900, 1999, 2021, 2030, 2100, 2299],
)
def test_pass_year(year):
    assert year_pattern.fullmatch(str(year))


@pytest.mark.parametrize(
    "item",
    [
        1800,
        1850,
        1899,
        2300,
        2900,
        "2001-2002",
        "2001-2",
        "2000a",
        "a2000",
        ",2000",
        "2000,",
    ],
)
def test_fail_day(item):
    assert not year_pattern.fullmatch(str(item))
