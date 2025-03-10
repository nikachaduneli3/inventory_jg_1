from datetime import datetime
from django.db import models
from core.models import BaseModel
import random

class Category(BaseModel):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

def generate_barcode():
    digits = '0123456789'
    res = ''.join([random.choice(digits) for _ in range(13)])
    while Item.objects.filter(barcode=res).exists():
        res = ''.join([random.choice(digits) for _ in range(13)])
    return res

class Item(BaseModel):

    name = models.CharField(max_length=255)
    description  = models.TextField()
    price = models.FloatField()
    stock_qty = models.PositiveIntegerField()
    height = models.PositiveIntegerField(null=True)
    width = models.PositiveIntegerField(null=True)
    weight = models.PositiveIntegerField(null=True)
    expiration_date = models.DateField(null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='items')
    barcode =  models.CharField(max_length=13, editable=False, unique=True, default=generate_barcode)

    def __str__(self):
        return self.name
