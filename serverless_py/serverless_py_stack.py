from aws_cdk import (
    core,
    aws_lambda,
    aws_events as events,
    aws_events_targets as targets,
)

from pathlib import Path
import os


class ServerlessPyStack(core.Stack):
    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Make a layer from the dist folder
        layer = aws_lambda.LayerVersion(
            self,
            "CDKServerlessPyDeps",
            code=aws_lambda.Code.asset("dist"),
            compatible_runtimes=[aws_lambda.Runtime.PYTHON_3_6],
        )

        # Create my lambda with the attached layer
        requestsHandler = aws_lambda.Function(
            self,
            "RequestsHandler",
            layers=[layer],
            runtime=aws_lambda.Runtime.PYTHON_3_6,
            code=aws_lambda.Code.asset("src/functions/my_requests"),
            handler="index.handler",
            function_name="RequestsHandler",
        )

        # Run lambda once a day
        onceADayRule = events.Rule(
            self,
            "dhi-ftp-cron-rule",
            schedule=events.Schedule.cron(
                minute="0", hour="18", month="*", week_day="MON-SUN", year="*"
            ),
        )

        onceADayRule.add_target(targets.LambdaFunction(requestsHandler))
