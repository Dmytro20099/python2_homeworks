.PHONY: run
run:
	isort .
	flake8 .
	pytest .
