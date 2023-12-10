from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

from products.models import Product


class Cart(models.Model):
    class Meta:
        verbose_name = _("Кошик")
        verbose_name_plural = _("Кошик")

    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    items = models.ManyToManyField(Product, through="CartItem")

    def __str__(self):
        return f"{self.user}"


class CartItem(models.Model):
    class Meta:
        verbose_name = _("Інформація кошику")
        verbose_name_plural = _("Інформація кошику")

    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=_("Товар"))
    quantity = models.PositiveIntegerField(_("Кількість"), default=1)


class Order(models.Model):
    class Meta:
        verbose_name = _("Замовлення")
        verbose_name_plural = _("Замовлення")

    class DELIVERY_CHOICES(models.IntegerChoices):
        NEW_POST = 0, "Нова пошта"
        UKRAINIAN_POST = 1, "Укрпошта"

    class PAYMENT_CHOICES(models.IntegerChoices):
        CASH = 0, "Оплата при доставці"
        CARD = 1, "Переказ на карту"

    cart = models.ForeignKey("Cart", on_delete=models.CASCADE, verbose_name=_("Кошик"))
    first_name = models.CharField(_("Ім'я"), max_length=150)
    last_name = models.CharField(_("Прізвище"), max_length=150)
    middle_name = models.CharField(_("По батькові"), max_length=150)
    email = models.EmailField(_("Пошта"), max_length=150)
    phone_number = PhoneNumberField(_("Номер телефону"), null=True, blank=True)
    delivery_method = models.PositiveSmallIntegerField(_("Спосіб доставки"), choices=DELIVERY_CHOICES.choices)
    payment_method = models.PositiveSmallIntegerField(
        _("Спосіб оплати"),
        choices=PAYMENT_CHOICES.choices,
        default=PAYMENT_CHOICES.CASH,
    )
    city = models.CharField(_("Місто"), max_length=100)
    branch_address = models.CharField(_("Адреса відділення"), max_length=255)

    def __str__(self):
        return f"{self.pk} - {self.cart.user}"
