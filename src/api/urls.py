from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions, routers

from api.views import (BrandViewSet, CategoryViewSet, CityViewSet,
                       CustomerCreate, CustomerDelete, CustomerListAll,
                       CustomerListOne, CustomerUpdate,
                       ProducingCountryViewSet, ProductCreate, ProductDelete,
                       ProductListAll, ProductListOne, ProductUpdate)

app_name = "api"
router = routers.DefaultRouter()
router.register("category", CategoryViewSet)
router.register("country", ProducingCountryViewSet)
router.register("brand", BrandViewSet)
router.register("city", CityViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="Sonata Textile API",
        default_version="v1.0",
        description="API for passing questions",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="admin@admin.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path("", include(router.urls)),
    path("auth/", include("djoser.urls.jwt")),
    path("docs/", schema_view.with_ui("swagger", cache_timeout=0), name="swagger_docs"),
    path("customers/", CustomerListAll.as_view(), name="customers_all"),
    path("customers/<int:pk>/", CustomerListOne.as_view(), name="customer_one"),
    path("customers/create/", CustomerCreate.as_view(), name="customer_create"),
    path("customers/update/<int:pk>/", CustomerUpdate.as_view(), name="customer_update"),
    path("customers/delete/<int:pk>/", CustomerDelete.as_view(), name="customer_delete"),
    path("products/", ProductListAll.as_view(), name="products_all"),
    path("products/<int:pk>/", ProductListOne.as_view(), name="product_one"),
    path("products/create/", ProductCreate.as_view(), name="product_create"),
    path("products/update/<int:pk>/", ProductUpdate.as_view(), name="product_update"),
    path("products/delete/<int:pk>/", ProductDelete.as_view(), name="product_delete"),
]
