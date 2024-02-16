from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.indexPage.as_view(), name='index'),
    path('about/', views.aboutUs, name='about'),
    path('contact/', views.contactUs, name='contact'),
    path('services/', views.services, name='services'),
   
]