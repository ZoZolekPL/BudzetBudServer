from django.conf import settings
from django.db import models

from projects.models import Project


class Vaulations(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)

    project = models.OneToOneField(Project,
                                   on_delete=models.CASCADE)
    stages = models.IntegerField()
    price = models.DecimalField(max_digits=10,decimal_places=2)

class Stage(models.Model):
    vaulation = models.OneToOneField(Vaulations,
                                     on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    stagePrice = models.DecimalField(max_digits=10,decimal_places=2)


class UnderStage(models.Model):
    lp = models.OneToOneField(Stage,
                              on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    unit = models.CharField(max_length=250)
    value = models.DecimalField(max_digits=10,decimal_places=2)
    priceForUnit = models.DecimalField(max_digits=10,decimal_places=2)
    fullPrice = models.DecimalField(max_digits=10,decimal_places=2)

