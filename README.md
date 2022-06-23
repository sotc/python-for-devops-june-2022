[![Test On Multiple Python Versions](https://github.com/sotc/python-for-devops-june-2022/actions/workflows/main.yml/badge.svg)](https://github.com/sotc/python-for-devops-june-2022/actions/workflows/main.yml)

![AWS CodeBuild](https://codebuild.us-west-2.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoielplY0ZhaytrYmVzdGNDMm9peWFad1gvRno5UWowbGtVYTJTSU1qK0Y5RllDRUdGOGx0VExxMVViUHZ2cmZXTUNrY0ROYzl5MzRQeUhUUXpXa1NTRFJJPSIsIml2UGFyYW1ldGVyU3BlYyI6IjZMUUEwQ0lwYmk4NFduZ2EiLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=main)

# python-for-devops-june-2022
Python DevOps work with AWS and Actions


### CI/ CD - 
github Actions/ AWS CodeBuild

### IAC
CDK api gateway & lambda integration. Assumes aws cli installed and account environment variables setup already
1. cdk init 
2. uncomment cdk.Environment in app.py
3. cdk bootstrap
4. cdk deploy

## Try out api gateway and lambda fruit service. I'm using Httpie in the example below
* http POST https://<apigateway>/prod/ fruit=cherry
* http POST https://<apigateway>/prod/ fruit=durian

CDK CodeBuild github integration
1. Create ECR repo cdk methods < Add link to devopscdk_app_stack.py file here >
2. give CodeBuild permissions
2. Create CodeBuild and buildspec.yaml
3. `aws ecr get-login-password --region region | docker login --username AWS --password-stdin aws_account_id.dkr.ecr.region.amazonaws.com` Alternate authentication: `brew install docker-credential-helper-ecr`

CDK commands
 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation

### Devops Cycle: 
  * SWE
  * Kaizen
  * Culture
  * Automation

### Colab Notebook
* This is an example of how to use [colab](https://github.com/sotc/python-for-devops-june-2022/blob/main/getting_started_python.ipynb)

### Github Codespaces
Build out python project scaffold:

* [Makefile](https://github.com/sotc/python-for-devops-june-2022/blob/main/Makefile)
* [requirements.txt](https://github.com/sotc/python-for-devops-june-2022/blob/main/requirements.txt)
* [test_devopslib.py](https://github.com/sotc/python-for-devops-may-2022/blob/main/test_devopslib.py)
* [python_library](https://github.com/sotc/python-for-devops-may-2022/tree/main/devopslib)
* Dockerfile
* commandline tool
* Microservice

1. Create aa virtualenv: `python3 -m venv ~/.venv`
2. edit `~/.bashrc` add `source ~/.venv/bin/activate` #Codecolab container
3. clone project then run `make all`

## Microservices
* Create wikisearch.py and logic.py

## Containerized Microservice
* Create Dockerfile
* Create Container Repository in AWS ECR
* log into aws ecr using the command line
* docker build -t devops-june-2022 .
* docker tag devops-june-2022:latest `<tag name goes here>`
* docker push `<tag name>`
`docker run -p 127.0.0.1:8080:8080 <dockerid>`

## Tear down infrastructure
* cdk destroy
* cdk diff