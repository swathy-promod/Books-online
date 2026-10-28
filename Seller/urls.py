from django.urls import path
from . import views

app_name = "Seller"

urlpatterns = [
    # path('Homepage/', views.Homepage, name="Homepage"),

    # # TYPE
    # path('Type/', views.Type, name='Type'),
    # path('DeleteType/<int:id>/', views.DeleteType, name='DeleteType'),

    # # PRODUCT
    # path('Product/', views.Product, name='Product'),
    # path('DeleteProduct/<int:id>/', views.DeleteProduct, name='DeleteProduct'),

    # # PRODUCT DETAILS
    # path('ProductDetails/', views.ProductDetails, name='ProductDetails'),
    # path('DeleteProductDetails/<int:id>/', views.DeleteProductDetails, name='DeleteProductDetails'),

    # # STOCK
    # path('Stock/', views.Stock, name='Stock'),
    # path('DeleteStock/<int:id>/', views.DeleteStock, name='DeleteStock'),

    path('Homepage/', views.Homepage,name='Homepage'),

    
    path('SellerProfile/', views.SellerProfile, name='SellerProfile'),
    path('SellerEditProfile/', views.SellerEditProfile, name='SellerEditProfile'),
    path('SellerChangePassword/',views.SellerChangePassword, name='SellerChangePassword'),
    
    path('AddProduct/', views.AddProduct, name='AddProduct'),
    path('ProductDelete/<int:id>/', views.ProductDelete, name='ProductDelete'),

    path('ViewBooking/',views.ViewBooking,name='ViewBooking'),
    path('ViewComplaint/',views.ViewComplaint,name="ViewComplaint"),

    path('Reply/<int:rid>',views.Reply,name="Reply"),
    
    path('AddStock/<int:pid>/',views.AddStock, name='AddStock'),
    path('StockDelete/<int:id>/<int:pid>/', views.StockDelete, name='StockDelete'),
    path('StockEdit/<int:id>/<int:pid>/',views.StockEdit, name='StockEdit'),
]