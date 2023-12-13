from django.urls import path

from core.views import IndexView

app_name = "core"
urlpatterns = [
    path("index/", IndexView.as_view(), name="index"),
]
