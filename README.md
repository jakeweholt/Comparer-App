# comparer

This is a flask app for computing string similarities.

## Dev Setup
Clone repo. In the comparer root directory, run the following:
```
pip install virtualenv
virtualenv --python=/location/of/interpreter/python3 venv
pip install -r requirements.txt
```
## Testing Changes Locally
After you've made changes, you can spin up a flask endpoint, by running `./deploy_flask.sh` (you may need to run `chmod +x ./deploy_flask.sh` first).

## Deploying to AWS
Before doing this, make sure to set up an environment variable `ECR_REG_ADDRESS` which is the URI of the ECR repo on AWS. You also need the AWS account credentials setup using the AWS CLI. To deploy to AWS run `./build_and_deploy.sh`. This will build the docker image and push it to AWS.

Log in to the AWS console, go to ECS, go to clusters, select comparer-prod, and update the cluster.

## Accessing the endpoint

Try this curl command: `curl -X POST -H "Content-Type: application/json" http://bigstuffedanimal.com/compare -d '{"a": {"email": "name@gmail.com","last_4_ssn": "0011"}, "b": {"email":"mane@gmail.com","last_4_ssn": "0000"}}'`
