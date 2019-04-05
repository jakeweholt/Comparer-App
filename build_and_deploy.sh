docker build -t comparer_app .
eval $(aws ecr get-login --no-include-email --profile personal | sed 's|https://||')
docker tag comparer_app:latest 563257909816.dkr.ecr.us-west-2.amazonaws.com/comparer_app20190323
docker push 563257909816.dkr.ecr.us-west-2.amazonaws.com/comparer_app20190323