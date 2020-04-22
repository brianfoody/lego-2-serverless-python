import json
import pytest

from aws_cdk import core
from serverless_py.serverless_py_stack import CdkPythonLambdaStack


def get_template():
    app = core.App()
    CdkPythonLambdaStack(app, "serverless_py")
    return json.dumps(app.synth().get_stack("serverless_py").template)


def test_sqs_queue_created():
    assert "AWS::SQS::Queue" in get_template()


def test_sns_topic_created():
    assert "AWS::SNS::Topic" in get_template()
