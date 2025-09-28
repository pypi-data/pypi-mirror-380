# Justfile for docdocgo project

# Default recipe
default:
    @just --list

# Run comprehensive tests and examples
test:
    @echo "🧪 Running test suite..."
    just test-unit
    @echo "🚀 Running examples..."
    just test-examples
    @echo "✅ Examples completed successfully!"

# Run only unit tests
test-unit:
    @echo "🧪 Running unit tests..."
    uv run pytest -v

# Run only examples
test-examples: generate-template
    #!/bin/bash
    echo "🚀 Running examples..."
    uv run python examples/basic_usage.py
    cd examples/project
    uv sync --index-strategy unsafe-best-match
    uv run python main.py

# Build Python wheels (placeholder for future implementation)
build:
    @echo "🏗️ Building Python wheels..."
    uv build

# Clean build artifacts and generated files
clean:
    @echo "🧹 Cleaning build artifacts..."
    rm -rf dist/
    rm -rf *.egg-info/
    rm -rf .pytest_cache/
    rm -rf htmlcov/
    find . -type d -name __pycache__ -exec rm -rf {} +
    find . -type f -name "*.pyc" -delete
    # Remove all generated .docx files from main directory
    rm -f *.docx
    # Remove generated files from examples/
    rm -f examples/template.docx
    rm -f examples/result.docx
    rm -f examples/temp_result.docx
    # Remove generated files from examples/output/
    rm -f examples/output/*.docx
    # Remove generated files from examples/project/
    rm -f examples/project/*.docx
    rm -f examples/project/result.docx
    rm -f examples/project/template.docx
    @echo "✅ Cleaned all build artifacts and generated files!"

# Install in development mode
install:
    @echo "📦 Installing in development mode..."
    uv sync

# Lint and format the code
lint:
    @echo "🔍 Running ruff linter..."
    uv run ruff check --fix .
    @echo "✨ Running ruff formatter..."
    uv run ruff format .
    @echo "✅ Linting and formatting completed!"

# Commit changes with message (depends on lint)
commit message: lint
    @echo "📝 Committing changes..."
    git add .
    git commit -m "{{ message }}"
    @echo "✅ Committed: {{ message }}"

# Prepare for publishing (lint, commit, verify clean)
publish-prepare: lint
    @echo "🔍 Checking if working directory is clean..."
    @if [ -n "$(git status --porcelain)" ]; then \
        echo "❌ Working directory is not clean. Please commit or stash changes."; \
        echo "Uncommitted changes:"; \
        git status --short; \
        exit 1; \
    fi
    @echo "✅ Working directory is clean, ready to publish!"

# Generate template Word document for project
generate-template output="examples/project/template.docx":
    @echo "📄 Generating Word template with two markers for project..."
    uv run python examples/generate_example_template.py --output "{{ output }}"
    @echo "✅ Template generated: {{ output }}"

# Test the template with docdocgo (now handled by basic_usage.py)
test-template:
    @echo "🧪 Testing template workflow (basic_usage.py handles template creation and processing)..."
    @echo "✅ Template test completed!"

# Full demo workflow
demo:
    @echo "🎬 Running full demo workflow..."
    just test-examples
    @echo "🎉 Full demo completed!"

# Publish to TestPyPI
publish-test:
    @echo "📦 Building package..."
    uv build
    @echo "🚀 Publishing to TestPyPI..."
    uv publish --publish-url https://test.pypi.org/legacy/ dist/* --token "$TESTPYI_TOKEN"
    @echo "✅ Published to TestPyPI successfully!"

# Publish to PyPI (production)
publish:
    @echo "📦 Building package..."
    uv build
    @echo "🚀 Publishing to PyPI..."
    uv publish dist/* --token "$UV_PUBLISH_TOKEN"
    @echo "✅ Published to PyPI successfully!"
