# Makefile for CFD Experiments Project
PROJNAME := $(notdir $(PWD))

.PHONY: all
all: ## Process all source code	
	@cd src && make

.PHONY: init
init:
	python3 -m venv _venv
	mkdir -p docs rst/_static

# .PHONY: reqs
reqs: ## Install Python requirements
	pip install -r requirements.txt

.PHONY: test
test:
	cd src && make test

.PHONY: html
html:
	cd rst && sphinx-build -d _build/doctrees . ../docs

.PHONY: ui
ui:	src/$(PROJNAME).ui
	pyuic5 --output src/UI_$(PROJNAME).py $<
