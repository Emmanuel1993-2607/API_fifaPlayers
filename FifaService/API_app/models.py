from django.db import models
from django.db.models.deletion import CASCADE


class Team(models.Model):
    teamName = models.CharField(max_length=65)

class Player(models.Model):
    nameComp = models.CharField(max_length=65)
    firstName = models.CharField(max_length=65)
    lastName = models.CharField(max_length=65)     
    position = models.CharField(max_length=65)
    idFifa = models.CharField(max_length=65)
    team = models.ForeignKey(Team, on_delete=CASCADE)


