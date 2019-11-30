
# from django.contrib import admin
from django.urls import path
# from . import views
from firstapp import views
urlpatterns = [

    path('', views.home),
    path('add/', views.add),
    path('add-post/', views.add_post),
    path('list/', views.lists),
    path('delete/<id>/', views.delete),
    path('edit/<id>/', views.edit),
    path('update/<id>/', views.update),
    
    path('test/', views.test),


]
