# comparer

This is a flask app for computing string similarities.

## Dev Setup
Clone repo. In the comparer root directory, run the following:
```
pip install virtualenv
virtualenv --python=/location/of/interpreter/python3 venv
source venv/bin/activate
pip install -r requirements.txt
```
## Testing Changes Locally
After you've made changes, you can spin up a flask endpoint, by running `./deploy_flask.sh` (you may need to run `chmod +x ./deploy_flask.sh` first).

## Deploying to AWS
Before doing this, make sure to set up an environment variable `ECR_REG_ADDRESS` which is the URI of the ECR repo on AWS. You also need the AWS account credentials setup using the AWS CLI. To deploy to AWS run `./build_and_deploy.sh`. This will build the docker image and push it to AWS.

Log in to the AWS console, go to ECS, go to clusters, select comparer-prod, and update the cluster.

## Accessing live endpoints

Currently, there are two live endpoints to hit: `compare` and `match`. 

#### Compare
`compare` will take two vectors, and compare them element by element using both Levenshtein and a measure of the string similarity as a float in the range [0, 1]. Note that this is 1.0 if the sequences are identical, and 0.0 if they have nothing in common.

##### Example curl
```
curl -X POST -H "Content-Type: application/json" http://api.bigstuffedanimal.com/compare -d '{"a": {"email": "name@gmail.com","last_4_ssn": "0011"}, "b": {"email":"mane@gmail.com","last_4_ssn": "0000"}}'
```

##### Sample Response
```
{
  "a": {
    "email": "name@gmail.com",
    "last_4_ssn": "0011"
  },
  "b": {
    "email": "mane@gmail.com",
    "last_4_ssn": "0000"
  },
  "email": {
    "levenshtein_distance": 2,
    "similarity_probability": 0.8571428571428571
  },
  "last_4_ssn": {
    "levenshtein_distance": 2,
    "similarity_probability": 0.5
  }
}
```
#### Match
`match` will search within a search space for a value x. It returns the most likely match, as well as similarity scores for each item in the search space.

##### Example curl
```
curl -X POST -H "Content-Type: application/json" http://api.bigstuffedanimal.com/match -d '{"x": "tester_email@gmail.com", "search_base": ["tester.email@gmail.com", "email.tester@gmail.com", "fake.email@yahoo.com", "not_even_an_email@gmail.com"]}';
```
##### Sample Response
```
{
  "most_likely_match": "tester.email@gmail.com",
  "scores": {
    "email.tester@gmail.com": {
      "similarity_probability": 0.7272727272727273
    },
    "fake.email@yahoo.com": {
      "similarity_probability": 0.5714285714285714
    },
    "not_even_an_email@gmail.com": {
      "similarity_probability": 0.7755102040816326
    },
    "tester.email@gmail.com": {
      "similarity_probability": 0.9545454545454546
    }
  },
  "x": "tester_email@gmail.com"
}
```


