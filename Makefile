setup:
	python3 -m venv ~/.junedevops

install:
	pip install -r requirements.txt

post-install:
	python -m textblob.download_corpora

lint:
	pylint --disable=R,C devopscdk-app/lambdaDevOpsApp/fruit.py

format:
	black devopscdk-app/lambdaDevOpsApp/*.py

deploy:
	echo "deploy to aws code here"

test-cdk:
	cd devopscdk-app; python -m pytest -vv

#test:
#	python -m pytest -vv --cov=devopslib

all: install post-install lint format deploy
