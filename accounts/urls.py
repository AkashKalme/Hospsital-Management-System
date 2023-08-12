from . import views
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('',views.login,name="login"),
    path('register/',views.register,name="register"),
    path('logout/',views.logout,name="logout"),
]
