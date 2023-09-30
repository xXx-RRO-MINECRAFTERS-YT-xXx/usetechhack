#!/bin/bash

PROJECT=${PWD##*/}

if [[ $1 = 'help' ]]; then
    echo "usage: ./helper.sh [option]"
    echo ""
    echo "OPTIONS:"
    echo "help         Это сообщение"
    echo "config       Генерация .env"
    echo "gql          Генерация shema.json для GraphQL"
    echo "build        Собрать фронтенд"

fi

if [[ $1 = 'config' ]]; then
    rm -rf docs/
    cat ./kernel/.env.example >> ./kernel/.env
    echo "Don't forget to change your SECRET_KEY"
    echo "https://djecrety.ir/ can help you!"
    cat ./kernel/config/local_settings.example >> ./kernel/config/local_settings.py

    echo
    # Client configs
    cat ./client/.env.example >> ./client/.env
    echo "Don't forget to change env file in client application"
    exit 1
fi

if [[ $1 = 'gql' ]]; then

    if [[ $2 = '-d' ]]; then
        docker-compose up -d --build web
        docker exec ${PROJECT}-web-1 ./manage.sh gql
        docker-compose down
    fi

    cp ./kernel/schema.json ./client/schema.json
    exit 1
fi

if [[ $1 = 'build' ]]; then
    docker-compose up -d --build webclient
    docker exec ${PROJECT}-webclient-1 yarn install
    docker exec ${PROJECT}-webclient-1 yarn relay
    docker exec ${PROJECT}-webclient-1 yarn build
    docker-compose down

    rm -f client/schema.json
    rm -rf kernel/webclient
    cp -r client/build kernel/webclient
    rm -rf client/build

    exit 1
fi
