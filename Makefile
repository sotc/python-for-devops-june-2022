setup:
	python3 -m venv ~/.junedevops

install:
	pip install -r requirements.txt

lint:
	pylint --disable=R,C devopscdk-app/lambdaDevOpsApp/fruit.py

format:
	black devopscdk-app/lambdaDevOpsApp/*.py

deploy:
	echo "deploy code"

all: install post-install lint test format deploy

#test:
#	python -m pytest -vv --cov=devopscdk-app
