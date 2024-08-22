from django.urls import re_path
from . import consumers

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # This should point to your index view
]


websocket_urlpatterns = [
    re_path(r'ws/chat/$', consumers.ChatConsumer.as_asgi()),
]
