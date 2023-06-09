project := "iso8601"

# Run tests via pytest
test:
    poetry run pytest -v

# Run nox tests
nox *ARGS="-x":
    poetry run nox {{ARGS}}

# Add a CHANGELOG.md entry, e.g. just changelog-add added "My entry"
changelog-add TYPE ENTRY:
    changelog-manager add {{TYPE}} "{{ENTRY}}"

# Find out what your next released version might be based on the changelog.
next-version:
    changelog-manager suggest

# Build and create files for a release
prepare-release:
    #!/bin/bash
    set -xeuo pipefail
    changelog-manager release
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
    changelog-manager display --version $VERSION > build/release-notes.md
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
