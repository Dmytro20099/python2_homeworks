.PHONY: check
check:
	@echo 'Starting code correction'
	black .
	isort .
	flake8 .
	pytest .
	@echo 'FINISH'
