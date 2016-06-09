from channels import route
from main.consumers import connect_project, disconnect_project

channel_routing = [
    route('websocket.connect', connect_project, path=r'^/ws/project/(?P<pk>\d+)/$'),
    route('websocket.disconnect', disconnect_project, path=r'^/ws/project/(?P<pk>\d+)/$'),
]
