import os

from django.db.models import Sum
from django.db.models.signals import post_delete, post_save, pre_save
from django.dispatch import receiver

from gemini.client import get_car_description

from .models import Car, CarInventory


@receiver(post_delete, sender=Car)
def car_delete_photo(sender, instance, **kwargs):
    if instance.photo and os.path.isfile(instance.photo.path):
        os.remove(instance.photo.path)

def car_inventory_update():
    cars_count = Car.objects.count()
    total_value = Car.objects.aggregate(total_value=Sum('value'))['total_value'] or 0.0

    CarInventory.objects.create(
        cars_count=cars_count,
        cars_value=total_value
    )

@receiver([pre_save], sender=Car)
def car_signals_description(sender, instance, **kwargs):
    if not instance.description:
        description_ai = get_car_description(instance.model, instance.brand, instance.model_year)
        instance.description = description_ai

@receiver([post_save, post_delete], sender=Car)
def car_signals_inventory(sender, instance, **kwargs):
    car_inventory_update()