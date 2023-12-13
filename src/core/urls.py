from django.urls import path

from core.views import AboutUsView, IndexView

app_name = "core"
urlpatterns = [
    path("index/", IndexView.as_view(), name="index"),
    path("about_us/", AboutUsView.as_view(), name="about_us"),
]
