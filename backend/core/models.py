from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    email = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    interests = models.CharField(max_length=255)


class Cars(models.Model):
    seats = models.IntegerField()
    animals = models.BooleanField()
    brand = models.CharField(max_length=255)
    owner = models.ForeignKey(Person, on_delete=models.CASCADE)
