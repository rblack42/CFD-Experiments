# Makefile for CFD Experiments Project

.PHONY: all
all: ## Process all source code	
	@cd py && make
	@cd cpp && make
	@cd go && make

.PHONY: init
init:
	python3 -m venv _venv
	mkdir -p docs rst/_static go cpp py

# .PHONY: reqs
reqs: ## Install Python requirements
	pip install -r requirements.txt
