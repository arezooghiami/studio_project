import admin_thumbnails
from django.contrib import admin
from .models import *
from django_jalali.admin.filters import JDateFieldListFilter

# Register your models here.
class ProductVariantInlines(admin.TabularInline):
    model = Variatns
    extra = 2

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name' , 'create' , 'update')
    prepopulated_fields = {
        'slug':('name',)
    }
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name' , 'discount' , 'unit_price' , 'total_price' ,'create')
    inlines = [ProductVariantInlines,]




admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Variatns)
admin.site.register(Size)