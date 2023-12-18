from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

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

    def __str__(self):
        return f"{self.cart} - {self.product}"


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

    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    cart = models.ForeignKey("Cart", on_delete=models.CASCADE, verbose_name=_("Кошик"))
    delivery_method = models.PositiveSmallIntegerField(_("Спосіб доставки"), choices=DELIVERY_CHOICES.choices)
    payment_method = models.PositiveSmallIntegerField(
        _("Спосіб оплати"),
        choices=PAYMENT_CHOICES.choices,
        default=PAYMENT_CHOICES.CASH,
    )
    city = models.ForeignKey(to="order.City", on_delete=models.CASCADE, verbose_name=_("Місто"))
    branch_address = models.CharField(_("Адреса відділення"), max_length=255)

    def __str__(self):
        return f"{self.pk} - {self.cart.user}"


class City(models.Model):
    class Meta:
        verbose_name = _("Місто")
        verbose_name_plural = _("Міста")

    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"{self.name}"
