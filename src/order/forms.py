from django import forms
from django.utils.translation import gettext_lazy as _

from order.models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["delivery_method", "payment_method", "city", "branch_address"]

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user

        if user.social_auth.filter(provider="google-oauth2").exists():
            user_info_dict = {
                "first_name": user.first_name,
                "last_name": user.last_name,
                "phone_number": user.phone_number,
            }
            translate_fields = {"first_name": "Ім'я", "last_name": "Прізвище", "phone_number": "Номер телефону"}
            filtered_user_info = {key: value for key, value in user_info_dict.items() if value is None}
            for key in filtered_user_info:
                self.fields[key] = forms.CharField(label=_(translate_fields[key]), max_length=80, required=True)

        for field_name in self.fields:
            self.fields[field_name].required = True
