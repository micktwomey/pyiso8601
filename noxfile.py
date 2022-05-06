import nox


@nox.session(reuse_venv=True)
def lint(session: nox.Session):
    session.install("pytest", "hypothesis", "pytz", "black", "mypy", "isort")
    session.run("isort", "--check", "--diff", "iso8601")
    session.run("black", "--check", "--diff", "iso8601")
    session.run("mypy", "--strict", "iso8601")


@nox.session(reuse_venv=True)
def check_example(session: nox.Session):
    session.install(".", "mypy")
    session.run("mypy", "--strict", "docs/example.py")
    session.run("python", "docs/example.py")


@nox.session(reuse_venv=True)
def docs(session: nox.Session):
    session.install(".[docs]")
    session.run("sphinx-build", "docs", "docs/_build")


@nox.session(python=["3.7", "3.8", "3.9", "3.10", "3.11", "pypy3"], reuse_venv=True)
def test(session: nox.Session):
    session.install(".[test]")
    session.run("pytest", "-vv", "--tb=short", "--log-level=INFO")
