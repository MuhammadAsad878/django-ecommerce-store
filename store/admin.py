from django.contrib import admin
from .models import Product
from import_export import resources
from import_export.admin import ImportExportModelAdmin



class ProductResource(resources.ModelResource):
    class Meta:
        model = Product
        fields = ('title', 'size', 'description', 'color', 'retail_price', 'wholesale_price', 'stock', 'image')

@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin):
    resource_class = ProductResource
    list_display = ('title', 'size', 'color', 'retail_price', 'stock')
