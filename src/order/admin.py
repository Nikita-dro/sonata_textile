from django.contrib import admin

from order.models import Cart, CartItem, City, Order


class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 1


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    inlines = [CartItemInline]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    ...


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    ...
