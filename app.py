#!/usr/bin/env python3

from aws_cdk import core

from serverless_py.serverless_py_stack import ServerlessPyStack


app = core.App()
ServerlessPyStack(app, "serverless-py", env={"region": "ap-southeast-2"})

app.synth()
