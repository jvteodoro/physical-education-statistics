PYTHON ?= python

setup:
	$(PYTHON) -m pip install --no-build-isolation -e .

generate-data:
	$(PYTHON) scripts/generate_datasets.py

run-week-%:
	$(PYTHON) -m marimo edit notebooks/semana_$*_*.py

list-notebooks:
	@find notebooks -maxdepth 1 -name 'semana_*.py' | sort
