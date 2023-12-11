from django.contrib import admin

from products.models import Brand, Category, ProducingCountry, Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    ...


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    ...


@admin.register(ProducingCountry)
class ProducingCountryAdmin(admin.ModelAdmin):
    ...


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    ...
