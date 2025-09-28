import pytest

from citation_date import uk_pattern, us_pattern


@pytest.mark.parametrize(
    "us_date",
    [
        "April 29 2001 ",
        "April 29, 2001",
        "April, 29, 2001",
        "April. 29, 2001",
        "April     29,   2001",
        "April29, 2001",
        "April292001",
        "April29,2001",
        "April.29,2001",
    ],
)
def test_pass_us_date(us_date):
    assert us_pattern.search(us_date)


@pytest.mark.parametrize(
    "us_date",
    [
        "Dec/29/2001 ",
        "Dec/292001",
    ],
)
def test_fail_us_date(us_date):
    assert not us_pattern.search(us_date)


@pytest.mark.parametrize(
    "uk_date",
    [
        "29April 2001 ",
        "29,April  2001",
        "29, April, 2001",
        "29, April. 2001",
        "29,   , April2001",
        "29April2001",
        "29,April2001",
        "29 April 2001 ",
        "29.April2001",
        "29.April.2001",
    ],
)
def test_pass_uk_date(uk_date):
    assert uk_pattern.search(uk_date)
