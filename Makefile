.PHONY: check
check:
	@echo 'Starting code correction'
	black .
	isort .
	flake8 .\main.py
	@echo 'FINISH'
