"""
ASGI config for foxy project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os
from django.urls import path
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from chat.consumers import PersonalChatConsumer
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'foxy.settings')

application = get_asgi_application()
application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(URLRouter([path('ws/<int:id>/', PersonalChatConsumer.as_asgi())]))
})
