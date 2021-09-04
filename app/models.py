from django.db import models


class Location(models.Model):

    class Meta:
        abstract = True

    name = models.CharField(blank=True, max_length=255, verbose_name='Name')
    area = models.PositiveIntegerField(null=True, blank=True, verbose_name='Area')
    population = models.PositiveIntegerField(null=True, blank=True, verbose_name='Population')

    def __str__(self):
        return str(self.id)


class Continent(Location):
    pass


class Country(Location):

    hospitals = models.PositiveIntegerField(null=True, blank=True, verbose_name='Country number of hospitals')
    national_parks = models.PositiveIntegerField(null=True, blank=True, verbose_name='Country number of national parks')

    # Relations
    continent = models.ForeignKey('Continent', null=True, on_delete=models.SET_NULL, related_name='countries')


class City(Location):

    roads = models.PositiveIntegerField(null=True, blank=True, verbose_name='City number of roads')
    trees = models.PositiveIntegerField(null=True, blank=True, verbose_name='City number of trees')

    # Relations
    country = models.ForeignKey('Country', null=True, on_delete=models.SET_NULL, related_name='cities')
    continent = models.ForeignKey('Continent', null=True, on_delete=models.SET_NULL, related_name='cities')
