from django.urls import path
from . import views
app_name='Guest'

urlpatterns = [
    path('Login/', views.Login, name='Login'),

    path('ajaxplace/',views.ajaxplace,name="ajaxplace"),
    path('Homepage/', views.Homepage, name="Homepage"),
    path('', views.index, name="index"),


    path('UserRegistration/', views.UserRegistration, name='UserRegistration'),
  
    path('SellerRegistration/', views.SellerRegistration, name='SellerRegistration'),

    path('Logout/', views.Logout, name="Logout"),
]