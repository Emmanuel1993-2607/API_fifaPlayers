from django.http.response import JsonResponse
from rest_framework.decorators import api_view
from rest_framework import viewsets, mixins

#rest_framework permissions
from API_app.serializers import PlayerSerializer, TeamSerializer
from API_app.models import Player, Team


#allows you to see players with the endpoint
class PlayerViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = PlayerSerializer
    def get_queryset(self):
        queryset = Player.objects.all()
        
        name = self.request.query_params.get('name')
        order = self.request.query_params.get('order')        
        
        if name is not None:
            queryset = queryset.filter(nameComp__icontains=name)

        if order is not None:
            queryset = queryset.order_by("nameComp" if order == "ask" else "-nameComp")
        else:
            queryset = queryset.order_by("nameComp")            
            
        return queryset



@api_view(['POST'])
def TeamPlayersView(request):
    if request.method == 'POST':        
        if "Name" in request.data:
            selectedTeam: Team = Team.objects.all().filter(teamName__icontains=request.data['Name']).first()
            if selectedTeam:
                Players = TeamSerializer(selectedTeam).data
                
                return JsonResponse({
                    'TeamName': selectedTeam.teamName,
                    'Players' : Players['player_set']
                    })
            else:
                return JsonResponse({
                    'message': "Team don't found"
                })
    

