
# from django.contrib import admin
from django.urls import path
from . import views
# from product import views
from django.conf import settings

from django.conf.urls.static import static
from django.core.files.storage import FileSystemStorage
urlpatterns = [

#category Route
    path('category/add/', views.add),

    path('category/list/', views.lists),
    path('category/delete/<id>/', views.delete),
    path('category/edit/<id>/', views.edit),
    path('category/update/<id>/', views.update),
#Product Route   
    path('product-add/', views.product_add),

    path('product-list/', views.product_lists),
    path('product-delete/<id>/', views.product_delete),
    path('product-edit/<id>/', views.product_edit),
    path('product-update/', views.product_update,name ="upload"),


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)