from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD
    path('home/', views.indexPage.as_view(), name='index'),
    path('about/', views.aboutUs, name='about'),
    path('contact/', views.contactUs, name='contact'),
    path('services/', views.services, name='services'),
   
=======
    path('home/', views.indexPage.as_view(), name='index')
    
>>>>>>> parent of 28c67a5 (Fixed CSS bug)
]