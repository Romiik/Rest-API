from rest_framework import serializers
from .models import Trainer, Pokemon


class TrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainer
        # fields = ['id', 'name', 'town', 'age', 'birthday']
        fields = '__all__'


class PokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        # fields = ['id', 'name', 'p_type', 'hp']
        fields = '__all__'
