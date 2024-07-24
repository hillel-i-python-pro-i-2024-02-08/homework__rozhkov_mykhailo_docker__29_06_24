# Get user id for macOS and Linux
.PHONY: d-run
# Just run
d-run:
	docker compose up --build


.PHONY: d-purge
# Purge all data related with services
d-purge:
	docker compose down --volumes --remove-orphans --rmi local --timeout 0


.PHONY: poetry-export-requirements
# Export the current dependencies to requirements.txt.
poetry-export-requirements:
	poetry shell &&\
	poetry export --format requirements.txt --output requirements.txt --without-hashes --without dev