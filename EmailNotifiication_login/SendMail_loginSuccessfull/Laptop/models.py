from django.db import models

# Create your models here.
class Laptop(models.Model):
    company=models.CharField(max_length=50)
    model_name=models.CharField(max_length=50)
    ram=models.IntegerField()
    rom=models.FloatField()
    processor=models.CharField(max_length=30)
    weight=models.FloatField()
    price=models.FloatField()


    def __str__(self):
        return'{},{},{},{},{},{}'.format(self.company,self.model_name,self.ram,self.rom,self.price)