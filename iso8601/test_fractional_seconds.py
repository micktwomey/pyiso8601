import datetime
import decimal

import pytest

import iso8601


@pytest.mark.parametrize("fraction, microsecond", [
    ("1", 100000),
    ("000001", 1),
    ("123456789", 123456),
    ("9" * 40, 999999),
    ("000000" + "9" * 40, 0),
])
@pytest.mark.parametrize("precision", [2, 6, 28])
@pytest.mark.parametrize("separator", [".", ","])
def test_fractional_seconds_ignore_decimal_context(
    fraction: str, microsecond: int, precision: int, separator: str
) -> None:
    with decimal.localcontext() as context:
        context.prec = precision
        context.traps[decimal.Inexact] = True
        parsed = iso8601.parse_date("2026-10-08T12:34:56" + separator + fraction + "Z")
    assert parsed == datetime.datetime(2026, 10, 8, 12, 34, 56, microsecond, iso8601.UTC)


def test_long_fraction_does_not_round_up_to_a_second() -> None:
    parsed = iso8601.parse_date("2026-10-08T12:34:56." + "9" * 40 + "Z")
    assert parsed.second == 56
    assert parsed.microsecond == 999999
