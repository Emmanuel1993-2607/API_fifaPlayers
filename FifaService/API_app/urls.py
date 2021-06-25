from django.urls.conf import include
from rest_framework import routers
from django.urls import path
from API_app.views import PlayerViewSet, TeamPlayersView

router = routers.DefaultRouter()
router.register(r'player', PlayerViewSet, basename="player")


url = [
    path('team', TeamPlayersView),    
]
