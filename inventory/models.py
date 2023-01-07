from django.db import models

# Create your models here.
class User(models.Model):
    Item_name=models.CharField(max_length=70)
    Total_Stock_In_KG=models.IntegerField()
    Price_Per_KG=models.IntegerField()
