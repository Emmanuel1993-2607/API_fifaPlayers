from API_app.models import Player, Team
from rest_framework import serializers


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'

class TeamSerializer(serializers.ModelSerializer):
    player_set = PlayerSerializer(many=True, read_only=True)
    class Meta:
        model = Team
        fields = ['teamName', 'player_set']

