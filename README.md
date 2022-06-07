# python-for-devops-june-2022
Python DevOps work with AWS and Actions


# python-for-devops-may-2022
Python DevOps work

### CI/CD - IAC
* CDK to create iam roles 

### Devops Cycle: 
  * SWE
  * Kaizen
  * Culture
  * Automation

## Create a project scaffold
* Colab Notebook 
* Create development environment that is cloud-based:
* Github Codespaces 
* AWS CloudShell
* AWS Cloud9

### Colab Notebook
* This is an example of how to use [colab](https://github.com/sotc/python-for-devops-may-2022/blob/main/getting_started_python.ipynb)

### Github Codespaces
Build out python project scaffold:

* [Makefile](https://github.com/sotc/python-for-devops-may-2022/blob/main/Makefile)
* [requirements.txt](https://github.com/sotc/python-for-devops-may-2022/blob/main/requirements.txt)
* [test_devopslib.py](https://github.com/sotc/python-for-devops-may-2022/blob/main/test_devopslib.py)
* [python_library](https://github.com/sotc/python-for-devops-may-2022/tree/main/devopslib)
* Dockerfile
* commandline tool
* Microservice

1. Create aa virtualenv: `python3 -m venv ~/.venv`
2. edit `~/.bashrc` add `source ~/.venv/bin/activate` #Codecolab container
3. clone project then run `make all`

## Commandline Tools and Step Functions

![StepFunctionCmdLine](https://user-images.githubusercontent.com/512362/171966733-09a69de4-c1ff-4c2d-8d80-f3e23f9a88ef.png)

## Microservices

## Containerized Continuous Delivery

`docker run -p 127.0.0.1:8080:8080 <dockerid>`
