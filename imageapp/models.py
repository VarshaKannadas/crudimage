from django.db import models

# Create your models here.
class Products(models.Model):
    product_name=models.CharField(max_length=100,null=True)
    price=models.IntegerField(null=True)
    quantity=models.IntegerField(null=True)
    image=models.ImageField(upload_to="image/",null=True)