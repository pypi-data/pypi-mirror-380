import pytest

from citation_date import month_pattern


@pytest.mark.parametrize(
    "month_name",
    [
        "Jan",
        "jan",
        "Jan",
        "January",
        "feb",
        "Feb",
        "February",
        "Mar",
        "March",
        "Apr",
        "April",
        "May",
        "Jun",
        "June",
        "Jul",
        "July",
        "July",
        "Aug",
        "August",
        "Sep",
        "Sept",
        "September",
        "Oct",
        "October",
        "Nov",
        "November",
        "Dec",
        "December",
    ],
)
def test_pass_month(month_name):
    assert month_pattern.fullmatch(month_name)


@pytest.mark.parametrize(
    "item",
    ["Ja", "Febr."],
)
def test_fail_day(item):
    assert not month_pattern.fullmatch(item)
