from django.db import models


class Materials(models.Model):

    name = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    description = models.TextField()
    units = models.CharField(max_length=250)
    choice = (("material","Material"),("service","Service"),)
    types = models.CharField(max_length=20,
                             choices=choice,
                             default="material")




    def __str__(self):
        return self.name
