from django.contrib.auth import get_user_model


def sample_customer(email, **params):
    default = {
        "first_name": "TestFirstName",
        "last_name": "TestLastName",
    }
    default.update(params)
    return get_user_model().objects.create(email=email, **default)
