SHELL := /bin/bash
PYTHON ?= python
VENV_DIR ?= .venv
VENV_PYTHON := $(VENV_DIR)/bin/python
VENV_PIP := $(VENV_DIR)/bin/pip

.PHONY: help install setup activate generate-data list-notebooks run-week-%

help:
	@echo "Comandos disponíveis:"
	@echo "  make install         Cria o venv, instala requirements e registra o projeto"
	@echo "  make setup           Alias para make install"
	@echo "  make activate        Abre um shell com o ambiente virtual ativado"
	@echo "  make generate-data   Gera os datasets educacionais"
	@echo "  make list-notebooks  Lista os notebooks semanais"
	@echo "  make run-week-01     Abre o notebook da semana desejada no marimo"

$(VENV_DIR)/bin/activate:
	$(PYTHON) -m venv $(VENV_DIR)
	$(VENV_PYTHON) -m pip install --upgrade pip
	$(VENV_PIP) install -r requirements.txt
	$(VENV_PIP) install --no-build-isolation -e .

install: $(VENV_DIR)/bin/activate generate-data

setup: install

activate:
	@if [ ! -f $(VENV_DIR)/bin/activate ]; then \
		echo "Ambiente virtual não encontrado. Rode 'make install' primeiro."; \
		exit 1; \
	fi
	@echo "Abrindo shell com $(VENV_DIR) ativado. Use 'exit' para sair."
	@bash -i -c 'source $(VENV_DIR)/bin/activate && exec bash -i'

generate-data:
	$(VENV_PYTHON) scripts/generate_datasets.py

run-week-%:
	@find notebooks -maxdepth 1 -name 'semana_$*_*.py' -exec $(VENV_PYTHON) -m marimo edit {} \;

list-notebooks:
	@find notebooks -maxdepth 1 -name 'semana_*.py' | sort
