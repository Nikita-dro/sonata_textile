from django.urls import path

from .views import ShowBasketView, add_to_cart

app_name = "order"
urlpatterns = [
    path("add_to_cart/", add_to_cart, name="add_to_cart"),
    path("basket/", ShowBasketView.as_view(), name="show_basket"),
]
