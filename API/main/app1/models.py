from django.db import models

class Persons(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'persons'


class Users(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'users'
