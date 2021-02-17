from django.db import models
from django_countries.fields import CountryField
from embed_video.fields import EmbedVideoField
from phone_field import PhoneField

class Item(models.Model):
    video = EmbedVideoField()  



class Country(models.Model):
    name = models.CharField(max_length=40)
    countrycode = models.SmallIntegerField()

    def __str__(self):
        return self.name


class Company(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Person(models.Model):
    firstname = models.CharField(max_length=150)
    lastname = models.CharField(max_length=150)
    email = models.EmailField(max_length=254)
    phone_number = PhoneField(null=False, blank=False, unique=True, help_text='Client phone number')
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, blank=True, null=True)
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, blank=True, null=True)
    objective = models.CharField(max_length=100)
    description = models.TextField(null=True, max_length=250)

    def __str__(self):
        return self.firstname