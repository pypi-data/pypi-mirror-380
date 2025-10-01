import nox

@nox.session
def lint(session):
    session.install("ruff")
    session.run("ruff", "check", ".")

@nox.session
def typecheck(session):
    session.install("mypy")
    session.run("mypy", ".")

@nox.session
def test(session):
    session.install("pytest")
    session.run("pytest")

