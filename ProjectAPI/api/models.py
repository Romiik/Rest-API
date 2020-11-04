from django.db import models


class Trainer(models.Model):
    name = models.CharField(max_length=200)
    town = models.CharField(max_length=100)
    age = models.IntegerField()
    birthday = models.DateTimeField()

    class Meta:
        verbose_name_plural = 'Trainers'

    def __str__(self):
        return '{}'.format(self.name)


class PokemonType(models.Model):
    p_type = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Pokemon Types'

    def __str__(self):
        return '{}'.format(self.p_type)


class Pokemon(models.Model):
    name = models.CharField(max_length=100)
    p_type = models.ForeignKey(PokemonType, on_delete=models.CASCADE)
    hp = models.IntegerField()

    class Meta:
        verbose_name_plural = 'Pokemons'

    def __str__(self):
        return '{}'.format(self.name)
