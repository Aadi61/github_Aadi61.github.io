from django.db import models

class Drink(models.Model):

    name= models.CharField(max_length=200)
    descriptiom = models.CharField(max_length=500)
    unit=models.IntegerField()
    if name=='Orange':
        unit=5
    else:
        unit=4


    def __str__(self):
        return self.name+' '+self.descriptiom