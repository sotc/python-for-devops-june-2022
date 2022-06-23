#import aws_cdk as cdk
from constructs import Construct
from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
    aws_apigateway as apigw,
    aws_ecr as ecr,
    aws_codebuild as codebuild,
)

from constructs import Construct

class DevopscdkAppStack(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        my_lambda = _lambda.Function(
            self, 'FruitLambdaProxyIntegration',
            runtime=_lambda.Runtime.PYTHON_3_9,
            code=_lambda.Code.from_asset('lambdaDevOpsApp'), #code to deploy into lambda
            handler='fruit.handler',
        )
        api = apigw.LambdaRestApi(
            self, 'fruitapi',
            handler=my_lambda,
            proxy=True,
        )
        stage = apigw.StageOptions(
            stage_name="dev"
        )
        ecr_repo = ecr.Repository(
            self, "wikiSearchReop",
            repository_name="devops-june-2022"
            )
        build_docker_image = codebuild.BuildEnvironment(
            privileged=True
        )
        container_build = codebuild.Source.git_hub(
            owner="sotc",
            repo="https://github.com/sotc/python-for-devops-june-2022.git",

        )
        #codebuild.BuildSpec.from_source_filename()