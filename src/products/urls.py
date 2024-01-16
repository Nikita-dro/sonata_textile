from django.urls import path

from products.views import (ProductDetailView, ProductListView,
                            ProductSearchListView, brand_generate,
                            categories_generate, material_generate,
                            producing_country_generate, product_generate)

app_name = "products"
urlpatterns = [
    path("category/<int:pk>/", ProductListView.as_view(), name="category_products"),
    path("product/<int:pk>/", ProductDetailView.as_view(), name="product_info"),
    path("search/", ProductSearchListView.as_view(), name="search_product"),
    path("generate-category/<int:number>/", categories_generate, name="categories_generate"),
    path("generate-country/<int:number>/", producing_country_generate, name="producing_country_generate"),
    path("generate-brand/<int:number>/", brand_generate, name="brand_generate"),
    path("generate-material/<int:number>/", material_generate, name="material_generate"),
    path("generate/<int:number>/", product_generate, name="product_generate"),
]
