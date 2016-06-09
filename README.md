# Channels example

## Dev setup

```
docker-compose build
docker-compose up -d db
docker-compose run web reset_db
docker-compose run web migrate
docker-compose run web createsuperuser
docker-compose up
```

```
docker-compose run web makemigrations
docker-compose run web migrate
docker exec -ti channelsexample_web_1 ./post_migrate.sh
```
