import nox


@nox.session(reuse_venv=True)
def lint(session: nox.Session):
    session.install("pytest", "hypothesis", "pytz", "black", "mypy")
    session.run("black", "--check", "--diff", "iso8601")
    session.run("mypy", "iso8601")


@nox.session(reuse_venv=True)
def docs(session: nox.Session):
    session.install(".", "Sphinx")
    session.run("sphinx-build", "docs", "docs/_build")


@nox.session(python=["3.6", "3.7", "3.8", "3.9", "3.10", "pypy3"], reuse_venv=True)
def test(session: nox.Session):
    session.install(".")
    session.install("pytest", "hypothesis", "pytz")
    session.run("pytest", "-vv", "--tb=short", "--log-level=INFO")
