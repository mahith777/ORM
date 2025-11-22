from django.db import models
from django.contrib import admin
class product(models.Model):
    name=models.CharField(max_length=100)
    batch_number=models.IntegerField()
    product_id=models.IntegerField()
    manufacture_date=models.DateField()
    price=models.IntegerField()
    product_id=models.IntegerField(primary_key=True)
    colours=models.CharField(max_length=20)
class productAdmin(admin.ModelAdmin):
    list_display=["name","batch_number","product_id","manufacture_date","price","product_id","colours"]
