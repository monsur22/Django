
# from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    # path('', views.home),
    # path('add/', views.add),
    # path('lists/', views.lists),
    # path('add-data/', views.add_data),
    path('reg/', views.reg),
    path('login/', views.login),


]
