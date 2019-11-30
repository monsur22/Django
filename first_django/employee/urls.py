# from django.contrib import admin  
from django.urls import path  
from employee import views  
urlpatterns = [  
    # path('admin/', admin.site.urls),  
    path('emp', views.emp),  
    path('show',views.show),  
    path('edit/<int:id>', views.edit), 
    # path('employe-edit/<int:id>', views.employe_edit), 
    path('update/<int:id>', views.update),  
    path('delete/<int:id>', views.destroy),  
]  