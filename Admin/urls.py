from django.urls import path
from . import views
app_name = 'Admin'

urlpatterns = [
    path('Homepage/', views.Homepage, name="Homepage"),

    
    path('AdminRegistration/', views.AdminRegistration, name='AdminRegistration'),
    path('AdminDelete/<int:did>/', views.AdminDelete, name='AdminDelete'),
    path('AdminEdit/<int:eid>/', views.AdminEdit, name='AdminEdit'),
    
    path('District/', views.District, name='District'),
    path('DistrictDelete/<int:id>/', views.DistrictDelete, name='DistrictDelete'),
    path('DistrictEdit/<int:id>/',views.DistrictEdit, name='DistrictEdit'),

    path('Category/',views.Category,name='Category'),
    path('CategoryDelete/<int:id>/', views.CategoryDelete, name='CategoryDelete'),
    path('CategoryEdit/<int:id>/',views.CategoryEdit, name='CategoryEdit'),

    path('Place/',views.Place,name='Place'),
    path('PlaceDelete/<int:id>/', views.PlaceDelete, name='PlaceDelete'),
    path('PlaceEdit/<int:id>/',views.PlaceEdit, name='PlaceEdit'),

    path('Genre/',views.Genre,name='Genre'),
    path('GenreDelete/<int:id>/', views.GenreDelete, name='GenreDelete'),
    path('GenreEdit/<int:id>/',views.GenreEdit, name='GenreEdit'),

    
    # path('UserList/', views.UserList, name='UserList'),
    # path('accUser/<int:uid>', views.accUser, name='accUser'),
    # path('rejUser/<int:uid>', views.rejUser, name='rejUser'),

    # path('SellerList/', views.SellerList, name='SellerList'),
    # path('accSeller/<int:sid>', views.accSeller, name='accSeller'),
    # path('rejSeller/<int:sid>', views.rejSeller, name='rejSeller'),



]