from django.db import models

class District(models.Model):
    name = models.CharField(max_length=50)
    intro = models.TextField()
    area = models.CharField(max_length=150)
    population = models.CharField(max_length=50)

    def __str__(self):
        return self.name