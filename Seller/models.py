from django.db import models
from Guest.models import  *
from Admin.models import *

class tbl_type(models.Model):
    type_name=models.CharField(max_length=100)

class tbl_product(models.Model):
    product_name=models.CharField(max_length=100)
    product_description=models.CharField(max_length=100)
    product_price=models.CharField(max_length=100)
    product_photo=models.FileField(upload_to='Assets/Seller/Photos/')
    type_id=models.ForeignKey(tbl_type, on_delete=models.CASCADE, null=True, blank=True)
    seller_id=models.ForeignKey(tbl_seller, on_delete=models.CASCADE, null=True, blank=True)

class tbl_productdetails(models.Model):
    productdetails_author_name=models.CharField(max_length=100)
    productdetails_content=models.CharField(max_length=100)
    productdetails_written=models.CharField(max_length=100)
    productdetails_published=models.CharField(max_length=100)
    product_id=models.ForeignKey(tbl_product, on_delete=models.CASCADE, null=True, blank=True) 

class tbl_stock(models.Model):
    stock_qnty=models.IntegerField()
    stock_date=models.DateField(auto_now_add=True)
    product_id=models.ForeignKey(tbl_product, on_delete=models.CASCADE, null=True, blank=True) 

class tbl_gallery(models.Model):
    gallery_file=models.FileField(upload_to='Assets/Seller/Photos/')
    product_id=models.ForeignKey(tbl_product, on_delete=models.CASCADE, null=True, blank=True) 






