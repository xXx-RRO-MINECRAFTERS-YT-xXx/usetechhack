# Кейс №3
- Hackaton: Usetechhack

- Team: [xXx_PRO_MINECRAFTERS_YT_xXx](https://github.com/xXx-RRO-MINECRAFTERS-YT-xXx)

- Участники:
    * Адриан Макриденко: [@lyaguxafrog](https://github.com/lyaguxafrog)
    * Антон Архипов [@vard05](https://github.com/vard05)
    * Артемий Мятеж [@Ghost-ate-your-brains](https://github.com/Ghost-ate-your-brains)


## Стек

* Docker
* Docker-compose

### Frontend:
* JS
* Croc 
* React
* JSX

### Backend
* Python
* Django
* GraphQL
* Nginx
* PosgreSQL
* acme


## Запуск и деплой

1. Генерация конфига

```bash
$ ./helper.sh config
```
Генерируются `.env` в `client/` и `kernel/`
В `kernel/.env` нужно изменить `SECRET_KEY`, для этого можно использовать [Djecrety](https://djecrety.ir/)

2. Генерация схемы
```bash
$ ./helper.sh gql # для генерации новой схемы используйте флаг -d
```

3. Билд проекта
```bash
$ ./helper.sh build
```

4. Деплой
```bash
$ ./deploy.sh
```
Проект доступен по http://0.0.0.0/

## Структура проекта
```
.
│
├── client/ # Фронтенд
│    ├── .devcontainer/
│    ├── public/
│    ├── src/
│    ├── .env.example
│    ├── Dockerfile
│    ├── jsconfig.json
│    ├── package.json
│    └── yarn.lock
├── kernel/ # Бекенд
│    ├── .devcontainer/
│    ├── app_template/
│    ├── config/
│    ├── pizda/
│    ├── utils/
│    ├── .env.example
│    ├── dmanage.py
│    ├── Dockerfile
│    ├── entrypoint.sh
│    ├── manage.sh # скрипт управления бекендом
│    └── requirements.txt
├── keycloak
│    ├── .devcontainer/
│    └── Dockerfile
├── nginx
│    ├── Dockerfile
│    └── prod.conf
├── deploy.sh
├── docker-compose.yml
└── helper.sh
```
