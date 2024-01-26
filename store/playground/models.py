from django.db import models


# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=155)
    origin = models.CharField(max_length=155)
    orders = models.IntegerField( null=True)
    lead_time = models.TimeField(max_length=155, null=True)
