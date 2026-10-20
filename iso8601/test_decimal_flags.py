import datetime
import decimal

import pytest

import iso8601


@pytest.mark.parametrize("preexisting_flag", [False, True])
def test_fractional_parse_preserves_decimal_flags(preexisting_flag: bool) -> None:
    with decimal.localcontext() as context:
        context.prec = 6
        context.rounding = decimal.ROUND_DOWN
        context.traps[decimal.Inexact] = False
        context.traps[decimal.Rounded] = False
        context.clear_flags()
        context.flags[decimal.DivisionByZero] = preexisting_flag
        before = context.flags.copy()

        parsed = iso8601.parse_date("2026-10-08T12:34:56.123456789Z")

        assert parsed == datetime.datetime(2026, 10, 8, 12, 34, 56, 123456, iso8601.UTC)
        assert context.flags == before
