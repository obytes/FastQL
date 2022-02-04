help:
	@echo "Targets:"
	@echo "    make test"
	@echo "    make start"
	@echo "    make down"
	@echo "    make pull"
	@echo "    make build"
	@echo "    make lint"
	@echo "    make clean"
	@echo "    make clean-test"

up:
	docker-compose up -d

down:
	docker-compose down

build:
	docker-compose build

test:
	docker-compose up -d && docker-compose run --rm fastql bash -c "pytest"

clean:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test:
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/
	rm -fr .pytest_cache