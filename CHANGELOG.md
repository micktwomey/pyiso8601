# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]
### Changed
- Drop support for Python3.8
- Switch completely to [just](https://just.systems/) for development tasts, remove nox. Rely on Github actions matrix of python versions for testing across all supported python versions.
- Remove black, rely on ruff for formatting.

## [2.1.0] - 2023-10-03
### Fixed
- Use ruff for linting
- Fixed CHANGELOG version links

### Added
- Add readthedocs configuration

## [2.0.0] - 2023-06-09
### Added
- Add just for development commands
- Add Python 3.12 support

### Changed
- Move changelog into [CHANGELOG.md](CHANGELOG.md)
- Freshen up README

### Fixed
- Fix test_fixedoffset_eq by adding an actual assertion

### Removed
- Drop Python 3.6 support (3.6 is end of life)

## [1.1.0] - 2022-09-28
### Added
- Add `is_iso8601` function for validating that a string matches an ISO 8601 format (thanks to David Baumgold (https://github.com/singingwolfboy) for https://github.com/micktwomey/pyiso8601/pull/21)
- Add Python 3.11 to the test mix

## [1.0.2] - 2021-11-23
### Added
- Add missing `__all__` in `__init__.py`. Addresses https://github.com/micktwomey/pyiso8601/issues/17 (thanks to Alex Gaynor for reporting)

## [1.0.1] - 2021-11-22
### Added
- Add missing py.typed file (as per PEP 561), keeps mypy happy :D

## [1.0.0] - 2021-11-07
### Added
- Add type annotations to code

### Changed
- Switch to poetry for packaging
- Simplify internals and remove old compatability code
- Switch to nox for testing
- Lots of small project development changes

### Removed
- Remove external type annotations in pyi
- Drop python < 3.6 support

## [0.1.16] - 2021-07-16
### Added
- Include `docs/` into sdist tarball (thanks to kloczek in https://github.com/micktwomey/pyiso8601/issues/14)

## [0.1.15] - 2021-07-16
### Added
- Include .pyi files in built wheels and source tarballs

## [0.1.14] - 2021-02-05
### Added
- Add GitHub build actions for project
- Add project URLs in setup.py (thanks to Steve Piercy)
- Add Python 3.9 to test matrix (thanks to Luciano Mammino)
- Add type hints (thanks to Brett Cannon)

### Changed
- Update README links (thanks to Steve Piercy)
- Derive `ParseError` from `ValueError` (thanks to Lex Robinson)

### Fixed
- Fix handling of README in setup.py (encoding fun in 3.5, 3.6 and pypy3)
- Fix README links (thanks to Chris Barker)

## [0.1.13] - 2020-09-11
### Added
- Add python 3.7 and 3.8 to tests

### Changed
- Move to GitHub (https://github.com/micktwomey/pyiso8601). Thanks go to Martin Häcker for pointing out the bitbucket project had been deleted by Atlassian!

### Removed
- Remove python 2.6, 3.2, 3.3 and 3.4 from tests

## [0.1.12] - 2017-07-27
### Fixed
- Fix class reference for iso8601.Utc in module docstring (thanks to felixschwarz in https://bitbucket.org/micktwomey/pyiso8601/pull-requests/7/fix-class-reference-for-iso8601utc-in/diff)

## [0.1.11] - 2015-11-03
### Added
- Add support for , as separator for fractional part (thanks to ecksun in https://bitbucket.org/micktwomey/pyiso8601/pull-requests/5/add-support-for-as-separator-for/diff)
- Add Python 3.4 and 3.5 to tox test config.
- Add PyPy 3 to tox test config.
- Link to documentation at https://pyiso8601.readthedocs.org/

### Removed
- Remove logging (thanks to Quentin Pradet in https://bitbucket.org/micktwomey/pyiso8601/pull-requests/6/remove-debug-logging/diff)

## [0.1.10] - 2014-02-27
### Added
- Adds YYYY as a valid date (uses 1 for both month and day)
- Woo, semantic versioning, .10 at last.

### Fixed
- Fixes https://bitbucket.org/micktwomey/pyiso8601/issue/14/regression-yyyy-mm-no-longer-parses (thanks to Kevin Gill for reporting)

## [0.1.9] - 2014-02-26
### Fixed
- Lots of fixes tightening up parsing from jdanjou. In particular more invalid cases are treated as errors. Also includes fixes for tests (which is how these invalid cases got in in the first place).
- Release addresses https://bitbucket.org/micktwomey/pyiso8601/issue/13/new-release-based-on-critical-bug-fix

## [0.1.8] - 2013-10-22
### Fixed
- Remove +/- chars from README.rst and ensure tox tests run using LC_ALL=C. The setup.py egg_info command was failing in python 3.* on some setups (basically any where the system encoding wasn't UTF-8). (https://bitbucket.org/micktwomey/pyiso8601/issue/10/setuppy-broken-for-python-33) (thanks to klmitch)

## [0.1.7] - 2013-10-19
### Fixed
- Fix parsing of microseconds (https://bitbucket.org/micktwomey/pyiso8601/issue/9/regression-parsing-microseconds) (Thanks to dims and bnemec)

## [0.1.6] - 2013-10-18
### Fixed
- Correct negative timezone offsets (https://bitbucket.org/micktwomey/pyiso8601/issue/8/015-parses-negative-timezones-incorrectly) (thanks to Jonathan Lange)

## [0.1.5] - 2013-10-17
### Added
- Add support for python 3. https://code.google.com/p/pyiso8601/issues/detail?id=23 (thanks to zefciu)

### Changed
- Wow, it's alive! First update since 2007
- Moved over to https://bitbucket.org/micktwomey/pyiso8601
- Switched to py.test and tox for testing
- Make seconds optional in date format ("1997-07-16T19:20+01:00" now valid). https://bitbucket.org/micktwomey/pyiso8601/pull-request/1/make-the-inclusion-of-seconds-optional-in/diff (thanks to Chris Down)
- Support more variations of ISO 8601 dates, times and time zone specs.
- "Z" produces default timezone if one is specified (https://bitbucket.org/micktwomey/pyiso8601/issue/5/z-produces-default-timezone-if-one-is) (thanks to vfaronov). This one may cause problems if you've been relying on default_timezone to use that timezone instead of UTC. Strictly speaking that was wrong but this is potentially backwards incompatible.
- Handle compact date format (https://bitbucket.org/micktwomey/pyiso8601/issue/6/handle-compact-date-format) (thanks to rvandolson@esri.com)

### Fixed
- Correctly raise ParseError for more invalid inputs (https://bitbucket.org/micktwomey/pyiso8601/issue/1/raise-parseerror-for-invalid-input) (thanks to manish.tomar)
- Fix microsecond rounding issues (https://bitbucket.org/micktwomey/pyiso8601/issue/2/roundoff-issues-when-parsing-decimal) (thanks to nielsenb@jetfuse.net)
- Fix pickling and deepcopy of returned datetime objects (https://bitbucket.org/micktwomey/pyiso8601/issue/3/dates-returned-by-parse_date-do-not) (thanks to fogathmann and john@openlearning.com)
- Fix timezone offsets without a separator (https://bitbucket.org/micktwomey/pyiso8601/issue/4/support-offsets-without-a-separator) (thanks to joe.walton.gglcd)

## [0.1.4] - 2007-09-18
### Fixed
- The default_timezone argument wasn't being passed through correctly, UTC was being used in every case. Fixes issue 10.

## [0.1.3] - 2007-08-28
### Fixed
- Fixed the microsecond handling, the generated microsecond values were way too small. Fixes issue 9.

## [0.1.2] - 2007-07-24
### Added
- Adding ParseError to __all__ in iso8601 module, allows people to import it. Addresses issue 7.

### Changed
- Allow date/time separators other than T.
- Be a little more flexible when dealing with dates without leading zeroes. This violates the spec a little, but handles more dates as seen in the field. Addresses issue 6.

## [0.1.1] - 2007-03-30
### Changed
- When parsing dates without a timezone the specified default is used. If no default is specified then UTC is used. Addresses issue 4.

## [0.1.0] - 2007-01-04
### Added
- First release

[Unreleased]: https://github.com/micktwomey/pyiso8601/compare/2.1.0...HEAD
[2.1.0]: https://github.com/micktwomey/pyiso8601/compare/2.0.0...2.1.0
[2.0.0]: https://github.com/micktwomey/pyiso8601/compare/1.1.0...2.0.0
[1.1.0]: https://github.com/micktwomey/pyiso8601/compare/1.0.2...1.1.0
[1.0.2]: https://github.com/micktwomey/pyiso8601/compare/1.0.1...1.0.2
[1.0.1]: https://github.com/micktwomey/pyiso8601/compare/1.0.0...1.0.1
[1.0.0]: https://github.com/micktwomey/pyiso8601/compare/0.1.16...1.0.0
[0.1.16]: https://github.com/micktwomey/pyiso8601/compare/0.1.15...0.1.16
[0.1.15]: https://github.com/micktwomey/pyiso8601/compare/0.1.14...0.1.15
[0.1.14]: https://github.com/micktwomey/pyiso8601/compare/0.1.13...0.1.14
[0.1.13]: https://github.com/micktwomey/pyiso8601/compare/0.1.12...0.1.13
[0.1.12]: https://github.com/micktwomey/pyiso8601/compare/0.1.11...0.1.12
[0.1.11]: https://github.com/micktwomey/pyiso8601/compare/0.1.10...0.1.11
[0.1.10]: https://github.com/micktwomey/pyiso8601/compare/0.1.9...0.1.10
[0.1.9]: https://github.com/micktwomey/pyiso8601/compare/0.1.8...0.1.9
[0.1.8]: https://github.com/micktwomey/pyiso8601/compare/0.1.7...0.1.8
[0.1.7]: https://github.com/micktwomey/pyiso8601/compare/0.1.6...0.1.7
[0.1.6]: https://github.com/micktwomey/pyiso8601/compare/0.1.5...0.1.6
[0.1.5]: https://github.com/micktwomey/pyiso8601/compare/0.1.4...0.1.5
[0.1.4]: https://github.com/micktwomey/pyiso8601/compare/0.1.3...0.1.4
[0.1.3]: https://github.com/micktwomey/pyiso8601/compare/0.1.2...0.1.3
[0.1.2]: https://github.com/micktwomey/pyiso8601/compare/0.1.1...0.1.2
[0.1.1]: https://github.com/micktwomey/pyiso8601/compare/0.1.0...0.1.1
[0.1.0]: https://github.com/micktwomey/pyiso8601/releases/tag/0.1.0
