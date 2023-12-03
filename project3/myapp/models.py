from django.db import models

# Create your models here.
class Django_Table(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    salary = models.FloatField()
    
    
