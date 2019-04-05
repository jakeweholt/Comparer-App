echo Slightly Different:

curl -XPOST -H "Content-Type: application/json" http://54.188.138.74/compare -d '{
  "a": {
    "email": "jakeweholt@gmail.com",
    "last_4_ssn": "6969"
  },
  "b": {
    "email": "jake.weholt@gmail.com",
    "last_4_ssn": "6996"
  }
}';


echo 
echo Same:

curl -XPOST -H "Content-Type: application/json" http://54.188.138.74/compare -d '{
  "a": {
    "email": "jake.weholt@gmail.com",
    "last_4_ssn": "6969"
  },
  "b": {
    "email": "jake.weholt@gmail.com",
    "last_4_ssn": "6969"
  }
}'

echo 
echo Very Different:

curl -XPOST -H "Content-Type: application/json" http://54.188.138.74/compare -d '{
  "a": {
    "email": "tristan_lindborg@gmail.com",
    "last_4_ssn": "8013"
  },
  "b": {
    "email": "jake.weholt@gmail.com",
    "last_4_ssn": "6969"
  }
}'