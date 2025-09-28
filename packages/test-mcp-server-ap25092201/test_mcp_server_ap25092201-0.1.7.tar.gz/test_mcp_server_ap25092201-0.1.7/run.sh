#!/bin/bash

set -e

THIS_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

######################
# ENVIRONMENT
######################

# Install core dependencies
function install {
    echo "Installing core dependencies..."
    uv sync --no-dev
}

# Install all development dependencies
function install:dev {
    echo "Installing development dependencies..."
    uv sync --extra dev --extra test --extra lint --extra typing --extra docs
}

function install:all {
    echo "Installing all dependencies..."
    uv sync --extra dev --extra test --extra lint --extra typing --extra docs
}

# Install specific dependency groups
function install:test {
    echo "Installing test dependencies..."
    uv sync --extra test
}

function install:lint {
    echo "Installing linting dependencies..."
    uv sync --extra lint
}

function install:docs {
    echo "Installing documentation dependencies..."
    uv sync --extra docs
}


# Update all dependencies
function update {
    echo "Updating dependencies..."
    uv sync --upgrade --extra dev --extra test --extra lint --extra typing --extra docs
}

# Update only core dependencies (removes extras - useful for testing package manager scenarios)
function update:core {
    echo "Updating core dependencies only (removing dev extras)..."
    uv sync --upgrade
}

# Create a new virtual environment
function venv {
    echo "Creating virtual environment..."

    # Manually deactivate conda environment if active
    if [ -n "$CONDA_DEFAULT_ENV" ]; then
        echo "Deactivating conda environment: $CONDA_DEFAULT_ENV"
        # Clean all conda-related variables
        unset CONDA_DEFAULT_ENV CONDA_PREFIX CONDA_PYTHON_EXE CONDA_PROMPT_MODIFIER
        # Restore original PATH (remove conda paths)
        if [ -n "$_CONDA_OLD_PATH" ]; then
            export PATH="$_CONDA_OLD_PATH"
        fi
    fi

    # Manually deactivate regular virtual environment if active
    if [ -n "$VIRTUAL_ENV" ]; then
        echo "Deactivating virtual environment: $(basename $VIRTUAL_ENV)"
        # Clean all venv-related variables
        unset VIRTUAL_ENV PYTHONHOME
        # Restore original PATH (remove venv paths)
        if [ -n "$_OLD_VIRTUAL_PATH" ]; then
            export PATH="$_OLD_VIRTUAL_PATH"
        else
            # Fallback: try to remove common venv path patterns
            export PATH=$(echo "$PATH" | sed -E 's|[^:]*\.venv/bin:||g' | sed -E 's|:[^:]*\.venv/bin||g')
        fi
    fi

    # Ensure clean environment for uv (comprehensive cleanup)
    unset VIRTUAL_ENV UV_ACTIVE PYTHONHOME

    # Check if .venv exists
    if [ ! -d ".venv" ]; then
        echo "Creating new virtual environment..."
        uv venv
    fi

    # Get project name for prompt - exactly like Poetry did
    PROJECT_NAME=$(grep '^name = ' pyproject.toml | cut -d'"' -f2 2>/dev/null || basename "$PWD")

    # Work with the user's existing prompt system by setting the right environment variables
    # The user's .zshrc has a precmd_venv_info() function that detects environments

    # Set up the virtual environment properly
    export VIRTUAL_ENV="$PWD/.venv"
    export PATH="$VIRTUAL_ENV/bin:$PATH"

    # Set UV_ACTIVE to distinguish this from regular venv or poetry
    # The user's precmd_venv_info() function needs to be enhanced to detect this
    export UV_ACTIVE=1
    export UV_PROJECT="$PROJECT_NAME"

    # Force zsh explicitly - the user's prompt function will handle the display
    SHELL=/bin/zsh exec /bin/zsh
}

# Lock dependencies without installing them
function lock {
    echo "Locking dependencies..."
    uv lock
}

# Create a new Jupyter kernel for the current project
function kernel {
    echo "Installing Jupyter kernel..."
    PYTHON_VERSION=$(uv run python -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')")
    PROJECT_NAME=$(grep '^name = ' pyproject.toml | cut -d'"' -f2)
    uv run python -m ipykernel install --user \
        --name="$PROJECT_NAME" \
        --display-name="Python $PYTHON_VERSION ($PROJECT_NAME)"
}

# Remove the Jupyter kernel for the current project
function remove:kernel {
    echo "Removing Jupyter kernel..."
    PROJECT_NAME=$(grep '^name = ' pyproject.toml | cut -d'"' -f2)
    uv run jupyter kernelspec remove "$PROJECT_NAME" -y
}

# Export requirements.txt files
function requirements {
    echo "Exporting requirements.txt..."
    uv export --no-hashes --format requirements-txt --output-file requirements.txt
    uv export --no-hashes --format requirements-txt --extra dev --extra test --extra lint --extra typing --extra docs --output-file requirements-dev.txt
    echo "Requirements files created successfully"
}

######################
# LINTING AND FORMATTING
######################

# Helper function to get Python files
function get:python:files {
    echo "./src/test_mcp_server_ap25092201/"
}

function get:python:files:diff {
    git diff --name-only --diff-filter=d main | grep -E '\.py$|\.ipynb$' || echo ""
}

function get:python:files:tests {
    echo "tests/"
}

# Individual linting functions
function lint:mypy {
    echo "Running mypy..."
    PYTHON_FILES="${1:-$(get:python:files)}"
    MYPY_CACHE="${2:-.mypy_cache}"

    if [ ! -z "$PYTHON_FILES" ]; then
        mkdir -p "$MYPY_CACHE"
        uv run mypy $PYTHON_FILES --cache-dir "$MYPY_CACHE"
    else
        echo "No Python files to check with mypy."
    fi
}

function lint:flake8 {
    echo "Running flake8..."
    PYTHON_FILES="${1:-$(get:python:files)}"

    if [ ! -z "$PYTHON_FILES" ]; then
        uv run flake8 $PYTHON_FILES
    else
        echo "No Python files to check with flake8."
    fi
}

function lint:pylint {
    echo "Running pylint..."
    PYTHON_FILES="${1:-$(get:python:files)}"

    if [ ! -z "$PYTHON_FILES" ]; then
        uv run pylint $PYTHON_FILES
    else
        echo "No Python files to check with pylint."
    fi
}

# Main linting function
function lint {
    lint:mypy
    lint:flake8
    lint:pylint
}

# Run all linters on changed files
function lint:diff {
    PYTHON_FILES=$(get:python:files:diff)
    echo "Running linters on changed files..."
    lint:mypy "$PYTHON_FILES" ".mypy_cache_diff"
    lint:flake8 "$PYTHON_FILES"
    lint:pylint "$PYTHON_FILES"
}

# Run all linters on test files
function lint:tests {
    PYTHON_FILES=$(get:python:files:tests)
    echo "Running linters on test files..."
    lint:mypy "$PYTHON_FILES" ".mypy_cache_test"
    lint:flake8 "$PYTHON_FILES"
    lint:pylint "$PYTHON_FILES"
}

# Individual formatting functions
function format:black {
    echo "Running black..."
    PYTHON_FILES="${1:-$(get:python:files)}"

    if [ ! -z "$PYTHON_FILES" ]; then
        uv run black $PYTHON_FILES
    else
        echo "No Python files to format with black."
    fi
}

function format:isort {
    echo "Running isort..."
    PYTHON_FILES="${1:-$(get:python:files)}"

    if [ ! -z "$PYTHON_FILES" ]; then
        uv run isort $PYTHON_FILES
    else
        echo "No Python files to format with isort."
    fi
}

# CI-specific formatting checks (don't modify files)
function format:check:black {
    echo "Checking code formatting with black..."
    PYTHON_FILES="${1:-$(get:python:files)}"

    if [ ! -z "$PYTHON_FILES" ]; then
        uv run black --check --diff $PYTHON_FILES
    else
        echo "No Python files to check with black."
    fi
}

function format:check:isort {
    echo "Checking import sorting with isort..."
    PYTHON_FILES="${1:-$(get:python:files)}"

    if [ ! -z "$PYTHON_FILES" ]; then
        uv run isort --check-only --diff $PYTHON_FILES
    else
        echo "No Python files to check with isort."
    fi
}


# Main formatting function
function format {
    format:black
    format:isort
}

# Combined format checking (for CI)
function format:check {
    format:check:black
    format:check:isort
}

# Run formatters on changed files
function format:diff {
    PYTHON_FILES=$(get:python:files:diff)
    echo "Running formatters on changed files..."
    format:black "$PYTHON_FILES"
    format:isort "$PYTHON_FILES"
}

# Run formatters on test files
function format:tests {
    PYTHON_FILES=$(get:python:files:tests)
    echo "Running formatters on test files..."
    format:black "$PYTHON_FILES"
    format:isort "$PYTHON_FILES"
}

# Combined check
function check {
    # Note: This applies formatting (for local development)
    install:all
    format
    lint
    tests
}

# Combined check for CI (format check + lint + test)
function check:ci {
    format:check
    lint
    tests
}

# Pre-commit check
function pre:commit {
    format:diff
    lint:diff
    tests
}

######################
# TESTING
######################

# Run tests
function tests {
    echo "Running tests..."
    TEST_FILE="${1:-$(get:python:files:tests)}"
    shift || true
    uv run pytest "$TEST_FILE" "$@"
}

# Run tests with coverage
function tests:cov {
    echo "Running tests with coverage..."
    TEST_FILE="${1:-$(get:python:files:tests)}"
    shift || true
    uv run pytest "$TEST_FILE" --cov=test_mcp_server_ap25092201  --cov-report=term "$@"
}

# Run tests in verbose mode
function tests:verbose {
    echo "Running tests in verbose mode..."
    TEST_FILE="${1:-$(get:python:files:tests)}"
    shift || true
    uv run pytest "$TEST_FILE" -v "$@"
}

# Run tests that match a specific pattern
function tests:pattern {
    if [ -z "$1" ]; then
        echo "Usage: test:pattern <pattern> [test_file]"
        return 1
    fi
    PATTERN="$1"
    TEST_FILE="${2:-$(get:python:files:tests)}"
    echo "Running tests matching pattern $PATTERN..."
    uv run pytest "$TEST_FILE" -k "$PATTERN"
}

# Run a specific test file
function tests:file {
    if [ -z "$1" ]; then
        echo "Usage: test:file <file> [pytest_args...]"
        return 1
    fi
    FILE="$1"
    shift
    echo "Running tests from file $FILE..."
    uv run pytest "$FILE" "$@"
}

# Generate coverage report
function coverage {
    echo "Generating coverage report..."
    uv run coverage report
    uv run coverage html
    echo "HTML coverage report generated in htmlcov/"
}

# Help for pytest options
function help:test {
    echo '====== Pytest Options ======'
    echo ''
    echo 'Usage: tests [test_file] [pytest_args...]'
    echo ''
    echo 'Common pytest options:'
    echo '  -v, --verbose           Show more detailed output'
    echo '  -x, --exitfirst         Stop on first failure'
    echo '  --pdb                   Start the Python debugger on errors'
    echo '  -m MARK                 Only run tests with specific markers'
    echo '  -k EXPRESSION           Only run test files that match expression'
    echo '  --log-cli-level=INFO    Show log messages in the console'
    echo '  --cov=PACKAGE           Measure code coverage for a package'
    echo '  --cov-report=html       Generate HTML coverage report'
    echo ''
    echo 'Examples:'
    echo '  ./run.sh tests tests/ -v'
    echo '  ./run.sh tests:pattern "test_async"'
    echo '  ./run.sh tests:file tests/test_example.py -v'
    echo '  ./run.sh tests:cov tests/unit/ --cov-report=html -v'
    echo ''
    echo 'Specialized test functions:'
    echo '  tests:verbose            Run tests with verbose output'
    echo '  tests:cov                Run tests with coverage report'
    echo '  tests:pattern <pattern>  Run test files matching pattern'
    echo '  tests:file <file>        Run tests in specific file'
}

######################
# DOCUMENTATION
######################

# Generate API documentation automatically
function docs:api {
    echo "Generating API documentation..."
    cd docs && uv run sphinx-apidoc -o api ../src/test_mcp_server_ap25092201 -f
}

# Generate documentation
function docs {
    echo "Building documentation..."
    cd docs && uv run make html
    echo "Documentation built in docs/_build/html/"
}

# Live documentation server
function docs:live {
    echo "Starting live documentation server..."
    uv run sphinx-autobuild docs docs/_build/html --open-browser
}

# Check documentation quality
function docs:check {
    echo "Checking documentation quality..."
    uv run doc8 docs/
    cd docs && uv run make linkcheck
}

# Clean and rebuild documentation
function docs:clean {
    echo "Cleaning documentation build files..."
    (cd docs && uv run make clean)
    (cd docs && uv run make html)
}

######################
# BUILDING AND PUBLISHING
######################

# Clean build artifacts
function clean {
    echo "Cleaning build artifacts..."
    rm -rf dist/ build/ *.egg-info/ .pytest_cache .mypy_cache* .coverage coverage.xml htmlcov/ docs/_build/

    # Clean cache directories safely (avoid virtual environments)
    find . -type d -name "__pycache__" -not -path "*env/*" -exec rm -rf {} + 2>/dev/null || true
    find . -type f -name "*.pyc" -not -path "*env/*" -exec rm {} + 2>/dev/null || true
}

# export the contents of .env as environment variables
function try-load-dotenv {
    if [ ! -f "$THIS_DIR/.env" ]; then
        echo "no .env file found"
        return 1
    fi

    while read -r line; do
        export "$line"
    done < <(grep -v '^#' "$THIS_DIR/.env" | grep -v '^$')
}

# Build package
function build {
    echo "Building package..."
    clean
    uv build .
}

# Publish to TestPyPI
function publish:test {
    echo "Publishing to TestPyPI..."
    try-load-dotenv || true  # Load .env file if it exists
    uv publish --publish-url https://test.pypi.org/legacy/
}

# Publish to PyPI
function publish {
    echo "Publishing to PyPI..."
    try-load-dotenv || true  # Load .env file if it exists
    uv publish
}

# Validate that package builds correctly
function validate:build {
    echo "Validating build..."
    build
    uv run pip install --force-reinstall dist/*.whl
    echo "Package installed successfully"
}

######################
# RELEASE
######################

# Helper function to get multi-line changes input
function get:changes {
    echo "Enter changes (empty line to finish):" >&2
    local changes=""
    while IFS= read -r line; do
        [[ -z "$line" ]] && break
        changes="${changes}- ${line}"$'\n'
    done
    echo "$changes"
}

# Release versions
function release:major {
    echo "Creating major release..."
    changes=$(get:changes)
    python scripts/release.py create major --changes "$changes"
}

function release:minor {
    echo "Creating minor release..."
    changes=$(get:changes)
    python scripts/release.py create minor --changes "$changes"
}

function release:micro {
    echo "Creating micro release..."
    changes=$(get:changes)
    python scripts/release.py create micro --changes "$changes"
}

function release:rc {
    echo "Creating release candidate..."
    changes=$(get:changes)
    python scripts/release.py create micro --pre rc --changes "$changes"
}

function release:beta {
    echo "Creating beta release..."
    changes=$(get:changes)
    python scripts/release.py create micro --pre b --changes "$changes"
}

function release:alpha {
    echo "Creating alpha release..."
    changes=$(get:changes)
    python scripts/release.py create micro --pre a --changes "$changes"
}

# Rollback release
function rollback {
    echo "Rolling back last release..."
    python scripts/release.py rollback
}

# Helper function to show available release commands
function help:release {
    echo "Available release commands:"
    echo "  release:major   - Create major release"
    echo "  release:minor   - Create minor release"
    echo "  release:micro   - Create micro release"
    echo "  release:rc      - Create release candidate"
    echo "  release:beta    - Create beta release"
    echo "  release:alpha   - Create alpha release"
    echo "  rollback        - Rollback last release"
}

######################
# HELP
######################

# print all functions in this file
function help {
    echo "$0 <task> <args>"
    echo ""
    echo "====== MCP Test Server Development Tool ======"
    echo ""
    echo "Environment:"
    echo "  install              - Install core dependencies"
    echo "  install:dev          - Install all development dependencies"
    echo "  install:test         - Install test dependencies"
    echo "  install:lint         - Install linting dependencies"
    echo "  install:docs         - Install documentation dependencies"
    echo "  install:all          - Install all dependencies"
    echo "  update               - Update all dependencies (preserves dev extras)"
    echo "  update:core          - Update core dependencies only (removes dev extras)"
    echo "  venv                 - Create and activate virtual environment"
    echo "  lock                 - Lock dependencies"
    echo "  kernel               - Create Jupyter kernel"
    echo "  remove:kernel        - Remove Jupyter kernel"
    echo "  requirements         - Export requirements.txt files"
    echo ""
    echo "Linting & Formatting:"
    echo "  format               - Run all formatters (applies changes)"
    echo "  format:check         - Check formatting without changes (CI)"
    echo "  format:diff          - Run formatters on changed files"
    echo "  format:tests         - Run formatters on test files"
    echo "  lint                 - Run all linters"
    echo "  lint:diff            - Run linters on changed files"
    echo "  lint:tests           - Run linters on test files"
    echo "  check                - Run format + lint + test (applies changes)"
    echo "  check:ci             - Run format check + lint + test (CI)"
    echo "  pre:commit           - Run format and lint on changed files"
    echo ""
    echo "Testing:"
    echo "  tests [file] [args]   - Run tests"
    echo "  tests:cov             - Run tests with coverage"
    echo "  tests:verbose         - Run tests in verbose mode"
    echo "  tests:pattern <pat>   - Run tests matching pattern"
    echo "  tests:file <file>     - Run specific test file"
    echo "  coverage              - Generate coverage report"
    echo "  help:tests            - Show detailed test help"
    echo ""
    echo "Documentation:"
    echo "  docs:api             - Generate API documentation"
    echo "  docs                 - Build documentation"
    echo "  docs:live            - Start live documentation server"
    echo "  docs:check           - Check documentation quality"
    echo "  docs:clean           - Clean and rebuild documentation"
    echo ""
    echo "Building & Publishing:"
    echo "  clean                - Clean build artifacts"
    echo "  build                - Build package"
    echo "  publish:test         - Publish to TestPyPI"
    echo "  publish              - Publish to PyPI"
    echo "  validate:build       - Validate build"
    echo ""
    echo "Release:"
    echo "  release:major        - Create major release"
    echo "  release:minor        - Create minor release"
    echo "  release:micro        - Create micro release"
    echo "  release:rc           - Create release candidate"
    echo "  release:beta         - Create beta release"
    echo "  release:alpha        - Create alpha release"
    echo "  rollback             - Rollback last release"
    echo "  help:release         - Show detailed release help"
    echo ""
    echo "Available functions:"
    compgen -A function | grep -v "^get:" | cat -n
}

TIMEFORMAT="Task completed in %3lR"
time ${@:-help}
