# Pip and virtualenv - probably already installed

python -m ensurepip --upgrade
python -m pip install --upgrade pip
python -m pip install --upgrade virtualenv

# Create virtualenv

virtualenv -p python3 .env

source .env/bin/activate

# To install base CDK packages

pip install -r requirements.txt

# To add packages

`pip install requests aws-cdk.aws_events aws-cdk.aws_events_targets`

`pip freeze > requirements.txt`

# To deploy

Check it's valid

`cdk synth`

Bootstrap the env

`cdk bootstrap`

And deploy

`cdk deploy`
