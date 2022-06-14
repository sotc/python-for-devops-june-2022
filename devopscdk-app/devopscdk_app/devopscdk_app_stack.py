import aws_cdk as cdk
from constructs import Construct
from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
    aws_apigateway as apigw,
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