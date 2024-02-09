from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.indexPage.as_view(), name='index')
    
]