from django.db import models


# Create your models here.

class Proprietar(models.Model):
    nume = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return '%s %s' % (type(self), self.id)


class Animal(models.Model):
    nume = models.CharField(max_length=255)
    varsta = models.IntegerField()
    specie = models.CharField(max_length=255)
    proprietar = models.ForeignKey(Proprietar, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return '%s %s' % (type(self), self.id)
