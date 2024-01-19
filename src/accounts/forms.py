from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class UserRegistrationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        self.fields["password1"].help_text = ""
        self.fields["password2"].help_text = ""
        self.fields["password1"].label = _("Пароль")
        self.fields["password2"].label = _("Підтвердіть пароль")

    class Meta:
        model = get_user_model()
        fields = [
            "email",
            "phone_number",
            "password1",
            "password2",
            "first_name",
            "last_name",
        ]

        labels = {
            "email": _("Електронна пошта"),
            "phone_number": _("Номер телефону"),
            "first_name": _("Ім'я"),
            "last_name": _("Прізвище"),
        }

    def clean(self):
        _clean_data = super().clean()

        if (
            not bool(self.cleaned_data["email"])
            or not bool(self.cleaned_data["phone_number"])
            or not bool(self.cleaned_data["first_name"])
            or not bool(self.cleaned_data["last_name"])
        ):
            raise ValidationError(_("Всі поля є обов'язковими!"))

        if get_user_model().objects.filter(email=_clean_data["email"]).exists():
            raise ValidationError(_("Користувач із такою поштою вже існує!!!"))
        return _clean_data


# elif not bool(self.cleaned_data["email"]):
#     if (
#         get_user_model()
#         .objects.filter(phone_number=_clean_data["phone_number"])
#         .exists()
#     ):
#         raise ValidationError("User with phone number already exists!!!")
#
# elif not bool(self.cleaned_data["phone_number"]):
#     if get_user_model().objects.filter(email=_clean_data["email"]).exists():
#         raise ValidationError("User with email already exists!!!")
