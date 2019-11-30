from django.contrib import admin
from .models import Category
from .models import Product
# Register your models here.
class  CategoryModelAdmin(admin.ModelAdmin):
    list_display=["c_name"]
    search_fields=["c_name"]
    class Meta:
        model=Category



admin.site.register(Category,CategoryModelAdmin)
admin.site.register(Product)