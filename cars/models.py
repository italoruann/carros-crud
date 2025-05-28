from django.db import models
from django.db.models import PROTECT


class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Car(models.Model):
    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=200)
    
    brand = models.ForeignKey(Brand, on_delete=PROTECT, related_name='car_brand')
    
    factory_year = models.IntegerField(null=True, blank=True)
    model_year = models.IntegerField(null=True, blank=True)
    plate = models.CharField(null=True, blank=True, max_length=7)
    value = models.FloatField(null=True, blank=True)
    photo = models.ImageField(upload_to='cars/', null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.model
    
class CarInventory(models.Model):
    cars_count = models.IntegerField()
    cars_value = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
        
    def __str__(self):
        return f'{self.cars_count} - {self.cars_value}'