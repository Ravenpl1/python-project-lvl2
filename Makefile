install:
	poetry install

publish:
	poetry publish --dry-run

asciinema-rec:
	poetry run asciinema rec

package-install:
	python -m pip install --user dist/hexlet_code-0.1.0-py3-none-any.whl

package-uninstall:
	python -m pip uninstall hexlet-code

run-gendiff:
	poetry run gendiff ./tests/fixtures/file1.json ./tests/fixtures/file2.json

lint:
	poetry run flake8 gendiff

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=brain_games --cov-report xml

selfcheck:
	poetry check

check: selfcheck test lint

build: check
	poetry build

.PHONY: install test lint selfcheck check build