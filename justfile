project := "iso8601"

# Run linting and test tasks
default: pre-commit lint test docs

# Run pre-commit
pre-commit COMMAND="run" *ARGS="--all-files":
    poetry run pre-commit {{COMMAND}} {{ARGS}}

# Run all linting actions
lint: ruff mypy

# Lint code with ruff
ruff COMMAND="check" *ARGS=".":
    poetry run ruff {{COMMAND}} {{ARGS}}

# Check code with Mypy
mypy *ARGS=".":
    poetry run mypy {{ARGS}}

# Run tests
test: pytest

# Run pytest tests
pytest  *ARGS="-v":
    poetry run pytest {{ARGS}}

# Run sphinx build
docs:
    poetry run sphinx-build docs docs/_build

# Add a CHANGELOG.md entry, e.g. just changelog-add added "My entry"
changelog-add TYPE ENTRY:
    poetry run changelog-manager add {{TYPE}} "{{ENTRY}}"

# Find out what your next released version might be based on the changelog.
next-version:
    poetry run changelog-manager suggest

# Build and create files for a release
prepare-release:
    #!/bin/bash
    set -xeuo pipefail
    poetry run changelog-manager release
    poetry version $(changelog-manager current)
    rm -rvf dist
    poetry build

# Tag and release files, make sure you run 'just prepare-release' first.
do-release:
    #!/bin/bash
    set -xeuo pipefail
    VERSION=$(changelog-manager current)
    POETRY_VERSION=$(poetry version -s)
    if [ "${VERSION}" != "${POETRY_VERSION}" ]; then
        echo "Mismatch between changelog version ${VERSION} and poetry version ${VERSION}"
        exit 1
    fi
    git add pyproject.toml CHANGELOG.md
    mkdir -p build
    poetry run changelog-manager display --version $VERSION > build/release-notes.md
    if [ ! -f dist/{{project}}-${VERSION}.tar.gz ]; then
        echo "Missing expected file in dist, did you run 'just prepare-release'?"
        exit 1
    fi
    poetry publish --dry-run
    git commit -m"Release ${VERSION}"
    git tag $VERSION
    git push origin $VERSION
    git push origin main
    gh release create $VERSION --title $VERSION -F build/release-notes.md ./dist/*
    poetry publish
    rm -rvf ./dist
