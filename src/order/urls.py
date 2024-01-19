from django.urls import path

from .views import ShowBasketView, add_to_cart, cart_generate, order_view

app_name = "order"
urlpatterns = [
    path("add_to_cart/", add_to_cart, name="add_to_cart"),
    path("basket/", ShowBasketView.as_view(), name="show_basket"),
    path("generate-cart/", cart_generate, name="cart_generate"),
    path("decor/", order_view, name="order_view"),
]
