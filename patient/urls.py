from . import views
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('',views.home,name="home"),
    path('about/',views.about,name="about"),
    path('contact/',views.contact,name="contact"),
    path('allpatients/',views.allpatients,name="allpatients"),
    path('print/',views.print,name="print"),
    path('addpatient/',views.addpatient,name="addpatient"),
    path('savepatient/',views.savepatient,name="savepatient"),
    path('addhistory/',views.addhistory,name="addhistory"),
    path('visited/',views.visited,name="visited"),
    path('savehistory/',views.savehistory,name="savehistory"),
]
