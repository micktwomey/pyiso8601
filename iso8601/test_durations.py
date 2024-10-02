
import iso8601


def test_example_duration():
    # From https://en.wikipedia.org/wiki/ISO_8601#Durations
    # > For example, "P3Y6M4DT12H30M5S" represents a duration of "three years,
    # > six months, four days, twelve hours, thirty minutes, and five seconds".
    assert iso8601.parse_duration("P3Y6M4DT12H30M5S") == iso8601.Duration(
        years=3, months=6, days=4, hours=12, minutes=30, seconds=5
    )
