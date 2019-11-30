# from django.contrib import admin  
from django.urls import path  
from account import views
# from . import views  
urlpatterns = [  

    path('add/', views.add),  
    path('add/<str:email>/<str:token>', views.verify),  
    path('login/', views.login),  
    path('logout/', views.logout),
    path('forget/', views.forget),  
    path('update/<str:email>/<str:token>', views.update),
    path('update/pass-page', views.update_pasword,name ="uploadpassword"),  
    # path('update/pass-page', views.update_pasword),  
    path('list/', views.lists),
    path('email/', views.email),
    # path('hello/', views.email),
]  