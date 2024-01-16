from random import choice, randint

import requests
from django.core.files.base import ContentFile
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from djmoney.models.fields import MoneyField
from faker import Faker


class Product(models.Model):
    class Meta:
        verbose_name = _("Товар")
        verbose_name_plural = _("Товари")

    article = models.IntegerField(_("Артикул"), unique=True)
    avatar = models.ImageField(_("Зображення"), upload_to="img/products", null=True, blank=True)
    name = models.CharField(_("Назва"), max_length=250)
    category = models.ForeignKey(
        to="products.Category",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name=_("Категорія"),
    )
    brand = models.ForeignKey(
        to="products.Brand",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name=_("Бренд"),
    )
    price = MoneyField(_("Ціна"), max_digits=10, decimal_places=2, default_currency="UAH")
    size = models.CharField(_("Розмір"), max_length=50)
    material = models.ForeignKey(
        to="products.Material",
        on_delete=models.CASCADE,
        verbose_name=_("Матеірал"),
        null=True,
        blank=True,
    )
    producing_country = models.ForeignKey(
        to="products.ProducingCountry",
        on_delete=models.CASCADE,
        verbose_name=_("Країна виробництва"),
        null=True,
        blank=True,
    )
    availability = models.BooleanField(_("Наявність"), default=True)
    hit_sale = models.BooleanField(_("Хіт продаж"), default=False)
    description = models.TextField(_("Опис"), null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.article})"

    @classmethod
    def generate_instances(cls, count):
        faker = Faker()
        categories = Category.objects.all()
        brands = Brand.objects.all()
        materials = Material.objects.all()
        producing_countries = ProducingCountry.objects.all()

        for i in range(count):
            unique_article_generated = False
            while not unique_article_generated:
                article = randint(100, 9999)
                try:
                    Product.objects.get(article=article)
                except Product.DoesNotExist:
                    unique_article_generated = True

            product = Product.objects.create(
                article=article,
                name=faker.word(),
                category=choice(categories),
                brand=choice(brands),
                price=faker.random_int(min=100, max=3000),
                size=faker.random_element(elements=("S", "M", "L", "XL")),
                material=choice(materials),
                producing_country=choice(producing_countries),
                availability=faker.boolean(),
                hit_sale=faker.boolean(),
                description=faker.text(),
            )
            image_url = "https://picsum.photos/500/500"
            image_content = requests.get(image_url).content
            image_name = f"product_{timezone.now().strftime('%Y%m%d%H%M%S')}.jpg"

            product.avatar.save(image_name, ContentFile(image_content))


class Category(models.Model):
    class Meta:
        verbose_name = _("Категорія")
        verbose_name_plural = _("Категорії")

    name = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to="img/categories", null=True, blank=True)

    def __str__(self):
        return f"{self.name}"

    @classmethod
    def generate_instances(cls, count):
        faker = Faker()
        for i in range(count):
            unique_name_generated = False
            while not unique_name_generated:
                name = faker.word()
                try:
                    Category.objects.get(name=name)
                except Category.DoesNotExist:
                    unique_name_generated = True

            category = Category(name=name)
            image_url = "https://picsum.photos/500/500"
            image_content = requests.get(image_url).content
            image_name = f"category_{timezone.now().strftime('%Y%m%d%H%M%S')}.jpg"

            category.image.save(image_name, ContentFile(image_content))


class ProducingCountry(models.Model):
    class Meta:
        verbose_name = _("Країна виробництва")
        verbose_name_plural = _("Країни виробництва")

    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"{self.name}"

    @classmethod
    def generate_instances(cls, count):
        faker = Faker()
        for i in range(count):
            unique_name_generated = False
            while not unique_name_generated:
                name = faker.word()
                try:
                    ProducingCountry.objects.get(name=name)
                except ProducingCountry.DoesNotExist:
                    unique_name_generated = True

            ProducingCountry.objects.create(
                name=name,
            )


class Brand(models.Model):
    class Meta:
        verbose_name = _("Бренд")
        verbose_name_plural = _("Бренди")

    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"{self.name}"

    @classmethod
    def generate_instances(cls, count):
        faker = Faker()
        for i in range(count):
            unique_name_generated = False
            while not unique_name_generated:
                name = faker.word()
                try:
                    Brand.objects.get(name=name)
                except Brand.DoesNotExist:
                    unique_name_generated = True

            Brand.objects.create(
                name=name,
            )


class Material(models.Model):
    class Meta:
        verbose_name = _("Матеріал")
        verbose_name_plural = _("Матеріали")

    name = models.CharField(max_length=70, unique=True)

    def __str__(self):
        return f"{self.name}"

    @classmethod
    def generate_instances(cls, count):
        faker = Faker()
        for i in range(count):
            unique_name_generated = False
            while not unique_name_generated:
                name = faker.word()
                try:
                    Material.objects.get(name=name)
                except Material.DoesNotExist:
                    unique_name_generated = True

            Material.objects.create(
                name=name,
            )
