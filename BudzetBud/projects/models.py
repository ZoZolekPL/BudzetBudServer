import self as self
from django.conf import settings
from django.db import models


class Project(models.Model):

    title = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    owner = models.CharField(max_length=250, default='unknown')
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)

    description = models.TextField()
    timeStart = models.DateField()
    timeEnd = models.DateField()
    itsEnd = models.BooleanField(default=False)





    def __str__(self):
        return self.title
