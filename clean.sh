#!/bin/bash

# Remove Python cache directories and files
find . -type d -name "__pycache__" -exec rm -rf {} +
find . -type f -name "*.pyc" -delete
find . -type f -name "*.pyo" -delete

# Remove pytest cache
rm -rf .pytest_cache

# Remove coverage data
rm -f .coverage
rm -rf htmlcov

# Remove build artifacts
rm -rf build/
rm -rf dist/
rm -rf *.egg-info/