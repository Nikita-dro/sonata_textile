from django.urls import path

from core.views import AboutUsView, AllCategoriesView, DeliveryView, IndexView

app_name = "core"
urlpatterns = [
    path("index/", IndexView.as_view(), name="index"),
    path("about_us/", AboutUsView.as_view(), name="about_us"),
    path("delivery/", DeliveryView.as_view(), name="delivery"),
    path("categories/", AllCategoriesView.as_view(), name="all_categories"),
]
