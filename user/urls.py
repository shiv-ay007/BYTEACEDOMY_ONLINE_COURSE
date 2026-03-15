from django.urls import path
from . import views

urlpatterns= [
    path('', views.index),
    path('aboutus/', views.about),
    path('team/', views.team),
    path('gallery/', views.gallery),
    path('services/', views.services),
    path('index/', views.index),
    path('login/', views.login),
    path('register/', views.register),
    path('logout/', views.logout),
    path('contact/', views.contact),
   
    # You can add more paths here as needed
    # Add more paths as needed
]