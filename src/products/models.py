from django.db import models
from django.utils.translation import gettext_lazy as _


class Product(models.Model):
    class Meta:
        verbose_name = _("Товар")
        verbose_name_plural = _("Товари")

    class CATEGORY_CHOICES(models.IntegerChoices):
        TOWELS = 0, "Рушники"
        BLANKETS = 1, "Ковдри"
        BED_LINEN = 2, "Постільна білизна"
        PILLOWS = 3, "Подушки"
        PLAIDS = 4, "Пледи"
        BEDSPREADS = 5, "Покривала"
        MATTRESS_COVER = 6, "Наматрацники"
        TABLECLOTHS = 7, "Скатертини"
        PILLOWCASES = 8, "Декоративні наволочки"
        KITCHEN_TEXTILES = 9, "Кухонний текстиль"
        SHEETS = 10, "Простирадла"

    article = models.IntegerField(_("Артикул"), unique=True)
    name = models.CharField(_("Назва"), max_length=250)
    category = models.PositiveSmallIntegerField(_("Категорія"), choices=CATEGORY_CHOICES.choices)
    price = models.IntegerField(_("Ціна"))
    producing_country = models.CharField(_("Країна виробництва"), max_length=120)
    availability = models.BooleanField(_("Наявність"), default=True)
    description = models.TextField(_("Опис"), null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.article})"


class Towel(models.Model):
    class Meta:
        verbose_name = _("Рушник")
        verbose_name_plural = _("Рушники")

    class TYPE_CHOICES(models.IntegerChoices):
        HAND = 0, "Для рук"
        FACE = 1, "Для обличчя"
        BATH_HOUSE = 2, "Банні"
        SAUNA = 3, "Сауна"
        SETS = 4, "Набори"
        CORNER = 5, "Куточки"

    product = models.OneToOneField(to="products.Product", on_delete=models.CASCADE, related_name="towels")
    brand = models.CharField(_("Бренд"), max_length=150)
    material = models.CharField(_("Матеріал"), max_length=150)
    size = models.CharField(_("Розмір"), max_length=50)
    type = models.PositiveSmallIntegerField(_("Тип"), choices=TYPE_CHOICES.choices)

    def __str__(self):
        return f"{self.product.name} ({self.product.article})"


class Blanket(models.Model):
    class Meta:
        verbose_name = _("Ковдра")
        verbose_name_plural = _("Ковдри")

    class SEASONALITY_CHOICES(models.IntegerChoices):
        DEMI_SEASON = 0, "Демісезонні"
        WINTER = 1, "Зимові"
        SUMMER = 2, "Літні"

    product = models.OneToOneField(to="products.Product", on_delete=models.CASCADE, related_name="blankets")
    size = models.CharField(_("Розмір"), max_length=50)
    cover_material = models.CharField(_("Матеріал чохла"), max_length=150)
    filler = models.CharField(_("Наповнювач"), max_length=150)
    seasonality = models.PositiveSmallIntegerField(_("Сезонність"), choices=SEASONALITY_CHOICES.choices)

    def __str__(self):
        return f"{self.product.name} ({self.product.article})"


class BedLinen(models.Model):
    class Meta:
        verbose_name = _("Постільна білизна")
        verbose_name_plural = _("Постільна білизна")

    class SIZE_CHOICES(models.IntegerChoices):
        CHILDISH = 0, "Дитячий"
        TEENAGE = 1, "Підлітковий"
        ONE = 2, "Полуторний"
        TWO = 3, "Двоспальний"
        EURO = 4, "Євро"
        FAMILY = 5, "Сімейний"

    product = models.OneToOneField(to="products.Product", on_delete=models.CASCADE, related_name="bed_linens")
    brand = models.CharField(_("Бренд"), max_length=150)
    size = models.PositiveSmallIntegerField(_("Спальний розмір"), choices=SIZE_CHOICES.choices)
    material = models.CharField(_("Матеріал"), max_length=150)
    size_duvet_cover = models.PositiveSmallIntegerField(_("Розмір підковдри"))
    sheet_size = models.PositiveSmallIntegerField(_("Розмір простирадла"))
    pillowcase_size = models.PositiveSmallIntegerField(_("Розмір наволочки"))

    def __str__(self):
        return f"{self.product.name} ({self.product.article})"


class Pillow(models.Model):
    class Meta:
        verbose_name = _("Подушка")
        verbose_name_plural = _("Подушки")

    product = models.OneToOneField(to="products.Product", on_delete=models.CASCADE, related_name="pillows")
    brand = models.CharField(_("Бренд"), max_length=150)
    size = models.CharField(_("Розмір"), max_length=50)
    cover_material = models.CharField(_("Матеріал чохла"), max_length=150)
    filler = models.CharField(_("Наповнювач"), max_length=150)

    def __str__(self):
        return f"{self.product.name} ({self.product.article})"


class Plaid(models.Model):
    class Meta:
        verbose_name = _("Плед")
        verbose_name_plural = _("Пледи")

    class SIZE_PLAID_CHOICES(models.IntegerChoices):
        CHILDISH = 0, "Дитячий"
        ONE = 1, "Полуторний"
        TWO = 2, "Двоспальний"
        EURO = 3, "Євро"

    product = models.OneToOneField(to="products.Product", on_delete=models.CASCADE, related_name="plaids")
    brand = models.CharField(_("Бренд"), max_length=150)
    size = models.CharField(_("Розмір"), max_length=50)
    material = models.CharField(_("Матеріал"), max_length=150)
    type = models.PositiveSmallIntegerField(_("Спальний розмір"), choices=SIZE_PLAID_CHOICES.choices)

    def __str__(self):
        return f"{self.product.name} ({self.product.article})"


class Bedspread(models.Model):
    class Meta:
        verbose_name = _("Покривало")
        verbose_name_plural = _("Покривала")

    class SIZE_BEDSPREAD_CHOICES(models.IntegerChoices):
        ONE = 0, "Полуторний"
        EURO = 1, "Євро"

    product = models.OneToOneField(to="products.Product", on_delete=models.CASCADE, related_name="bedspreads")
    size = models.CharField(_("Розмір"), max_length=50)
    material = models.CharField(_("Матеріал"), max_length=150)
    type = models.PositiveSmallIntegerField(_("Спальний розмір"), choices=SIZE_BEDSPREAD_CHOICES.choices)
    complete_set = models.CharField(_("Комплектація"), max_length=260)

    def __str__(self):
        return f"{self.product.name} ({self.product.article})"


class MattressCovers(models.Model):
    class Meta:
        verbose_name = _("Наматрацник")
        verbose_name_plural = _("Наматрацники")

    class SIZE_MATTRESS_CHOICES(models.IntegerChoices):
        CHILDISH = 0, "Дитячий"
        SINGLE = 1, "Односпальний"
        ONE = 2, "Полуторний"
        TWO = 3, "Двоспальний"
        EURO = 4, "Євро"

    class TYPE_FASTENING_CHOICES(models.IntegerChoices):
        BOARD = 0, "З бортами"
        RUBBER = 1, "З резинкою по кутках"

    class CHARACTERISTIC_CHOICES(models.IntegerChoices):
        WATERPROOF = 0, "Водонепроникні"
        QUILTED = 1, "Стьобаний"

    product = models.OneToOneField(to="products.Product", on_delete=models.CASCADE, related_name="mattress_covers")
    size = models.CharField(_("Розмір"), max_length=50)
    type = models.PositiveSmallIntegerField(_("Спальний розмір"), choices=SIZE_MATTRESS_CHOICES.choices)
    cover_material = models.CharField(_("Матеріал чохла"), max_length=150)
    filler = models.CharField(_("Наповнювач"), max_length=150)
    type_fastening = models.PositiveSmallIntegerField(_("Тип кріплення"), choices=TYPE_FASTENING_CHOICES.choices)
    characteristic = models.PositiveSmallIntegerField(_("Особливості"), choices=CHARACTERISTIC_CHOICES.choices)

    def __str__(self):
        return f"{self.product.name} ({self.product.article})"


class Tablecloths(models.Model):
    class Meta:
        verbose_name = _("Скатертина")
        verbose_name_plural = _("Скатертини")

    product = models.OneToOneField(to="products.Product", on_delete=models.CASCADE, related_name="tablecloths")
    size = models.CharField(_("Розмір"), max_length=50)
    material = models.CharField(_("Матеріал"), max_length=150)

    def __str__(self):
        return f"{self.product.name} ({self.product.article})"


class Pillowcase(models.Model):
    class Meta:
        verbose_name = _("Декоративна наволочка")
        verbose_name_plural = _("Декоративні наволочки")

    product = models.OneToOneField(to="products.Product", on_delete=models.CASCADE, related_name="pillowcase")
    size = models.CharField(_("Розмір"), max_length=50)
    material = models.CharField(_("Матеріал"), max_length=150)

    def __str__(self):
        return f"{self.product.name} ({self.product.article})"


class Sheet(models.Model):
    class Meta:
        verbose_name = _("Простирадло")
        verbose_name_plural = _("Простирадла")

    class MATERIAL_CHOICES(models.IntegerChoices):
        FLAX = 0, "Лляні"
        TERRY = 1, "Махрові"

    product = models.OneToOneField(to="products.Product", on_delete=models.CASCADE, related_name="sheets")
    brand = models.CharField(_("Бренд"), max_length=150)
    size = models.CharField(_("Розмір"), max_length=50)
    material = models.PositiveSmallIntegerField(_("Матеріал"), choices=MATERIAL_CHOICES.choices)

    def __str__(self):
        return f"{self.product.name} ({self.product.article})"


class KitchenTextile(models.Model):
    class Meta:
        verbose_name = _("Кухонний текстиль")
        verbose_name_plural = _("Кухонний текстиль")

    class AGE_GROUP_CHOICES(models.IntegerChoices):
        CHILDISH = 0, "Дитячий"
        ADULT = 1, "Дорослий"

    class TYPE_CHOICES(models.IntegerChoices):
        APRON = 0, "Фартух"
        TACK = 1, "Прихватка"
        MITTEN = 2, "Рукавиця"

    product = models.OneToOneField(to="products.Product", on_delete=models.CASCADE, related_name="kitchen_textiles")
    age_group = models.PositiveSmallIntegerField(_("Вікова група"), choices=AGE_GROUP_CHOICES.choices)
    type = models.PositiveSmallIntegerField(_("Тип товару"), choices=TYPE_CHOICES.choices)

    def __str__(self):
        return f"{self.product.name} ({self.product.article})"
