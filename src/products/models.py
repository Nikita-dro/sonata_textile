from django.db import models
from django.utils.translation import gettext_lazy as _
from djmoney.models.fields import MoneyField


class Product(models.Model):
    class Meta:
        verbose_name = _("Товар")
        verbose_name_plural = _("Товари")

    article = models.IntegerField(_("Артикул"), unique=True)
    avatar = models.ImageField(_("Зображення"), upload_to="img/products", null=True, blank=True)
    name = models.CharField(_("Назва"), max_length=250)
    category = models.ForeignKey(to="products.Category", on_delete=models.CASCADE, verbose_name=_("Категорія"))
    brand = models.ForeignKey(
        to="products.Brand",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name=_("Бренд"),
    )
    price = MoneyField(_("Ціна"), max_digits=10, decimal_places=2, default_currency="UAH")
    size = models.CharField(_("Розмір"), max_length=50)
    material = models.CharField(_("Матеріал"), max_length=150)
    producing_country = models.ForeignKey(
        to="products.ProducingCountry",
        on_delete=models.CASCADE,
        verbose_name=_("Країна виробництва"),
    )
    availability = models.BooleanField(_("Наявність"), default=True)
    hit_sale = models.BooleanField(_("Хіт продаж"), default=False)
    description = models.TextField(_("Опис"), null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.article})"


class Category(models.Model):
    class Meta:
        verbose_name = _("Категорія")
        verbose_name_plural = _("Категорії")

    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"{self.name}"


class ProducingCountry(models.Model):
    class Meta:
        verbose_name = _("Країна виробництва")
        verbose_name_plural = _("Країни виробництва")

    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"{self.name}"


class Brand(models.Model):
    class Meta:
        verbose_name = _("Бренд")
        verbose_name_plural = _("Бренди")

    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"{self.name}"
