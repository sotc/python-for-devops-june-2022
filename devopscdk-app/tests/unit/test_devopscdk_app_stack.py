import aws_cdk as core
import aws_cdk.assertions as assertions

from devopscdk_app.devopscdk_app_stack import DevopscdkAppStack

# example tests. To run these tests, uncomment this file along with the example
# resource in devopscdk_app/devopscdk_app_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = DevopscdkAppStack(app, "devopscdk-app")
    template = assertions.Template.from_stack(stack)

