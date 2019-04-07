docker build -t comparer_app .;
eval $(aws ecr get-login --no-include-email --profile personal | sed 's|https://||');
docker tag comparer_app:latest $ECR_REG_ADDRESS;
docker push $ECR_REG_ADDRESS;