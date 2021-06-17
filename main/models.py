from django.db import models

# Create your models here.
class hero(models.Model):
    name = models.CharField(max_length=200)
    score = models.IntegerField()

    def __str__(self):
        return self.name
