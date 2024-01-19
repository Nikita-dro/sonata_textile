from random import choice, randint

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

    @classmethod
    def generate_instances(cls):
        users = get_user_model().objects.all()
        products = Product.objects.all()
        for user in users:
            try:
                cart = Cart.objects.get(user=user)
                all_products = CartItem.objects.filter(cart=cart)
            except Cart.DoesNotExist:
                cart = Cart.objects.create(user=user)
                all_products = []
            if not all_products:
                for i in range(3):
                    product = choice(products)
                    quantity = randint(1, 5)
                    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

                    if not created:
                        cart_item.quantity += quantity
                        cart_item.save()


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

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    cart = models.TextField(verbose_name=_("Кошик"))
    delivery_method = models.PositiveSmallIntegerField(_("Спосіб доставки"), choices=DELIVERY_CHOICES.choices)
    payment_method = models.PositiveSmallIntegerField(
        _("Спосіб оплати"),
        choices=PAYMENT_CHOICES.choices,
        default=PAYMENT_CHOICES.CASH,
    )
    city = models.ForeignKey(to="order.City", on_delete=models.CASCADE, verbose_name=_("Місто"))
    branch_address = models.CharField(_("Адреса відділення"), max_length=255)

    def __str__(self):
        return f"{self.pk} - {self.user}"


class City(models.Model):
    class Meta:
        verbose_name = _("Місто")
        verbose_name_plural = _("Міста")

    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"{self.name}"
