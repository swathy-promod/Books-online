from django.urls import path
from . import views
app_name='User'

urlpatterns = [

# path('Homepage/', views.Homepage, name="Homepage"),
# path('UserProfile/', views.UserProfile, name='UserProfile'),
# path('UserEditProfile/', views.UserEditProfile, name='UserEditProfile'),
# path('UserChangePassword/',views.UserChangePassword, name='UserChangePassword'),
# path('ViewProducts/',views.ViewProducts, name='ViewProducts'),
# path('Booking/', views.Booking, name='Booking'),
# path('Cart/', views.Cart, name="Cart"),
# path('AddToCart/<int:id>/', views.AddToCart, name='AddToCart'),
# # path('ViewCart/', views.ViewCart, name='ViewCart'),
# # # path('CartDelete/<int:id>/', views.CartDelete, name="CartDelete"),
# path("Complaint/", views.Complaint, name="Complaint"),
# path('Payment/<int:id>/', views.Payment, name="Payment"),
# path('PaymentSuccess/', views.PaymentSuccess, name="PaymentSuccess"),
# path("Rating/<int:pid>/", views.Rating, name="Rating"),
# path("Feedback/", views.Feedback, name="Feedback"),

path('Homepage/', views.Homepage , name="Homepage"),
path('UserProfile/', views.UserProfile, name='UserProfile'),
path('UserEditProfile/', views.UserEditProfile, name='UserEditProfile'),
path('UserChangePassword/',views.UserChangePassword, name='UserChangePassword'),
path('addcart/<int:id>/', views.AddToCart, name="AddToCart"), 
path('Cart/', views.Cart , name="Cart"),
path('Payment/<int:id>/', views.Payment, name="Payment"),
path('Products/',views.Products, name='Products'),
path('DeleteBooking/<int:id>/', views.DeleteBooking, name='DeleteBooking'),
path('Booking/<int:id>/', views.Booking, name='Booking'),
path('PaymentSuccess/', views.PaymentSuccess, name='PaymentSuccess'),
path('Complaint/', views.Complaint, name='Complaint'),
path('MyBookings/', views.MyBookings, name='MyBookings'),
path('CancelBooking/<int:id>/', views.CancelBooking, name='CancelBooking'),
path('Logout/', views.Logout , name="Logout"),

]
