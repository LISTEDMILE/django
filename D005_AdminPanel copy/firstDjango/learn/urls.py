
from django.urls import path
from . import views

urlpatterns = [
    path('',views.learn,name='learn'),
    path('2',views.learn2,name='learn2'),
   
]
