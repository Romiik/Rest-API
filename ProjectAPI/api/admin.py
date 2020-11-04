from django.contrib import admin
from .models import Trainer, PokemonType, Pokemon


admin.site.register(Trainer)
admin.site.register(PokemonType)
admin.site.register(Pokemon)
