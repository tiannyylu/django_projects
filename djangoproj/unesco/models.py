from django.db import models

class Iso(models.Model):
    name = models.CharField(max_length=128, null=True)

    def __str__(self):
        return self.name

class Region(models.Model):
    name = models.CharField(max_length=128, null=True)

    def __str__(self):
        return self.name

class States(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class Site(models.Model):
    name = models.CharField(max_length=128, null=True)
    description = models.CharField(max_length=128, null=True)
    justification = models.CharField(max_length=128, null=True)
    year = models.IntegerField(null=True)
    longitude = models.FloatField(null=True)
    latitude = models.FloatField(null=True)
    area_hectares = models.FloatField(null=True, default=0.0)
    iso = models.ForeignKey(Iso, on_delete=models.CASCADE, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, null=True, blank=True)
    states = models.ForeignKey(States, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self) :
        return self.name, self.description, self.year, self.longitude, self.latitude, self.area_hectares, self.iso
