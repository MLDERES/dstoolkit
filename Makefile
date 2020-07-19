MODULE := mlderes.dstoolkit

build-dev:
	@echo "\nBuilding Dev"

build-prod:
	@echo "\nBuilding Prod"
	# Update version number
	pip uninstall mlderes.dstoolkit
	python setup.py sdist
	
push: build-prod
	# git commands for commiting changes, m

publish: build-prod
	twine upload --skip-existing -u mlderes dist/* 
	pip install mlderes.dstoolkit
