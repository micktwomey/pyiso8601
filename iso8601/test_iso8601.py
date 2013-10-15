from __future__ import absolute_import

import datetime

import pytest

from iso8601 import iso8601

def test_iso8601_regex():
    assert iso8601.ISO8601_REGEX.match("2006-10-11T00:14:33Z")

def test_timezone_regex():
    assert iso8601.TIMEZONE_REGEX.match("+01:00")
    assert iso8601.TIMEZONE_REGEX.match("+00:00")
    assert iso8601.TIMEZONE_REGEX.match("+01:20")
    assert iso8601.TIMEZONE_REGEX.match("-01:00")

def test_parse_no_timezone_different_default():
    tz = iso8601.FixedOffset(2, 0, "test offset")
    d = iso8601.parse_date("2007-01-01T08:00:00", default_timezone=tz)
    assert d.tzinfo == tz

@pytest.mark.parametrize("invalid_date", [
    ("2013-10-",),
    ("2013-",),
    ("",),
    (None,),
    ("23",),
])

def test_parse_invalid_date(invalid_date):
    with pytest.raises(iso8601.ParseError) as exc:
        iso8601.parse_date(invalid_date)
    assert exc.errisinstance(iso8601.ParseError)

@pytest.mark.parametrize("valid_date,expected_datetime", [
    ("2007-06-23 06:40:34.00Z", datetime.datetime(2007, 6, 23, 6, 40, 34, 0, iso8601.UTC)),  # Handle a separator other than T
    ("1997-07-16T19:20+01:00", datetime.datetime(1997, 7, 16, 19, 20, 0, 0, iso8601.FixedOffset(1, 0, "+01:00"))),  # Parse with no seconds
    ("2007-01-01T08:00:00", datetime.datetime(2007, 1, 1, 8, 0, 0, 0, iso8601.UTC)),  # Handle timezone-less dates. Assumes UTC. http://code.google.com/p/pyiso8601/issues/detail?id=4
    ("2006-10-20T15:34:56.123+02:30", datetime.datetime(2006, 10, 20, 15, 34, 56, 123000, iso8601.FixedOffset(2, 30, "+02:30"))),
    ("2006-10-20T15:34:56Z", datetime.datetime(2006, 10, 20, 15, 34, 56, 0, iso8601.UTC)),
    ("2007-5-7T11:43:55.328Z'", datetime.datetime(2007, 5, 7, 11, 43, 55, 328000, iso8601.UTC)),  # http://code.google.com/p/pyiso8601/issues/detail?id=6
    ("2006-10-20T15:34:56.123Z", datetime.datetime(2006, 10, 20, 15, 34, 56, 123000, iso8601.UTC)),
])

def test_parse_valid_date(valid_date, expected_datetime):
    assert iso8601.parse_date(valid_date) == expected_datetime
