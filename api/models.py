from django.db import models


# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=150)
    year_of_release = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name
