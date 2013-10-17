Simple module to parse ISO 8601 dates

This module parses the most common forms of ISO 8601 date strings (e.g.
2007-01-14T20:34:22+00:00) into datetime objects.

>>> import iso8601
>>> iso8601.parse_date("2007-01-25T12:00:00Z")
datetime.datetime(2007, 1, 25, 12, 0, tzinfo=<iso8601.iso8601.Utc ...>)
>>>

See the LICENSE file for the license this package is released under.

If you want more full featured parsing look at:

- http://labix.org/python-dateutil - python-dateutil

Homepage
========

* https://bitbucket.org/micktwomey/pyiso8601/

This was originally hosted at https://code.google.com/p/pyiso8601/

References
==========

* http://www.cl.cam.ac.uk/~mgk25/iso-time.html - simple overview

* http://hydracen.com/dx/iso8601.htm - more detailed enumeration of valid formats.

Testing
=======

1. pip install -r dev-requirements.txt
2. tox

Note that you need all the pythons installed to perform a tox run (see below). Homebrew helps a lot on the mac.

Alternatively, to test only with your current python:

1. pip install -r dev-requirements.txt
2. py.test --verbose iso8601

Supported Python Versions
=========================

Tested against:

- Python 2.6
- Python 2.7
- Python 3.2
- Python 3.3
- PyPy

Python 3.0 and 3.1 are untested but should work.

Jython is untested but should work.

Python 2.5 is not supported (too old).

Changes
=======

0.1.5
-----

* Wow, it's alive! First update since 2007
* Moved over to https://bitbucket.org/micktwomey/pyiso8601
* Add support for python 3. https://code.google.com/p/pyiso8601/issues/detail?id=23 (thanks to zefciu)
* Switched to py.test and tox for testing
* Make seconds optional in date format ("1997-07-16T19:20+01:00" now valid). https://bitbucket.org/micktwomey/pyiso8601/pull-request/1/make-the-inclusion-of-seconds-optional-in/diff (thanks to Chris Down)
* Correctly raise ParseError for more invalid inputs (https://bitbucket.org/micktwomey/pyiso8601/issue/1/raise-parseerror-for-invalid-input) (thanks to manish.tomar)
* Support more variations of ISO 8601 dates, times and time zone specs.
* Fix microsecond rounding issues (https://bitbucket.org/micktwomey/pyiso8601/issue/2/roundoff-issues-when-parsing-decimal) (thanks to nielsenb@jetfuse.net)
* Fix pickling and deepcopy of returned datetime objects (https://bitbucket.org/micktwomey/pyiso8601/issue/3/dates-returned-by-parse_date-do-not) (thanks to fogathmann and john@openlearning.com)
* Fix timezone offsets without a separator (https://bitbucket.org/micktwomey/pyiso8601/issue/4/support-offsets-without-a-separator) (thanks to joe.walton.gglcd)

0.1.4
-----

* The default_timezone argument wasn't being passed through correctly, UTC was being used in every case. Fixes issue 10.

0.1.3
-----

* Fixed the microsecond handling, the generated microsecond values were way too small. Fixes issue 9.

0.1.2
-----

* Adding ParseError to __all__ in iso8601 module, allows people to import it. Addresses issue 7.
* Be a little more flexible when dealing with dates without leading zeroes. This violates the spec a little, but handles more dates as seen in the field. Addresses issue 6.
* Allow date/time separators other than T.

0.1.1
-----

* When parsing dates without a timezone the specified default is used. If no default is specified then UTC is used. Addresses issue 4.
