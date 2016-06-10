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

Browser:
```javascript
var wsAddress = "ws://localhost:9999/ws/project/1/",
    socket = new WebSocket(wsAddress);
socket.onmessage = function(e) {
    console.log({onmessage: JSON.parse(e.data)});
};
socket.onopen = function() {
    console.log("websocket connected");
};
socket.onclose = function() {
    console.log("websocket disconnected");
};
```

Shell Plus
```
docker exec -ti channelsexample_wsserver_1 python3 manage.py shell_plus
from channels import Group
Group('project-1').send({'text': '{"a": "b"}'})
```
