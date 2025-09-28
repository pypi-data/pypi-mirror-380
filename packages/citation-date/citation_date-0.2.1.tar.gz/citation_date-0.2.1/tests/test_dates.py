import pytest

from citation_date import dates_pattern, decode_date


@pytest.mark.parametrize(
    "raw_text, group_name, group_capture",
    [
        ("The date is April 29 2001 ", "naked_date", "April 29 2001"),
        ("The date is (april29,2001)", "parents_date", "april29,2001"),
        ("The date is [april, 29 2001]", "brackets_date", "april, 29 2001"),
    ],
)
def test_pass_date(raw_text, group_name, group_capture):
    match = dates_pattern.search(raw_text)
    assert match and match.group(group_name) == group_capture
    assert decode_date(group_capture) == "April 29, 2001"
