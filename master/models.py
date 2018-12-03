from django.db import models
from django.contrib.auth.models import User


class Company(models.Model):
    name = models.CharField(max_length=50)
    master = models.ForeignKey(to=User, on_delete=True)

    def __str__(self):
        return "{} - {}".format(self.name, self.master)


class Item(models.Model):
    company = models.ForeignKey(Company, on_delete=True)
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return  "{} - {}".format(self.name, self.company)
