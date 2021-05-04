from django.db import models

# Create your models here.

class Make(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self) :
        return self.name

class Auto(models.Model):
    nickname = models.CharField(max_length=128)
    make = models.ForeignKey(Make, on_delete=models.CASCADE)
    mileage = models.IntegerField(null=True)
    comments = models.CharField(max_length=1024, blank=True)

    def __str__(self) :
        return self.nickname
