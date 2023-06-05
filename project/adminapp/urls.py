from django.urls import path
from adminapp import views
urlpatterns = [
    path('adminhome/',views.adminhome,name='adminhome'),
    path('adminlogin/',views.adminlogin,name='adminlogin'),
    path('adminsignup/',views.adminsignup,name='adminsignup'),
    path('adminlogout/',views.adminlogout,name='adminlogout'),
    path('user_reg/',views.user_reg,name='user_reg'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('updateuser/<int:id>', views.updateuser, name='updateuser'),
    path('updaterecord/<int:id>', views.updaterecord, name='updaterecord'),
] 
