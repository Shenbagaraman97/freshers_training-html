from django.db import models

# Create your models here.






class Employeetable(models.Model):
    firstname = models.CharField(max_length=100, blank=True, null=True)
    lastname = models.CharField(max_length=100, blank=True, null=True)
    fullname = models.CharField(max_length=100, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    age = models.IntegerField(blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employeetable'