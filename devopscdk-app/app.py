#!/usr/bin/env python3
import os

import aws_cdk as cdk

from devopscdk_app.devopscdk_app_stack import DevopscdkAppStack


app = cdk.App()
DevopscdkAppStack(app, "DevopscdkAppStack",

    # Source current AWS Account and Region that are implied by the current CLI configuration.

    env=cdk.Environment(account=os.getenv('CDK_DEFAULT_ACCOUNT'), region=os.getenv('CDK_DEFAULT_REGION')),

    )

app.synth()
