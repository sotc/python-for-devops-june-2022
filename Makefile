setup:
	python3 -m venv ~/.junedevops

post-install:
	python -m textblob.download_corpora

install:
	pip install -r requirements.txt

lint:
	pylint --disable=R,C devopsCDK/lambdaDevOpsApp/hello.py

test:
	python -m pytest -vv --cov=devopsCDK

format:
	black *.py lambdaDevOpsApp/*.py

deploy:
	#deploy

all: install post-install lint test format deploy
