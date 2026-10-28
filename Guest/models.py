from django.db import models
from Admin.models import tbl_district
from Admin.models import tbl_place

class tbl_user(models.Model):
    user_name=models.CharField(max_length=100)
    user_email=models.CharField(max_length=100)
    user_password=models.CharField(max_length=100)
    user_contact=models.CharField(max_length=100)
    place = models.ForeignKey(tbl_place, on_delete=models.CASCADE, null=True, blank=True) 
    user_gender=models.CharField(max_length=100)
    user_status=models.IntegerField(default=0)
    user_photo = models.FileField(upload_to='Assets/User/Photos/')
    user_bio=models.CharField(max_length=100)


class tbl_seller(models.Model):
    seller_name=models.CharField(max_length=100)
    seller_email=models.CharField(max_length=100)
    seller_contact=models.CharField(max_length=100)
    seller_password=models.CharField(max_length=100)
    seller_address=models.CharField(max_length=100)
    seller_photo = models.FileField(upload_to='Assets/Seller/Photos/')
    seller_proof = models.FileField(upload_to='Assets/Seller/Proof/')
    seller_status= models.IntegerField(default=0)
    place=models.ForeignKey(tbl_place, on_delete=models.CASCADE, null=True, blank=True)
    seller_doj=models.CharField(max_length=100)
    seller_doe=models.CharField(max_length=100)
    seller_licence=models.CharField(max_length=100)
    
class tbl_address(models.Model):
    address_details=models.CharField(max_length=100)
    user_id= models.ForeignKey(tbl_user, on_delete=models.CASCADE, null=True, blank=True)



