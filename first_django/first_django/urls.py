
from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('test/', views.test),
    path('firstapp/', include('firstapp.urls')),
    path('employee/', include('employee.urls')),
    path('account/', include('account.urls')),
    path('product/', include('product.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)