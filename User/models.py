from django.db import models
from Seller.models import tbl_product
from User.models import *
from Guest.models import *


class tbl_booking(models.Model):
    booking_date = models.DateField(auto_now_add=True)
    booking_status = models.IntegerField(default=0)
    booking_amount = models.IntegerField()
    user = models.ForeignKey(tbl_user, on_delete=models.CASCADE, null=True, blank=True) 
    product = models.ForeignKey(tbl_product, on_delete=models.CASCADE, null=True, blank=True) 

class tbl_cart(models.Model):
    cart_status=models.IntegerField(default=0)
    cart_qnty=models.IntegerField(default=0)
    product=models.ForeignKey(tbl_product,on_delete=models.CASCADE, null=True, blank=True) 
    user = models.ForeignKey(tbl_user, on_delete=models.CASCADE, null=True, blank=True) 
    booking = models.ForeignKey(tbl_booking, on_delete=models.CASCADE, null=True, blank=True) 

 
class tbl_complaint(models.Model):
    complaint_title = models.CharField(max_length=30)
    complaint_details = models.CharField(max_length=100)
    complaint_date = models.DateField(auto_now_add=True)
    complaint_reply = models.CharField(max_length=100, default="No Reply Yet")
    complaint_status = models.IntegerField(default=0)
    product = models.ForeignKey(tbl_product, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(tbl_user, on_delete=models.CASCADE, null=True, blank=True)

class tbl_payment(models.Model):
    payment_amount = models.IntegerField()
    payment_date = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(tbl_user, on_delete=models.CASCADE, null=True, blank=True) 
    booking = models.ForeignKey(tbl_booking, on_delete=models.CASCADE, null=True, blank=True) 

    card_no = models.CharField(max_length=20)
    card_name = models.CharField(max_length=100)

    payment_status = models.IntegerField(default=1)

class tbl_rating(models.Model):
    rating_count =models.CharField(max_length=100)
    rating_comment =models.CharField(max_length=100)
    product=models.ForeignKey(tbl_product,on_delete=models.CASCADE, null=True, blank=True) 
    user=models.ForeignKey(tbl_user,on_delete=models.CASCADE, null=True, blank=True) 

class tbl_feedback(models.Model):
    feedback_content =models.CharField(max_length=100)


