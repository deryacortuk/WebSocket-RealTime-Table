from django.urls import path
from websocketTest import consumers

ws_urlpattern = [
    path('ws/data/',consumers.RealTimeData.as_asgi()),
]