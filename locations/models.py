from django.db import models
from django.contrib.auth.models import User
from items.models import Item

class Location(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    manager = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                                related_name='user_locations')

    def __str__(self):
        return self.name


class LocationItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='location_items')
    qty = models.PositiveIntegerField(default=1)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='location_items')

