from django.urls import path

from accounts.views import (ActivateUserView, UserRegistration,
                            customer_generate)

app_name = "accounts"
urlpatterns = [
    path("registration/", UserRegistration.as_view(), name="registration"),
    path(
        "activate/<str:uuid64>/<str:token>/",
        ActivateUserView.as_view(),
        name="user",
    ),
    path("generate/<int:number>/", customer_generate, name="customer_generate"),
]
