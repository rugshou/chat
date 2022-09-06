"""
ASGI config for community project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os
from channels.routing import ProtocolTypeRouter
from django.core.asgi import get_asgi_application
from channels.routing import URLRouter
from channels.auth import AuthMiddlewareStack
import community_site.routing
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'community.settings')
django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': AuthMiddlewareStack(URLRouter(community_site.routing.websocket_urlpatterns)),
                })
