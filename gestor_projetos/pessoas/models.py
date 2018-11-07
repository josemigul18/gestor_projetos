
from django.db import models

# Create your models here.
class Person(models.Model):
    username=models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    TYPE_PERSON = (
        ('P', 'Programer'),
        ('M', 'Manager'),
    )
    type_person = models.CharField(max_length=1, choices=TYPE_PERSON)

