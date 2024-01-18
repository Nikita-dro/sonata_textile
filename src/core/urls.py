from django.urls import path

from core.views import (
    AboutUsView,
    AllCategoriesView,
    DeliveryView,
    IndexView,
    UserLogin,
    UserLogout,
    ContactsView,
    PartnersView,
)

app_name = "core"
urlpatterns = [
    path("index/", IndexView.as_view(), name="index"),
    path("about_us/", AboutUsView.as_view(), name="about_us"),
    path("delivery/", DeliveryView.as_view(), name="delivery"),
    path("categories/", AllCategoriesView.as_view(), name="all_categories"),
    path("login/", UserLogin.as_view(), name="login"),
    path("logout/", UserLogout.as_view(), name="logout"),
    path("contacts/", ContactsView.as_view(), name="contacts"),
    path("partners/", PartnersView.as_view(), name="partners"),
]
