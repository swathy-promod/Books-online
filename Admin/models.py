from django.db import models

class tbl_admin(models.Model):
  
    admin_name = models.CharField(max_length=100)
    admin_email = models.CharField(max_length=100)
    admin_password = models.CharField(max_length=100)

class tbl_category(models.Model):
    
    category_name = models.CharField(max_length=100)

class tbl_genre(models.Model):
    
    genre_name = models.CharField(max_length=100)   
    category_id = models.ForeignKey(tbl_category, on_delete=models.CASCADE, null=True, blank=True)


class tbl_district(models.Model):
    
    district_name=models.CharField(max_length=100)

class tbl_place(models.Model):
    
    place_name=models.CharField(max_length=100)
    district_id= models.ForeignKey(tbl_district, on_delete=models.CASCADE, null=True, blank=True)
