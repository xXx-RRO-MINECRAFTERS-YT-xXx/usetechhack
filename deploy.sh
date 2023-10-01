#!/bin/bash

./helper.sh gql -d
./helper.sh build

docker-compose up -d --build nginx
docker-compose up -d --build keycloak 
