from django.urls import path

from products.views import (ProductDetailView, ProductListView,
                            ProductSearchListView)

app_name = "products"
urlpatterns = [
    path("category/<int:pk>/", ProductListView.as_view(), name="category_products"),
    path("product/<int:pk>/", ProductDetailView.as_view(), name="product_info"),
    path("search/", ProductSearchListView.as_view(), name="search_product"),
]
