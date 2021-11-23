import datetime

import iso8601

d = iso8601.parse_date("2007-01-25T12:00:00Z")
print(d)
assert d == datetime.datetime(2007, 1, 25, 12, 0, tzinfo=iso8601.UTC)
