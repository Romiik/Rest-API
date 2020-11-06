from django.shortcuts import render
from .models import Trainer, Pokemon
from .serializers import TrainerSerializer, PokemonSerializer
from rest_framework.views import APIView
from rest_framework import generics, mixins
from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets


class TrainerViewSet(viewsets.ModelViewSet):

    serializer_class = TrainerSerializer
    queryset = Trainer.objects.all()
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    #authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


class PokemonViewSet(viewsets.ModelViewSet):
    serializer_class = PokemonSerializer
    queryset = Pokemon.objects.all()
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
