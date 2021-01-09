import nox

@nox.session(python=["3.6", "3.7", "3.8", "3.9", "pypy3"])
def tests(session):
    session.install("-r", "requirements.txt")
    session.install("-e", ".")
    session.install("pytest")
    session.run("pytest")

@nox.session
def lint(session):
    session.install("-r", "requirements.txt")
    session.install("-e", ".")
    session.install("flake8")
    session.run("flake8", "flaskr")