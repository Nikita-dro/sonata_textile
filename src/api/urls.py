from django.urls import include, path
from rest_framework import routers

from api.views import (BrandViewSet, CartCreate, CartDelete, CartItemCreate,
                       CartItemDelete, CartItemListAll, CartItemListOne,
                       CartItemUpdate, CartListAll, CartListOne, CartUpdate,
                       CategoryViewSet, CityViewSet, CustomerCreate,
                       CustomerDelete, CustomerListAll, CustomerListOne,
                       CustomerUpdate, ProducingCountryViewSet, ProductCreate,
                       ProductDelete, ProductListAll, ProductListOne,
                       ProductUpdate)

app_name = "api"
router = routers.DefaultRouter()
router.register("category", CategoryViewSet)
router.register("country", ProducingCountryViewSet)
router.register("brand", BrandViewSet)
router.register("city", CityViewSet)
# router.register("cart", CartViewSet)
# router.register("cartitems", CartItemViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("customer/create/", CustomerCreate.as_view(), name="customer_create"),
    path("customer/update/<int:pk>/", CustomerUpdate.as_view(), name="customer_update"),
    path("customer/delete/<int:pk>/", CustomerDelete.as_view(), name="customer_delete"),
    path("customer/get-all/", CustomerListAll.as_view(), name="customers_all"),
    path("customer/get-one/<int:pk>/", CustomerListOne.as_view(), name="customer_one"),
    path("product/get-all/", ProductListAll.as_view(), name="products_all"),
    path("product/get-one/<int:pk>/", ProductListOne.as_view(), name="product_one"),
    path("product/create/", ProductCreate.as_view(), name="product_create"),
    path("product/update/<int:pk>/", ProductUpdate.as_view(), name="product_update"),
    path("product/delete/<int:pk>/", ProductDelete.as_view(), name="product_delete"),
    path("cart/get-all/", CartListAll.as_view(), name="carts_all"),
    path("cart/get-one/<int:pk>/", CartListOne.as_view(), name="cart_one"),
    path("cart/create/", CartCreate.as_view(), name="cart_create"),
    path("cart/update/<int:pk>/", CartUpdate.as_view(), name="cart_update"),
    path("cart/delete/<int:pk>/", CartDelete.as_view(), name="cart_delete"),
    path("cart-item/get-all/", CartItemListAll.as_view(), name="cart_items_all"),
    path("cart-item/get-one/<int:pk>/", CartItemListOne.as_view(), name="cart_item_one"),
    path("cart-item/create/", CartItemCreate.as_view(), name="cart_item_create"),
    path("cart-item/update/<int:pk>/", CartItemUpdate.as_view(), name="cart_item_update"),
    path("cart-item/delete/<int:pk>/", CartItemDelete.as_view(), name="cart_item_delete"),
]
